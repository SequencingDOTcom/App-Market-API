from rest_framework.decorators import api_view

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from external.sequencing.config import SequencingEndpoints, DefaultConfigs

import urllib2

import json

from external.sequencing.utils import file, job


def dev_console(request):
    return render(request, 'dev_console.html', {'endpoints': SequencingEndpoints, 'configs': DefaultConfigs})


@api_view(['POST'])
def dev_genetic_file_retrieval_test(request):
    payload = request.data

    file_id = payload['id']
    uri = payload['uri']
    seq_auth_token = payload['sequencingAuthenticationToken']

    raw_req = """
Request Method: GET

Request URL: {0}?id={1}

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11

Authorization: Bearer {2}

Accept: application/octet-stream
              """.format(uri, file_id, seq_auth_token)

    resp = file.retrieve_file(data_file_id=file_id, sequencing_token=seq_auth_token, uri=uri)

    return JsonResponse({'request': raw_req, 'response': str(resp.info())})


@api_view(['POST'])
def dev_job_status_notification_test(request):
    payload = request.data

    uri = payload['uri']
    seq_auth_token = payload['sequencingAuthenticationToken']
    seq_job_id = payload['sequencingJobId']
    status = payload['status']
    completion_status = payload['completionStatus']
    error_message = payload['errorMessage']
    output_files = payload['outputFiles']
    attributes = payload['attributes']
    callback = payload['callback']

    resp = job.job_status_reporting(sequencing_token=seq_auth_token,
                             attributes=attributes,
                             completion_status=completion_status,
                             error_message=error_message,
                             sequencing_job_id=seq_job_id,
                             status=status,
                             output_files=output_files,
                             callback=callback,
                             uri=uri)

    return JsonResponse({'request': '', 'response': resp})
