# JWK secrets generator - internal tool to regenerate jwk keys

Simple cli internal tool to help you generate new jwk secrets for inventory.
After you generate secrets, you need to manually distribute those secrets into the inventory.

All requirements of this tool are installed as part of Ansible installation; see `docs/installing_ansible.md` for details.
Don't forget to activate your venv using `. ~/venv/bin/activate`

To use the generator, run following command: `python generator.py`. It will print (to the standard output) new fresh jwk keys for all current microservices.
In order to use those, redirect the output to a vars file in your inventory (e. g. `ansible/inventories/example/group_vars/all/jwk_keys.yml`).
The generator will produce exact format that is used in vars, overriding default values.

Example output for dpm microservice:

```yaml
dpm_jwt_key:
  content: '{"kty": "EC", "crv": "P-256", "x": "KZptNugjx_OSFG0dIgBElAwn_ZuLyBH4iA4a-rVT30A",
    "y": "SAMDhR_K9V8H9juA9-z9XB4e0SluAkOx0qKrKHnDw9w", "kid": "pliVl6rPftrNXjvMER5gI0eEiZD4C0zsgO2MmAlQDuY",
    "alg": "ES256"}'
  fp: pliVl6rPftrNXjvMER5gI0eEiZD4C0zsgO2MmAlQDuY
  name: dpm-prod-key
  private: eyJjcnYiOiJQLTI1NiIsImQiOiJnNUdQWUJqSGJoU1V1MFJXM2JtTWIwanJReG04YVA0TG10VkdTcFAtQTk0Iiwia3R5IjoiRUMiLCJ4IjoiS1pwdE51Z2p4X09TRkcwZElnQkVsQXduX1p1THlCSDRpQTRhLXJWVDMwQSIsInkiOiJTQU1EaFJfSzlWOEg5anVBOS16OVhCNGUwU2x1QWtPeDBxS3JLSG5Edzl3In0=
```

Format of our jwk keys is rather cumbersome, but I guess that it's what config service expects. (e.g. it needs to be validated if `kid` in `microservice.jwt_key.content` is necessary).
What we see here is just simple jwk key defined here https://www.ietf.org/rfc/rfc7517.txt.
Parameters are Elliptic curve P-256  ES256 algorithm.

Key looks like this:
```json
{
    "kty": "EC",
    "d": "uGPnhGJp7xOsdlMt_IQSFzu7E7WMzYgAh9ghndPhp6U",
    "crv": "P-256",
    "x": "JOBKlzPc1ZgWrypsBaryUUIKWlVfVcXMMpc9yHtk2Ug",
    "y": "t2KAZub-ACo953dPG6KbWgF6UvR9YDGpkzEk7wl_0ck",
    "kid": "Some meaningful key name"
}
```
All of this forms private key. "d" is secret so public key is the same private minus "d" attribute.
For some reason in our vars file we don't have same format for public and private key.
Public key is stored as pure json, but private key is store as base64 json encoded string.
Since configuration service can have multiple jwk keys deployed, it's using optional `kid` parameter to name keys.
Config service is using key fingerprint as value for `kid` attribute, but there can be any string.
