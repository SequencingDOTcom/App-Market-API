using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using App_Market_API_integration.Models.RequestsDto;
using Microsoft.Owin.Security;
using App_Market_API_integration.Models.UserAuth;
using App_Market_API_integration.Models.Integration;
using App_Market_API_integration.Migrations;

namespace App_Market_API_integration.Controllers
{

    public class ExternalController : Controller
    {

        IAppIntegrator integration;
        IUserRepository<SequencingUser> repository = new SequencingUserRepository(); 
        public ExternalController(IAppIntegrator integr)
        {
            this.integration = integr;
        }

        [HttpPost]
        [ActionName("auth")]
        public string Authentication(AuthenticationRequestDto registerRequest)
        {
            var appToken = Guid.NewGuid().ToString();
            integration.Authentication(registerRequest, appToken);
            return appToken;
        }


        [HttpPost]
        [CustomAuthentication]
       
        public JsonResult JobRegister(JobRegisterDto registerRequest)
        {
            GenericResponce response = null;
            try
            {
                var appToken = System.Web.HttpContext.Current.Session["Authorization"].ToString();
                var sequencingKey = repository.GetUser(appToken).SequencingToken;

                /*Calling each party implementation */
                integration.JobSubmission();

                return Json(new { status = 0}, JsonRequestBehavior.AllowGet);
            }
            catch (Exception ex)
            {            
                return Json(new {status = 1, error = ex}, JsonRequestBehavior.AllowGet);
            }       
        }

        [HttpPost]
        [CustomAuthentication]
        public JsonResult GetJobResult(JobRegisterDto registerRequest)
        {
            var appToken = System.Web.HttpContext.Current.Session["Authorization"].ToString();
            var sequencingKey = repository.GetUser(appToken).SequencingToken;

            var outputfiles = new Dictionary<string, string>();

            var status = integration.JobResultsRetrieval();

            if (status.Equals(CompletionStatus.Success))
            {
                var genericObject = new
                {
                    sequencingJobId = registerRequest.sequencingJobId,
                    status = JobStatus.Completed,
                    completionStatus = CompletionStatus.Success,
                    outputFiles = outputfiles
                };

                return Json(genericObject, JsonRequestBehavior.AllowGet);
            }
            else
            {
                var genericObject = new
                {
                    sequencingJobId = registerRequest.sequencingJobId,
                    status = JobStatus.Completed,
                    completionStatus = CompletionStatus.Success,
                    outputFiles = outputfiles,
                    errorMessage = ""
                };

                return Json(genericObject, JsonRequestBehavior.AllowGet);
            }

        }
    }
}