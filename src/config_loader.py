"""Configuration loader for environment variables and settings."""
import os
from pathlib import Path
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

logger = logging.getLogger(__name__)


class Config:
    """Central configuration class for the application."""
    
    # Reddit API Configuration
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
    REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "CanadaImmigrationLeadFinder/1.0")
    
    # Claude AI Configuration
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    
    # Google Sheets Configuration
    GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
    GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH", "config/google_service_account.json")
    
    # Telegram Configuration
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    # Application Settings
    SCHEDULER_INTERVAL_HOURS = int(os.getenv("SCHEDULER_INTERVAL_HOURS", "6"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    OUTPUT_CSV_PATH = os.getenv("OUTPUT_CSV_PATH", "output/sample_leads.csv")
    
    # Reddit Subreddits and Keywords
    SUBREDDITS = [
        "canadaimmigration",
        "ImmigrationCanada",
        "CanadianImmigrant",
        "Canada"
    ]
    
    KEYWORDS = [
        "immigration",
        "visa",
        "permanent resident",
        "express entry",
        "sponsorship",
        "work permit",
        "study permit",
        "pr",
        "canada move"
    ]
    
    @staticmethod
    def validate():
        """Validate that all required environment variables are set."""
        required_vars = {
            "REDDIT_CLIENT_ID": Config.REDDIT_CLIENT_ID,
            "REDDIT_CLIENT_SECRET": Config.REDDIT_CLIENT_SECRET,
            "CLAUDE_API_KEY": Config.CLAUDE_API_KEY,
            "GOOGLE_SHEET_ID": Config.GOOGLE_SHEET_ID,
            "TELEGRAM_BOT_TOKEN": Config.TELEGRAM_BOT_TOKEN,
            "TELEGRAM_CHAT_ID": Config.TELEGRAM_CHAT_ID,
        }
        
        missing_vars = [key for key, value in required_vars.items() if not value]
        
        if missing_vars:
            logger.warning(f"Missing environment variables: {', '.join(missing_vars)}")
            return False
        
        return True


def setup_logging():
    """Setup logging configuration."""
    import sys
    import io
    
    # Handle Windows encoding issues
    if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
        # Reconfigure stdout to use UTF-8 for emoji support
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    
    logging.basicConfig(
        level=Config.LOG_LEVEL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )


if __name__ == "__main__":
    setup_logging()
    if Config.validate():
        print("✓ All configuration variables are set correctly")
    else:
        print("✗ Some configuration variables are missing")
