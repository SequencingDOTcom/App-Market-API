using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.RequestsDto
{
    public class StatusReportingDto
    {
        public string uri { get; set; }
        public string sequencingAuthenticationToken { get; set; }
        public long sequencingJobId { get; set; }
        public int status { get; set; }
        public int completionStatus { get; set; }
        public  string errorMessage { get; set; }
        public Dictionary<string, string> outputFiles { get; set; }
        public Dictionary<string, string> attributes { get; set; }
        public object callback { get; set; }

    }
}