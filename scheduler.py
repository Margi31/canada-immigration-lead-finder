"""Background scheduler for automatic pipeline runs."""
import schedule
import time
import logging
import sys
from pathlib import Path
from datetime import datetime

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.config_loader import Config, setup_logging
from main import ImmigrationLeadFinderPipeline

logger = logging.getLogger(__name__)


class PipelineScheduler:
    """Schedules the pipeline to run at regular intervals."""
    
    def __init__(self, interval_hours: int = None):
        """
        Initialize scheduler.
        
        Args:
            interval_hours: How often to run the pipeline (default from config)
        """
        self.interval_hours = interval_hours or Config.SCHEDULER_INTERVAL_HOURS
        self.pipeline = ImmigrationLeadFinderPipeline()
        self.is_running = False
    
    def schedule_pipeline(self):
        """Schedule the pipeline to run at regular intervals."""
        schedule.every(self.interval_hours).hours.do(self.run_pipeline_task)
        logger.info(f"✓ Pipeline scheduled to run every {self.interval_hours} hours")
    
    def run_pipeline_task(self):
        """Task to run the pipeline."""
        try:
            logger.info(f"\n{'='*60}")
            logger.info(f"🔄 Scheduled pipeline run at {datetime.now()}")
            logger.info(f"{'='*60}\n")
            
            self.pipeline.run_pipeline()
            
        except Exception as e:
            logger.error(f"Scheduler error: {e}", exc_info=True)
    
    def start(self):
        """Start the scheduler in a blocking loop."""
        self.is_running = True
        logger.info("🚀 Scheduler started. Press Ctrl+C to stop.")
        
        try:
            while self.is_running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        
        except KeyboardInterrupt:
            logger.info("\n⏹️  Scheduler stopped by user")
            self.is_running = False
        
        except Exception as e:
            logger.error(f"Scheduler encountered an error: {e}", exc_info=True)
    
    def stop(self):
        """Stop the scheduler."""
        self.is_running = False
        logger.info("Scheduler stopped")


def run_scheduler():
    """Run the scheduler."""
    setup_logging()
    
    logger.info("=" * 60)
    logger.info("🕐 Canada Immigration Lead Finder Scheduler")
    logger.info("=" * 60)
    
    scheduler = PipelineScheduler()
    scheduler.schedule_pipeline()
    scheduler.start()


if __name__ == "__main__":
    run_scheduler()
