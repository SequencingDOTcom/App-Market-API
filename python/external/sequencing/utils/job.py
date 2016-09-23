import json
import urllib2

from external.sequencing.config import SequencingEndpoints

job_status_notification_url = SequencingEndpoints.job_status_notification


def completion_notification(sequencing_job_id, status, completion_status,
                            output_files, sequencing_token,
                            error_message=None, attributes=None):
    url = '{0}?apiKey={1}'.format(job_status_notification_url, sequencing_token)
    data = {
        'sequencingJobId': sequencing_job_id,
        'status': status,
        'completionStatus': completion_status,
        'errorMessage': error_message,
        'outputFiles': output_files,
        'attributes': attributes
    }

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    return urllib2.urlopen(req, json.dumps(data))
