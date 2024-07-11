#!/usr/bin/env python3

def debug(message):
    print("DEBUG: {}".format(message))
    return message

from argparse import ArgumentParser
from jinja2 import Environment, Template, FileSystemLoader
from pathlib import Path
import yaml
import os

# CLI arguments
parser = ArgumentParser(description="Read Ansible summary output files and create a human-readable report")
parser.add_argument("-f", "--full", dest="full_out", type=str, help="Name of the output file where the full summary will be written", default="summary_full.html")
parser.add_argument("-s", "--short", dest="short_out", type=str, help="Name of the output file where the shortened summary will be written", default="summary_short.html")
parser.add_argument("-i", "--input_dir", dest="input_dir", type=str, help="Directory containing the summary files", default="summaries")
parser.add_argument("-r", "--report_changed", dest="report_changed", action="store_true", help="Report if the output files changed. Used by Ansible")

args = parser.parse_args()

if args.report_changed:
    from hashlib import sha256

# Input data
# input files are dictionaries with a single key (hostname), value is a dict with groups as keys and a list of summaries as values
merged = dict()
for file in Path(args.input_dir).glob(f"*.yml"):
    with file.open() as f:
        merged.update(yaml.safe_load(f))
# reorder the summaries' data so that details are last. This is possibe since Python 3.6 (older versions do not preserve dict ordering,
# making this code a no-op)
for host, groups in merged.items():
    for group, summaries in groups.items():
        for summary in summaries:
            if isinstance(summary, dict) and "details" in summary.keys():
                details = summary.pop("details")
                summary["details"] = details
# also generate data grouped by "group" attribute (transpose group and host)
by_group = dict()
for host, groups in merged.items():
    for group, data in groups.items():
        if group not in by_group.keys():
            by_group[group] = {}
        if host not in by_group[group].keys():
            by_group[group][host] = []
        by_group[group][host].extend(data)

# Jinja2 environment
my_dir = os.path.abspath(os.path.dirname(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(my_dir, "summary")))
env.filters["debug"] = debug

# Templating
changed = False
output_mapping = {"full.html.j2": args.full_out, "short.html.j2": args.short_out}
for template, output in output_mapping.items():
    if args.report_changed:
        try:
            with open(output, mode="rb") as f:
                before = sha256(f.read()).hexdigest()
        except FileNotFoundError:
            before = "0" # invalid value, guaranteed to be unequal to every hash
    plate = env.get_template(template)
    rendered = plate.render(by_host=merged, by_group=by_group)
    with open(output, mode="wb") as f:
        f.write(rendered.encode("UTF-8"))
    if args.report_changed:
        after = sha256(rendered.encode("UTF-8")).hexdigest()
        if before != after:
            changed = True

if args.report_changed:
    print("changed") if changed else print("same")