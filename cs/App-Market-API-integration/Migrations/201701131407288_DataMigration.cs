namespace App_Market_API_integration.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class DataMigration : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.SequencingUsers",
                c => new
                    {
                        UserId = c.Long(nullable: false, identity: true),
                        AuthToken = c.String(),
                        JobId = c.Long(nullable: false),
                        ApplicationId = c.Long(nullable: false),
                    })
                .PrimaryKey(t => t.UserId);
            
        }
        
        public override void Down()
        {
            DropTable("dbo.SequencingUsers");
        }
    }
}
