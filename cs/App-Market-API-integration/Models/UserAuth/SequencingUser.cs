using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.UserAuth
{
    public class SequencingUser
    {
        public long UserId { get; set; }
        public string SequencingToken { get; set; }
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public string AppToken { get; set; }
        public long JobId { get; set; }
        public long ApplicationId { get; set; }
    }
}