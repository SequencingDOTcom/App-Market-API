using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.RequestsDto
{
    public class AuthenticationRequestDto
    {
        public string sequencingAuthenticationToken { get; set; }
        public long sequencingJobId { get; set; }
        public int applicationId { get; set; }
        public string userId { get; set; }
        public UserDetails userDetails { get; set; }

    }

    public class UserDetails
    {
        public string userEmail { get; set; }
        public string userFirstName { get; set; }
        public string userLastName { get; set; }
    }
}