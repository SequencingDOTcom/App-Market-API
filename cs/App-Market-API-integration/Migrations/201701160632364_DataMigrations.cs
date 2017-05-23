namespace App_Market_API_integration.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class DataMigrations : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.SequencingUsers", "SequencingToken", c => c.String());
            AddColumn("dbo.SequencingUsers", "AppToken", c => c.String());
            DropColumn("dbo.SequencingUsers", "AuthToken");
        }
        
        public override void Down()
        {
            AddColumn("dbo.SequencingUsers", "AuthToken", c => c.String());
            DropColumn("dbo.SequencingUsers", "AppToken");
            DropColumn("dbo.SequencingUsers", "SequencingToken");
        }
    }
}
