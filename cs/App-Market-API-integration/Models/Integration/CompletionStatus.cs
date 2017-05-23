using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.Integration
{
    public enum CompletionStatus
    {
        Success = 0,
        Unknown = 1,
        ErrorDownloading = 2,
        ErrorProcessing = 3
    }
}