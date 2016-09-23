import json


class SequencingAuthenticationRequest:
    def __init__(self, request):
        payload = get_request_payload(request)
        self.sequencing_token = payload['sequencingAuthenticationToken']
        self.seq_job_id = payload['sequencingJobId']
        self.application_id = payload['applicationId']


class SequencingJobSubmissionRequest:
    def __init__(self, request):
        payload = get_request_payload(request)
        self.seq_job_id = payload['sequencingJobId']
        self.application_id = payload['applicationId']
        self.data_file_id = payload['dataFileId']

        self.attributes = {}
        if 'attributes' in payload:
            self.attributes = payload['attributes']


class SequencingJobResultsRetrievalRequest:
    def __init__(self, request):
        payload = get_request_payload(request)
        self.seq_job_id = payload['sequencingJobId']
        self.application_id = payload['applicationId']


def get_request_payload(request):
    return json.loads(request.body.decode('utf-8'))
