using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using App_Market_API_integration.Models.RequestsDto;

namespace App_Market_API_integration.Models.Integration
{
    public interface IAppIntegrator
    {
        void Authentication(AuthenticationRequestDto requestDto, string appToken);
        void JobSubmission();
        CompletionStatus JobResultsRetrieval();
    }
}
