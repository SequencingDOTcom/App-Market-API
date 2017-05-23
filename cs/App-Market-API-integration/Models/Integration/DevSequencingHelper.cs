using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using System.Web;
using App_Market_API_integration.Models.RequestsDto;
using Microsoft.Owin.Security;

namespace App_Market_API_integration.Models.Integration
{
    public class DevSequencingHelper
    {
        public static async Task<byte[]> RetrieveFile(string url, string id, string apiKey)
        {
            using (var client = new HttpClient())
            {
                var request = new HttpRequestMessage()
                {
                    RequestUri = new Uri(url + string.Format("?{0}", id)),
                    Method = HttpMethod.Get,
                };
                request.Headers.Add("Authorization", "Bearer " + apiKey);

                var response = await client.SendAsync(request, HttpCompletionOption.ResponseHeadersRead).ConfigureAwait(false);

                return response.Content.ReadAsByteArrayAsync().Result;
            }
        }

        public static async Task<object> JobStatusReporting(StatusReportingDto notificationDto)
        {
            var data = new Dictionary<string, string>
            {
                    { "sequencingJobId", notificationDto.sequencingJobId.ToString() },
                    { "status", notificationDto.status.ToString() },
                    { "completionStatus", notificationDto.completionStatus.ToString() },
                    { "errorMessage", notificationDto.errorMessage.ToString() },
                    { "outputFiles", notificationDto.outputFiles.ToString() },
                    { "attributes", notificationDto.attributes.ToString()},
                    { "callback", notificationDto.callback.ToString() }
            };
            using (var client = new HttpClient())
            {
                var request = new HttpRequestMessage()
                {
                    RequestUri = new Uri(notificationDto.uri),
                    Method = HttpMethod.Post,
                };
                request.Headers.Add("Authorization", "Bearer " + notificationDto.sequencingAuthenticationToken);
                request.Content = new FormUrlEncodedContent(data);

                var response = await client.SendAsync(request, HttpCompletionOption.ResponseHeadersRead).ConfigureAwait(false);

                return response.Content.ReadAsByteArrayAsync().Result;
            }
        }
    }
}