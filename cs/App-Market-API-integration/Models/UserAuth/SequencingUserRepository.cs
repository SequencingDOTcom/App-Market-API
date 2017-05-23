using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.UserAuth
{
    public class SequencingUserRepository : IUserRepository<SequencingUser>
    {
        public void CreateUser(SequencingUser userInfo)
        {
            try
            {
                using (SequencingContext db = new SequencingContext())
                {
                    db.UserInfo.Add(userInfo);
                    db.SaveChanges();
                }
            }
            catch (Exception ex)
            {

            }

        }

        public SequencingUser GetUser(string appToken)
        {
            using (SequencingContext db = new SequencingContext())
                return db.UserInfo.Where(u => u.AppToken == appToken).Select(user => user).FirstOrDefault();
        }
    }
}