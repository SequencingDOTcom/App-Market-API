import json
from external.sequencing.utils import file


def save_session(params, authentication_token):
    json.dump(params,
              open(file.create_dir('/tmp/sessions/%s' % authentication_token), 'w'))


def load_session(authentication_token):
    return json.load(open('/tmp/sessions/%s' % authentication_token))


def get_sequencing_token(authentication_token):
    return load_session(authentication_token)['seq_auth_token']