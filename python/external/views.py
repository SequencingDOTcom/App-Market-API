from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from external.sequencing import auth
from external.sequencing.payload.request import SequencingAuthenticationRequest, SequencingJobSubmissionRequest, \
    SequencingJobResultsRetrievalRequest
from external.sequencing.payload.response import AuthenticationResponse, SuccessResponse, \
    FailResponse, JobCompletedSuccessfullyResponse, JobCompletedWithErrorResponse, JobRunningResponse
from external.sequencing.utils import session, file
from external.sequencing.auth import BearerTokenAuthentication


@api_view(['POST'])
def sequencing_auth(request):
    """
    Sequencing authentication endpoint.
    Associates sequencing token with app generated auth token.
    Note that new application user will be created.
    """
    seq_req = SequencingAuthenticationRequest(request)
    app_token = auth.generate_app_token(seq_req.sequencing_token)

    session.save_session(dict(seq_auth_token=seq_req.sequencing_token,
                              seq_job_id=seq_req.seq_job_id,
                              application_id=seq_req.application_id),
                         app_token)

    return AuthenticationResponse(app_token)


@api_view(['POST'])
@authentication_classes((BearerTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def sequencing_job_register(request):
    """
    Sequencing job registration endpoint.
    """
    app_token = request.auth
    sequencing_token = session.get_sequencing_token(app_token)

    try:
        seq_req = SequencingJobSubmissionRequest(request)
        sequencing_job_id = seq_req.seq_job_id
        application_id = seq_req.application_id
        data_file_id = seq_req.data_file_id
        attributes = seq_req.attributes

        # ...
    except Exception as e:
        return FailResponse(str(e))

    return SuccessResponse()


@api_view(['POST'])
@authentication_classes((BearerTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def sequencing_job_results(request):
    """
    Provide job processing reports.
    """
    app_token = request.auth
    sequencing_token = session.get_sequencing_token(app_token)

    seq_req = SequencingJobResultsRetrievalRequest(request)
    sequencing_job_id = seq_req.seq_job_id
    application_id = seq_req.application_id

    completed = True
    if completed:
        output_files = dict(Result="https://www.somewhere.com/0/1/223/result.pdf", f2="url2")
        attributes = None
        success = True
        if success:
            return JobCompletedSuccessfullyResponse(
                        sequencing_job_id=sequencing_job_id,
                        output_files=output_files,
                        attributes=attributes)
        else:
            return JobCompletedWithErrorResponse(
                        sequencing_job_id=sequencing_job_id,
                        output_files=output_files,
                        error_message="...",
                        attributes=attributes)
    else:
        return JobRunningResponse(sequencing_job_id=sequencing_job_id)
