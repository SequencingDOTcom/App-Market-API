using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using App_Market_API_integration.Models.Integration;
using App_Market_API_integration.Models.RequestsDto;

namespace App_Market_API_integration.Controllers
{
    public class DevController : Controller
    {
        [HttpGet]
        public JsonResult GenericFileRetrieval(FileDto fileDto)
        {
            
            var fileStream = DevSequencingHelper.RetrieveFile(fileDto.url, fileDto.fileId, 
                fileDto.sequencingAuthenticationTokenurl).Result;

            return Json(new { request = RequestInfo(), response = fileStream }, JsonRequestBehavior.AllowGet);
        }

        public JsonResult JobStatusNotification(StatusReportingDto notificationDto)
        {
            var statusResult = DevSequencingHelper.JobStatusReporting(notificationDto);

            return Json(new { request = RequestInfo(), response = statusResult }, JsonRequestBehavior.AllowGet);


        }

        public string RequestInfo()
        {
            var context = System.Web.HttpContext.Current.Request;
            return string.Format("Request Method: {0} Request URL: {1} Headers: {2} ", context.HttpMethod,
                                                                          context.Url, context.Headers);
        }

    }
}