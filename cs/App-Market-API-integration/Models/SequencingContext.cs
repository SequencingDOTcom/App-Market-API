using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using App_Market_API_integration.Models.UserAuth;

namespace App_Market_API_integration.Models
{
    public class SequencingContext : DbContext
    {

        public SequencingContext() :
            base("SequencingConnection")
        { }

        public DbSet<SequencingUser> UserInfo { get; set; }
    }
}