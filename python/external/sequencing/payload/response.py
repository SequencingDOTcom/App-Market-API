from django.http import JsonResponse


class AuthenticationResponse(JsonResponse):
    def __init__(self, authentication_token):
        JsonResponse.__init__(self, {'authenticationToken': str(authentication_token)})


class SuccessResponse(JsonResponse):
    def __init__(self):
        JsonResponse.__init__(self, {'status': 0})


class FailResponse(JsonResponse):
    def __init__(self, error):
        JsonResponse.__init__(self, {'status': 1, 'error': error})


class JobResultResponse(JsonResponse):
    def __init__(self, sequencing_job_id, status, completion_status, error_message=None,
                 output_files=None, attributes=None, callback=None):
        JsonResponse.__init__(self, {'sequencingJobId': sequencing_job_id,
                                     'status': status,
                                     'completionStatus': completion_status,
                                     'errorMessage': error_message,
                                     'outputFiles': output_files,
                                     'attributes': attributes,
                                     'callback': callback})


class JobRunningResponse(JobResultResponse):
    def __init__(self, sequencing_job_id):
        JobResultResponse.__init__(self, sequencing_job_id=sequencing_job_id,
                                   status=0, completion_status=None)


class JobCompletedSuccessfullyResponse(JobResultResponse):
    def __init__(self, sequencing_job_id, output_files, attributes=None, callback=None):
        JobResultResponse.__init__(self, sequencing_job_id=sequencing_job_id,
                                   status=1,
                                   completion_status=0,
                                   output_files=output_files,
                                   attributes=attributes,
                                   callback=callback)


class JobCompletedWithErrorResponse(JobResultResponse):
    def __init__(self, sequencing_job_id, output_files, error_message, attributes=None, callback=None):
        JobResultResponse.__init__(self, sequencing_job_id=sequencing_job_id,
                                   status=1,
                                   completion_status=1,
                                   output_files=output_files,
                                   error_message=error_message,
                                   attributes=attributes,
                                   callback=callback)
