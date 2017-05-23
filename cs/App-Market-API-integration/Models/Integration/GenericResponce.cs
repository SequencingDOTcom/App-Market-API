using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.Integration
{
    public class GenericResponce
    {
        public string Message { get; set; }
        public object Data { get; set; }
        public int ExitCode { get; set; }
    }
}