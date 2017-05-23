using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.RequestsDto
{
    public class JobRegisterDto
    {
        public long sequencingJobId;
        public int applicationId;
        public string dataFileId;
        public Dictionary<string, string> attributes;
        public string userId;

    }
}