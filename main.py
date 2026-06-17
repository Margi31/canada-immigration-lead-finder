"""Main entry point for the Canada Immigration Lead Finder pipeline."""
import logging
import sys
import csv
from datetime import datetime
from typing import List, Dict
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.config_loader import Config, setup_logging
from src.reddit_scraper import RedditScraper
from posts.ai_qualifier import AIQualifier
from Claude.sheets_uploader import SheetsUploader
from Sheets.telegram_notifier import TelegramNotifier
import asyncio

logger = logging.getLogger(__name__)


class ImmigrationLeadFinderPipeline:
    """Main pipeline orchestrator."""
    
    def __init__(self):
        """Initialize pipeline components."""
        self.scraper = RedditScraper()
        self.qualifier = AIQualifier()
        self.uploader = SheetsUploader()
        self.notifier = TelegramNotifier()
        self.output_csv = Config.OUTPUT_CSV_PATH
        
        # Ensure output directory exists
        Path(self.output_csv).parent.mkdir(parents=True, exist_ok=True)
    
    def run_pipeline(self) -> Dict:
        """
        Run the complete pipeline.
        
        Returns:
            Dictionary with pipeline results
        """
        logger.info("=" * 60)
        logger.info("🚀 Starting Canada Immigration Lead Finder Pipeline")
        logger.info("=" * 60)
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "posts_scraped": 0,
            "leads_qualified": 0,
            "sheets_uploaded": False,
            "notifications_sent": 0
        }
        
        try:
            # Step 1: Scrape Reddit
            logger.info("\n📱 Step 1: Scraping Reddit...")
            posts = self.scraper.scrape_all_subreddits(limit=50)
            results["posts_scraped"] = len(posts)
            logger.info(f"✓ Scraped {len(posts)} posts")
            
            if not posts:
                logger.warning("No posts found. Exiting pipeline.")
                return results
            
            # Step 2: Qualify leads with AI
            logger.info("\n🤖 Step 2: Qualifying leads with Claude AI...")
            qualified_leads = self.qualifier.qualify_batch(posts)
            results["leads_qualified"] = len(qualified_leads)
            logger.info(f"✓ Qualified {len(qualified_leads)} leads")
            
            if not qualified_leads:
                logger.warning("No qualified leads found.")
                return results
            
            # Step 3: Upload to Google Sheets
            logger.info("\n📊 Step 3: Uploading to Google Sheets...")
            sheets_success = self.uploader.upload_leads(qualified_leads)
            results["sheets_uploaded"] = sheets_success
            
            if sheets_success:
                logger.info("✓ Leads uploaded to Google Sheets")
            else:
                logger.warning("Google Sheets upload skipped (API not configured)")
            
            # Step 4: Send Telegram notifications
            logger.info("\n💬 Step 4: Sending Telegram notifications...")
            notifications = asyncio.run(
                self.notifier.send_batch_notifications(qualified_leads[:5])  # Limit to 5
            )
            results["notifications_sent"] = notifications
            logger.info(f"✓ Sent {notifications} notifications")
            
            # Step 5: Save to CSV
            logger.info("\n💾 Step 5: Saving to CSV...")
            self._save_to_csv(qualified_leads)
            logger.info(f"✓ Saved to {self.output_csv}")
            
        except Exception as e:
            logger.error(f"Pipeline error: {e}", exc_info=True)
        
        # Print summary
        self._print_summary(results)
        
        return results
    
    def _save_to_csv(self, leads: List[Dict]):
        """Save qualified leads to CSV file."""
        if not leads:
            logger.warning("No leads to save")
            return
        
        try:
            fieldnames = [
                "id", "title", "author", "content", "contact_info",
                "lead_type", "confidence", "needs", "url", "source",
                "qualified_at"
            ]
            
            with open(self.output_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for lead in leads:
                    row = {field: lead.get(field, "") for field in fieldnames}
                    if isinstance(row.get('needs'), list):
                        row['needs'] = ", ".join(row['needs'])
                    writer.writerow(row)
            
            logger.info(f"✓ Saved {len(leads)} leads to {self.output_csv}")
        
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")
    
    def _print_summary(self, results: Dict):
        """Print pipeline summary."""
        logger.info("\n" + "=" * 60)
        logger.info("📋 PIPELINE SUMMARY")
        logger.info("=" * 60)
        logger.info(f"⏱️  Timestamp: {results['timestamp']}")
        logger.info(f"📱 Posts Scraped: {results['posts_scraped']}")
        logger.info(f"✅ Leads Qualified: {results['leads_qualified']}")
        logger.info(f"📊 Sheets Uploaded: {'Yes' if results['sheets_uploaded'] else 'No'}")
        logger.info(f"💬 Notifications Sent: {results['notifications_sent']}")
        logger.info("=" * 60)


def main():
    """Main function."""
    # Setup logging
    setup_logging()
    
    # Validate configuration
    if not Config.validate():
        logger.warning("⚠️  Some configuration variables are missing")
        logger.warning("   Refer to .env.example and create a .env file")
    
    # Run pipeline
    pipeline = ImmigrationLeadFinderPipeline()
    results = pipeline.run_pipeline()
    
    # Exit with appropriate code
    if results["leads_qualified"] > 0:
        logger.info("\n✅ Pipeline completed successfully!")
        sys.exit(0)
    else:
        logger.info("\n⚠️  Pipeline completed but no qualified leads found")
        sys.exit(1)


if __name__ == "__main__":
    main()
