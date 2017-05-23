using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Mvc.Filters;

namespace App_Market_API_integration.Models.UserAuth
{
    public class CustomAuthenticationAttribute : ActionFilterAttribute, IAuthenticationFilter
    {
        SequencingUserRepository repository = new SequencingUserRepository();

        public void OnAuthentication(AuthenticationContext filterContext)
        {
            var headers = System.Web.HttpContext.Current.Request.Headers;
            if (headers["Authorization"] != null)
            {
                var appToken = headers["Authorization"].Split(new char[] { ' ' })[1];
                if (repository.GetUser(appToken) == null)
                    filterContext.Result = new HttpUnauthorizedResult();
                else
                    HttpContext.Current.Session["Authorization"] = appToken;
            }
        }

        public void OnAuthenticationChallenge(AuthenticationChallengeContext filterContext)
        {
        }
    }
}