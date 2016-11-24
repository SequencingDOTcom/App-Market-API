import json
import urllib2

from external.sequencing.config import SequencingEndpoints


def job_status_reporting(sequencing_token, sequencing_job_id, status,
                         completion_status=None, error_message=None,
                         output_files=None, attributes=None, callback=None,
                         uri=SequencingEndpoints.job_status_notification):
    url = '{0}'.format(uri, sequencing_token)

    data = {
        'sequencingJobId': sequencing_job_id,
        'status': status,
        'completionStatus': completion_status,
        'errorMessage': error_message,
        'outputFiles': output_files,
        'attributes': attributes,
        'callback': callback
    }

    headers = {
        'Authorization': 'Bearer %s' % sequencing_token,
        'Content-Type': 'application/json'
    }

    request = urllib2.Request(url, data=json.dumps(data), headers=headers)
    response = urllib2.urlopen(request)

    return request, response
