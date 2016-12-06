from rest_framework.decorators import api_view

from django.http import JsonResponse
from django.shortcuts import render

from external.sequencing.config import SequencingEndpoints, DefaultConfigs

from external.sequencing.utils import file, job


def dev_console(request):
    return render(request, 'dev_console.html', {'endpoints': SequencingEndpoints, 'configs': DefaultConfigs})


@api_view(['POST'])
def dev_genetic_file_retrieval_test(request):
    payload = request.data

    file_id = payload['id']
    uri = payload['uri']
    seq_auth_token = payload['sequencingAuthenticationToken']

    request, response = file.retrieve_file(data_file_id=file_id, sequencing_token=seq_auth_token, uri=uri)

    return JsonResponse({'request': __request_info(request), 'response': str(response.info())})


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

    request, response = job.job_status_reporting(sequencing_token=seq_auth_token,
                                                 attributes=attributes,
                                                 completion_status=completion_status,
                                                 error_message=error_message,
                                                 sequencing_job_id=seq_job_id,
                                                 status=status,
                                                 output_files=output_files,
                                                 callback=callback,
                                                 uri=uri)

    return JsonResponse({'request': __request_info(request), 'response': str(response.info())})


def __request_info(request):
    return "Request Method: {0}\nRequest URL: {1}\nHeaders: {2}\n".format(request.get_method(),
                                                                          request.get_full_url(), request.headers)
