namespace App_Market_API_integration.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class DataMigrations1 : DbMigration
    {
        public override void Up()
        {
            DropPrimaryKey("dbo.SequencingUsers");
            AlterColumn("dbo.SequencingUsers", "UserId", c => c.Long(nullable: false));
            AlterColumn("dbo.SequencingUsers", "AppToken", c => c.String(nullable: false, maxLength: 128));
            AddPrimaryKey("dbo.SequencingUsers", "AppToken");
        }
        
        public override void Down()
        {
            DropPrimaryKey("dbo.SequencingUsers");
            AlterColumn("dbo.SequencingUsers", "AppToken", c => c.String());
            AlterColumn("dbo.SequencingUsers", "UserId", c => c.Long(nullable: false, identity: true));
            AddPrimaryKey("dbo.SequencingUsers", "UserId");
        }
    }
}
