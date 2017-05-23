using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.RequestsDto
{
    public class FileDto
    {
        public string fileId { get; set; }
        public string url { get; set; }
        public string sequencingAuthenticationTokenurl { get; set; }
    }
}