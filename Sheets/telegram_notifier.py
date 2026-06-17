"""Telegram notifications for new qualified leads."""
import logging
from typing import List, Dict
from telegram import Bot
from telegram.error import TelegramError
import asyncio
from src.config_loader import Config

logger = logging.getLogger(__name__)


class TelegramNotifier:
    """Sends Telegram notifications for qualified leads."""
    
    def __init__(self):
        """Initialize Telegram bot."""
        try:
            self.bot = Bot(token=Config.TELEGRAM_BOT_TOKEN)
            self.chat_id = Config.TELEGRAM_CHAT_ID
            logger.info("✓ Telegram bot initialized")
        except Exception as e:
            logger.error(f"Failed to initialize Telegram bot: {e}")
            self.bot = None
    
    async def send_lead_notification(self, lead: Dict) -> bool:
        """
        Send notification for a single qualified lead.
        
        Args:
            lead: Qualified lead dictionary
        
        Returns:
            True if notification sent successfully
        """
        if not self.bot:
            logger.warning("Telegram bot not initialized")
            return False
        
        try:
            message = self._format_lead_message(lead)
            
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode='HTML'
            )
            
            logger.info(f"✓ Notification sent for lead: {lead.get('title', 'Unknown')}")
            return True
        
        except TelegramError as e:
            logger.error(f"Telegram error sending notification: {e}")
            return False
        except Exception as e:
            logger.error(f"Error sending notification: {e}")
            return False
    
    async def send_batch_notifications(self, leads: List[Dict]) -> int:
        """
        Send notifications for multiple leads.
        
        Args:
            leads: List of qualified leads
        
        Returns:
            Number of successful notifications
        """
        if not self.bot:
            logger.warning("Telegram bot not initialized")
            return 0
        
        success_count = 0
        
        for lead in leads:
            if await self.send_lead_notification(lead):
                success_count += 1
        
        return success_count
    
    async def send_summary_notification(self, leads: List[Dict]) -> bool:
        """
        Send a summary notification for all new leads.
        
        Args:
            leads: List of qualified leads
        
        Returns:
            True if notification sent successfully
        """
        if not self.bot or not leads:
            return False
        
        try:
            message = self._format_summary_message(leads)
            
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode='HTML'
            )
            
            logger.info(f"✓ Summary notification sent ({len(leads)} leads)")
            return True
        
        except TelegramError as e:
            logger.error(f"Telegram error sending summary: {e}")
            return False
        except Exception as e:
            logger.error(f"Error sending summary: {e}")
            return False
    
    def _format_lead_message(self, lead: Dict) -> str:
        """Format a lead into a Telegram message."""
        title = lead.get('title', 'Unknown')
        author = lead.get('author', 'Unknown')
        lead_type = lead.get('lead_type', 'General')
        confidence = lead.get('confidence', 0)
        contact = lead.get('contact_info', 'N/A')
        url = lead.get('url', '')
        
        message = f"""
🎯 <b>New Qualified Lead</b>

<b>Title:</b> {title[:100]}
<b>Author:</b> {author}
<b>Type:</b> {lead_type}
<b>Confidence:</b> {confidence:.0%}
<b>Contact:</b> <code>{contact}</code>

<a href="{url}">View on Reddit</a>
        """.strip()
        
        return message
    
    def _format_summary_message(self, leads: List[Dict]) -> str:
        """Format a summary message for multiple leads."""
        lead_types = {}
        for lead in leads:
            lt = lead.get('lead_type', 'Unknown')
            lead_types[lt] = lead_types.get(lt, 0) + 1
        
        type_breakdown = "\n".join(
            [f"  • {lt}: {count}" for lt, count in lead_types.items()]
        )
        
        avg_confidence = sum(l.get('confidence', 0) for l in leads) / len(leads) if leads else 0
        
        message = f"""
📊 <b>Daily Lead Summary</b>

<b>Total Leads:</b> {len(leads)}
<b>Average Confidence:</b> {avg_confidence:.0%}

<b>Breakdown by Type:</b>
{type_breakdown}

Check Google Sheets for full details.
        """.strip()
        
        return message
    
    def send_notification_sync(self, lead: Dict) -> bool:
        """
        Send notification synchronously (blocking).
        
        Args:
            lead: Qualified lead dictionary
        
        Returns:
            True if successful
        """
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        return loop.run_until_complete(self.send_lead_notification(lead))


async def main():
    """Test the Telegram notifier."""
    notifier = TelegramNotifier()
    
    test_lead = {
        "title": "Looking for PR sponsorship",
        "author": "sarah_khan",
        "lead_type": "sponsorship",
        "confidence": 0.85,
        "contact_info": "sarah@example.com",
        "url": "https://reddit.com/r/canadaimmigration/..."
    }
    
    if notifier.bot:
        success = await notifier.send_lead_notification(test_lead)
        print(f"\n💬 Notification result: {'✓ Sent' if success else '✗ Failed'}")
    else:
        print("✗ Telegram bot not initialized")


if __name__ == "__main__":
    from src.config_loader import setup_logging
    setup_logging()
    asyncio.run(main())
