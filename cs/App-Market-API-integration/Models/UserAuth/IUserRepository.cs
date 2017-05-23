using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace App_Market_API_integration.Models.UserAuth
{
    public interface IUserRepository<T>
    {
        T GetUser(string appToken);

        void CreateUser(T userInfo);
    }
}