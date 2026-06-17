"""Google Sheets uploader for qualified leads."""
import logging
from typing import List, Dict
import os
from src.config_loader import Config

try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from google.auth.exceptions import DefaultCredentialsError
    from google.api_python_client import discovery
    GOOGLE_SHEETS_AVAILABLE = True
except ImportError:
    GOOGLE_SHEETS_AVAILABLE = False

logger = logging.getLogger(__name__)


class SheetsUploader:
    """Uploads qualified leads to Google Sheets."""
    
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    def __init__(self):
        """Initialize Google Sheets API connection."""
        self.service = None
        self.spreadsheet_id = Config.GOOGLE_SHEET_ID
        
        if not GOOGLE_SHEETS_AVAILABLE:
            logger.warning("Google Sheets API libraries not available. Install with: pip install google-api-python-client")
            return
        
        try:
            credentials_path = Config.GOOGLE_CREDENTIALS_PATH
            
            if not os.path.exists(credentials_path):
                logger.warning(f"Google credentials file not found: {credentials_path}")
                return
            
            credentials = Credentials.from_service_account_file(
                credentials_path,
                scopes=self.SCOPES
            )
            
            self.service = discovery.build('sheets', 'v4', credentials=credentials)
            logger.info("✓ Google Sheets API connection established")
        
        except Exception as e:
            logger.error(f"Failed to initialize Google Sheets API: {e}")
    
    def upload_leads(self, leads: List[Dict], sheet_name: str = "Qualified Leads") -> bool:
        """
        Upload qualified leads to Google Sheets.
        
        Args:
            leads: List of qualified lead dictionaries
            sheet_name: Name of the sheet to upload to
        
        Returns:
            True if upload successful, False otherwise
        """
        if not self.service or not leads:
            logger.warning("Service not initialized or no leads to upload")
            return False
        
        try:
            # Prepare headers
            headers = [
                "ID",
                "Title",
                "Author",
                "Contact Info",
                "Lead Type",
                "Confidence",
                "Needs",
                "URL",
                "Qualified At",
                "Source"
            ]
            
            # Prepare data rows
            rows = [headers]
            for lead in leads:
                row = [
                    lead.get("id", ""),
                    lead.get("title", ""),
                    lead.get("author", ""),
                    lead.get("contact_info", ""),
                    lead.get("lead_type", ""),
                    str(lead.get("confidence", 0)),
                    ", ".join(lead.get("needs", [])),
                    lead.get("url", ""),
                    lead.get("qualified_at", ""),
                    lead.get("source", "")
                ]
                rows.append(row)
            
            # Check if sheet exists and clear it
            self._ensure_sheet_exists(sheet_name)
            
            # Upload data
            body = {
                'values': rows
            }
            
            result = self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=f"{sheet_name}!A1",
                valueInputOption="RAW",
                body=body
            ).execute()
            
            logger.info(f"✓ {len(leads)} leads uploaded to Google Sheets")
            logger.info(f"  Updated {result.get('updatedCells')} cells")
            
            return True
        
        except Exception as e:
            logger.error(f"Error uploading to Google Sheets: {e}")
            return False
    
    def _ensure_sheet_exists(self, sheet_name: str):
        """Ensure the sheet exists, create if it doesn't."""
        try:
            sheet_metadata = self.service.spreadsheets().get(
                spreadsheetId=self.spreadsheet_id
            ).execute()
            
            sheets = sheet_metadata.get('sheets', [])
            sheet_exists = any(sheet['properties']['title'] == sheet_name for sheet in sheets)
            
            if not sheet_exists:
                request = {
                    'addSheet': {
                        'properties': {
                            'title': sheet_name
                        }
                    }
                }
                self.service.spreadsheets().batchUpdate(
                    spreadsheetId=self.spreadsheet_id,
                    body={'requests': [request]}
                ).execute()
                logger.info(f"Created new sheet: {sheet_name}")
        
        except Exception as e:
            logger.warning(f"Could not ensure sheet exists: {e}")
    
    def append_leads(self, leads: List[Dict], sheet_name: str = "Qualified Leads") -> bool:
        """
        Append new leads to existing sheet (without overwriting).
        
        Args:
            leads: List of qualified leads to append
            sheet_name: Sheet to append to
        
        Returns:
            True if successful
        """
        if not self.service or not leads:
            return False
        
        try:
            # Prepare data rows (without headers)
            rows = []
            for lead in leads:
                row = [
                    lead.get("id", ""),
                    lead.get("title", ""),
                    lead.get("author", ""),
                    lead.get("contact_info", ""),
                    lead.get("lead_type", ""),
                    str(lead.get("confidence", 0)),
                    ", ".join(lead.get("needs", [])),
                    lead.get("url", ""),
                    lead.get("qualified_at", ""),
                    lead.get("source", "")
                ]
                rows.append(row)
            
            body = {
                'values': rows
            }
            
            result = self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=f"{sheet_name}!A2",
                valueInputOption="RAW",
                body=body
            ).execute()
            
            logger.info(f"✓ {len(leads)} leads appended to Google Sheets")
            
            return True
        
        except Exception as e:
            logger.error(f"Error appending to Google Sheets: {e}")
            return False


def main():
    """Test the sheets uploader."""
    uploader = SheetsUploader()
    
    test_leads = [
        {
            "id": "test1",
            "title": "Need help with visa",
            "author": "john_doe",
            "contact_info": "john@example.com",
            "lead_type": "work_visa",
            "confidence": 0.95,
            "needs": ["visa_guidance", "job_search"],
            "url": "https://reddit.com/...",
            "qualified_at": "2024-01-15T10:30:00",
            "source": "reddit"
        }
    ]
    
    if uploader.service:
        success = uploader.upload_leads(test_leads)
        print(f"\n📊 Upload result: {'✓ Success' if success else '✗ Failed'}")
    else:
        print("✗ Google Sheets API not initialized")


if __name__ == "__main__":
    from src.config_loader import setup_logging
    setup_logging()
    main()
