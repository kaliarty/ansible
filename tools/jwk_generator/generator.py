#!/usr/bin/env python3
from jwcrypto import jwk
import base64
import yaml
import json

secrets = {}
services = {
  'anomaly_detection_anomaly_detector': 'anomaly-detection-anomaly-detector',
  'audit': 'audit',
  'dpe': 'dpe',
  'dpm': 'dpm',
  'frontend': 'mmm-fe',
  'mdm_server': 'mdm',
  'mmm': 'mmm-be',
  'rdm': 'rdm',
  'term_suggestions_api': 'term-suggestions-api',
  'term_suggestions_feedback': 'term-suggestions-feedback',
  'term_suggestions_neighbors': 'term-suggestions-neighbors',
  'term_suggestions_recommender': 'term-suggestions-recommender',
  'task': 'task',
  'workflow': 'workflow',
  'comment': 'comment',
  'dmm': 'dmm',
  'mde_lineage': 'mde_lineage',
  'dqf': 'dqf'
}

for service_name, service_key_name in services.items() :
    key = jwk.JWK.generate(kty='EC', crv='P-256')
    fingerprint = key.thumbprint()
    # additional enhancement required by cs (although not sure if it's really required and could not be dropped since it's not part of jwk standard)
    enrichment = {'kid': fingerprint, 'alg': 'ES256'}

    private_key = key.export_private(as_dict=True)
    private_key.update(enrichment)
    private_key = base64.b64encode(json.dumps(private_key).encode()).decode('UTF-8')

    public_key = key.export_public(True)
    public_key.update(enrichment)

    jwk_data = {'content': json.dumps(public_key), 'fp': fingerprint, 'name':  service_key_name + '-prod-key', 'private': private_key}
    secrets["{}_jwt_key".format(service_name)] = jwk_data

print(yaml.dump(secrets))
