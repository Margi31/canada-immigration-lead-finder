"""Reddit scraper for finding immigration-related posts and comments."""
import praw
import logging
from datetime import datetime, timedelta
from typing import List, Dict
from src.config_loader import Config

logger = logging.getLogger(__name__)


class RedditScraper:
    """Scrapes Reddit for immigration-related posts and comments."""
    
    def __init__(self):
        """Initialize Reddit API connection."""
        try:
            self.reddit = praw.Reddit(
                client_id=Config.REDDIT_CLIENT_ID,
                client_secret=Config.REDDIT_CLIENT_SECRET,
                user_agent=Config.REDDIT_USER_AGENT
            )
            logger.info("✓ Reddit API connection established")
        except Exception as e:
            logger.error(f"Failed to initialize Reddit API: {e}")
            raise
    
    def get_posts(self, subreddit_name: str, limit: int = 50, time_filter: str = "week") -> List[Dict]:
        """
        Get posts from a specific subreddit.
        
        Args:
            subreddit_name: Name of the subreddit to scrape
            limit: Maximum number of posts to retrieve
            time_filter: Time filter ('day', 'week', 'month', 'all')
        
        Returns:
            List of post dictionaries with metadata
        """
        posts = []
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            
            for post in subreddit.new(limit=limit):
                # Filter by keywords
                if not self._contains_keywords(post.title + " " + post.selftext):
                    continue
                
                post_data = {
                    "id": post.id,
                    "title": post.title,
                    "content": post.selftext,
                    "author": str(post.author),
                    "created_utc": post.created_utc,
                    "score": post.score,
                    "num_comments": post.num_comments,
                    "url": f"https://reddit.com{post.permalink}",
                    "source": "reddit"
                }
                posts.append(post_data)
            
            logger.info(f"Found {len(posts)} relevant posts in r/{subreddit_name}")
        
        except Exception as e:
            logger.error(f"Error scraping r/{subreddit_name}: {e}")
        
        return posts
    
    def get_comments(self, post_id: str, limit: int = 100) -> List[Dict]:
        """
        Get comments from a specific post.
        
        Args:
            post_id: Reddit post ID
            limit: Maximum number of comments to retrieve
        
        Returns:
            List of comment dictionaries
        """
        comments = []
        try:
            submission = self.reddit.submission(id=post_id)
            submission.comments.replace_more(limit=None)
            
            for comment in submission.comments.list()[:limit]:
                if not self._contains_keywords(comment.body):
                    continue
                
                comment_data = {
                    "id": comment.id,
                    "author": str(comment.author),
                    "content": comment.body,
                    "created_utc": comment.created_utc,
                    "score": comment.score,
                    "post_id": post_id,
                    "source": "reddit_comment"
                }
                comments.append(comment_data)
        
        except Exception as e:
            logger.error(f"Error getting comments from post {post_id}: {e}")
        
        return comments
    
    def _contains_keywords(self, text: str) -> bool:
        """Check if text contains any relevant keywords."""
        text_lower = text.lower()
        return any(keyword.lower() in text_lower for keyword in Config.KEYWORDS)
    
    def scrape_all_subreddits(self, limit: int = 50) -> List[Dict]:
        """
        Scrape all configured subreddits.
        
        Args:
            limit: Maximum number of posts per subreddit
        
        Returns:
            Combined list of all posts from all subreddits
        """
        all_posts = []
        
        for subreddit in Config.SUBREDDITS:
            logger.info(f"Scraping r/{subreddit}...")
            posts = self.get_posts(subreddit, limit=limit)
            all_posts.extend(posts)
        
        logger.info(f"✓ Total posts scraped: {len(all_posts)}")
        return all_posts


def main():
    """Main function for testing the scraper."""
    scraper = RedditScraper()
    posts = scraper.scrape_all_subreddits(limit=10)
    
    for post in posts[:5]:
        print(f"\n📝 {post['title']}")
        print(f"   Author: {post['author']}")
        print(f"   Score: {post['score']}")
        print(f"   URL: {post['url']}")


if __name__ == "__main__":
    from src.config_loader import setup_logging
    setup_logging()
    main()
