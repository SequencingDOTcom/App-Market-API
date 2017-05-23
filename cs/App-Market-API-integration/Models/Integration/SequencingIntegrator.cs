using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using App_Market_API_integration.Models.RequestsDto;
using App_Market_API_integration.Models.UserAuth;

namespace App_Market_API_integration.Models.Integration
{
    public class SequencingIntegrator : IAppIntegrator
    {
        private SequencingUserRepository repository = new SequencingUserRepository();

        public void Authentication(AuthenticationRequestDto requestDto, string appToken)
        {
            SequencingUser user = repository.GetUser(appToken);
            if (user == null)
                repository.CreateUser(new SequencingUser
                {
                    SequencingToken = requestDto.sequencingAuthenticationToken,
                    AppToken = appToken,
                    JobId = requestDto.sequencingJobId,
                    ApplicationId = requestDto.applicationId,
                    UserId = long.Parse(requestDto.userId)
                });
        }

        public CompletionStatus JobResultsRetrieval()
        {
            throw new NotImplementedException();
        }

        public void JobSubmission()
        {
            throw new NotImplementedException();
        }

    }
}