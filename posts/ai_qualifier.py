"""AI-powered lead qualification using Claude."""
import logging
from typing import List, Dict
from anthropic import Anthropic
from src.config_loader import Config

logger = logging.getLogger(__name__)


class AIQualifier:
    """Qualifies leads using Claude AI."""
    
    def __init__(self):
        """Initialize Claude API client."""
        self.client = Anthropic()
        self.model = "claude-3-5-sonnet-20241022"
        logger.info("✓ Claude AI client initialized")
    
    def qualify_lead(self, post_data: Dict) -> Dict:
        """
        Qualify a single lead using Claude.
        
        Args:
            post_data: Post/comment data to qualify
        
        Returns:
            Dictionary with qualification results
        """
        prompt = self._build_qualification_prompt(post_data)
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=500,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            response_text = message.content[0].text
            qualification = self._parse_response(response_text, post_data)
            
            return qualification
        
        except Exception as e:
            logger.error(f"Error qualifying lead: {e}")
            return {
                "is_qualified": False,
                "confidence": 0.0,
                "reason": f"Error during qualification: {str(e)}",
                "contact_info": None,
                "lead_type": None
            }
    
    def qualify_batch(self, posts: List[Dict], batch_size: int = 10) -> List[Dict]:
        """
        Qualify multiple leads in batches.
        
        Args:
            posts: List of posts to qualify
            batch_size: Number of leads to process at once
        
        Returns:
            List of qualified leads
        """
        qualified_leads = []
        
        for i, post in enumerate(posts):
            logger.info(f"Qualifying lead {i+1}/{len(posts)}...")
            qualification = self.qualify_lead(post)
            
            if qualification.get("is_qualified"):
                lead = {
                    **post,
                    **qualification,
                    "qualified_at": self._get_timestamp()
                }
                qualified_leads.append(lead)
            
            # Add delay to respect API rate limits
            if (i + 1) % batch_size == 0:
                logger.info(f"Processed {i+1} leads, taking a short break...")
        
        logger.info(f"✓ Qualification complete. {len(qualified_leads)} qualified leads found.")
        return qualified_leads
    
    def _build_qualification_prompt(self, post_data: Dict) -> str:
        """Build qualification prompt for Claude."""
        content = post_data.get("content", "")[:1000]  # Limit content length
        title = post_data.get("title", "")
        
        prompt = f"""You are an expert immigration consultant. Analyze this Reddit post/comment about Canadian immigration and determine if the author is a qualified lead for immigration services.

CONTENT TO ANALYZE:
Title: {title}
Body: {content}
Author: {post_data.get('author', 'Unknown')}

QUALIFICATION CRITERIA:
1. Is the person seeking immigration information for Canada?
2. Do they have a specific question or need (not just general discussion)?
3. Are they likely to be interested in professional services?
4. Can you identify any contact information (email, phone)?

RESPOND WITH JSON (no markdown, just plain JSON):
{{
    "is_qualified": true/false,
    "confidence": 0.0-1.0,
    "reason": "brief explanation",
    "lead_type": "job_seeker|student|entrepreneur|family_sponsorship|general_inquiry",
    "contact_info": "email or phone if visible, else null",
    "needs": ["list", "of", "identified", "needs"]
}}

Only return the JSON, no additional text."""
        
        return prompt
    
    def _parse_response(self, response: str, post_data: Dict) -> Dict:
        """Parse Claude's response."""
        import json
        
        try:
            # Try to extract JSON from the response
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1
            
            if start_idx == -1 or end_idx <= start_idx:
                return {
                    "is_qualified": False,
                    "confidence": 0.0,
                    "reason": "Could not parse response",
                    "contact_info": None,
                    "lead_type": None
                }
            
            json_str = response[start_idx:end_idx]
            parsed = json.loads(json_str)
            
            return {
                "is_qualified": parsed.get("is_qualified", False),
                "confidence": parsed.get("confidence", 0.0),
                "reason": parsed.get("reason", ""),
                "contact_info": parsed.get("contact_info"),
                "lead_type": parsed.get("lead_type"),
                "needs": parsed.get("needs", [])
            }
        
        except json.JSONDecodeError:
            logger.warning(f"Failed to parse Claude response as JSON")
            return {
                "is_qualified": False,
                "confidence": 0.0,
                "reason": "JSON parsing error",
                "contact_info": None,
                "lead_type": None
            }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()


def main():
    """Test the AI qualifier."""
    qualifier = AIQualifier()
    
    test_post = {
        "title": "Moving to Canada for work",
        "content": "Hi everyone! I'm a software engineer from India with 5 years of experience. I've been offered a job in Toronto. What visa do I need? Email: john@example.com",
        "author": "john_doe",
        "url": "https://reddit.com/r/canadaimmigration/..."
    }
    
    result = qualifier.qualify_lead(test_post)
    print("\n📊 Qualification Result:")
    for key, value in result.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    from src.config_loader import setup_logging
    setup_logging()
    main()
