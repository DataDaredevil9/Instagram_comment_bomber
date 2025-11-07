#!/usr/bin/env python3
"""
Instagram Comment Automation Script

WARNING: This script violates Instagram's Terms of Service.
Use at your own risk. Accounts may be banned or restricted.
This is for educational purposes only.
"""

import random
import time
import string
import re
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, PleaseWaitFewMinutes, ChallengeRequired
import sys
from typing import List, Optional


class InstagramCommentBomber:
    def __init__(self):
        self.clients: List[Client] = []
        self.comment_text: Optional[str] = None
        
    def generate_random_username(self) -> str:
        """Generate a random username for testing purposes"""
        adjectives = ['cool', 'awesome', 'amazing', 'epic', 'rad', 'swift', 'bright', 'bold']
        nouns = ['user', 'star', 'hero', 'ninja', 'warrior', 'champion', 'legend', 'master']
        numbers = ''.join(random.choices(string.digits, k=4))
        return f"{random.choice(adjectives)}_{random.choice(nouns)}_{numbers}"
    
    def create_test_accounts(self, num_accounts: int = 5) -> List[dict]:
        """
        Generate test account credentials.
        NOTE: These are just placeholders. In reality, you would need to:
        1. Actually create Instagram accounts (which violates ToS)
        2. Or use existing accounts you control
        """
        accounts = []
        for i in range(num_accounts):
            username = self.generate_random_username()
            # In a real scenario, you'd need actual passwords
            # This is just a template
            accounts.append({
                'username': username,
                'password': f"TempPass{random.randint(1000, 9999)}"
            })
        return accounts
    
    def login_account(self, username: str, password: str) -> Optional[Client]:
        """Attempt to login to an Instagram account"""
        try:
            cl = Client()
            cl.login(username, password)
            print(f"✓ Successfully logged in as {username}")
            return cl
        except LoginRequired:
            print(f"✗ Login failed for {username}: Authentication required")
            return None
        except ChallengeRequired:
            print(f"✗ Login failed for {username}: Challenge required (2FA/verification)")
            return None
        except PleaseWaitFewMinutes:
            print(f"✗ Login failed for {username}: Rate limited, please wait")
            return None
        except Exception as e:
            print(f"✗ Login failed for {username}: {str(e)}")
            return None
    
    def extract_shortcode_from_url(self, url: str) -> Optional[str]:
        """Extract shortcode from Instagram post URL"""
        # Remove trailing slash if present
        url = url.rstrip('/')
        
        # Patterns for different Instagram URL formats:
        # https://www.instagram.com/p/SHORTCODE/
        # https://www.instagram.com/reel/SHORTCODE/
        # https://instagram.com/p/SHORTCODE/
        patterns = [
            r'instagram\.com/p/([A-Za-z0-9_-]+)',
            r'instagram\.com/reel/([A-Za-z0-9_-]+)',
            r'instagram\.com/tv/([A-Za-z0-9_-]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def get_media_id_from_url(self, client: Client, url: str) -> Optional[str]:
        """Get media ID from Instagram post URL"""
        try:
            shortcode = self.extract_shortcode_from_url(url)
            if not shortcode:
                print(f"✗ Could not extract shortcode from URL: {url}")
                return None
            
            print(f"✓ Extracted shortcode: {shortcode}")
            
            # Get media ID from shortcode using instagrapi
            # Method 1: Try using media_pk_from_code if available
            try:
                if hasattr(client, 'media_pk_from_code'):
                    media_id = client.media_pk_from_code(shortcode)
                    print(f"✓ Got media ID: {media_id}")
                    return str(media_id)
            except Exception as e1:
                print(f"  media_pk_from_code failed: {str(e1)}")
            
            # Method 2: Use media_info to get the media and extract its PK
            try:
                print(f"  Fetching media info from shortcode...")
                media_info = client.media_info(shortcode)
                # Try pk attribute first
                if hasattr(media_info, 'pk'):
                    media_id = str(media_info.pk)
                    print(f"✓ Got media ID: {media_id}")
                    return media_id
                # Try id attribute as fallback
                elif hasattr(media_info, 'id'):
                    media_id = str(media_info.id)
                    print(f"✓ Got media ID (via id attribute): {media_id}")
                    return media_id
                else:
                    print(f"✗ Media info object doesn't have pk or id attribute")
                    return None
            except Exception as e2:
                print(f"✗ Error getting media info: {str(e2)}")
                return None
        except Exception as e:
            print(f"✗ Error getting media ID from URL: {str(e)}")
            return None
    
    def post_comment(self, client: Client, media_id: str, comment: str) -> bool:
        """Post a comment on a media (accepts media ID or shortcode)"""
        try:
            # Try posting with the provided ID/shortcode
            client.media_comment(media_id, comment)
            print(f"✓ Comment posted successfully")
            return True
        except PleaseWaitFewMinutes:
            print(f"✗ Rate limited, waiting before retry...")
            time.sleep(60)
            return False
        except Exception as e:
            # If it fails and media_id looks like a shortcode, try converting it
            error_msg = str(e).lower()
            if 'must been contain digits' in error_msg or 'shortcode' in error_msg:
                print(f"  Attempting to convert shortcode to media ID...")
                try:
                    # Try to get media info and use its PK
                    media_info = client.media_info(media_id)
                    actual_media_id = str(media_info.pk)
                    client.media_comment(actual_media_id, comment)
                    print(f"✓ Comment posted successfully (after conversion)")
                    return True
                except Exception as e2:
                    print(f"✗ Error posting comment after conversion: {str(e2)}")
                    return False
            else:
                print(f"✗ Error posting comment: {str(e)}")
                return False
    
    def run_bombing(self, post_url: str, comment_text: str, 
                   num_accounts: int = 5, comments_per_account: int = 1,
                   delay_between_comments: int = 5, account_credentials: List[dict] = None):
        """
        Main function to execute the comment bombing
        
        Args:
            post_url: Instagram post URL to target
            comment_text: Comment text to post
            num_accounts: Number of accounts to use
            comments_per_account: Number of comments per account
            delay_between_comments: Delay in seconds between comments
            account_credentials: List of dicts with 'username' and 'password' keys
        """
        print("=" * 60)
        print("INSTAGRAM COMMENT AUTOMATION SCRIPT")
        print("=" * 60)
        print("\n⚠️  WARNING: This violates Instagram's Terms of Service!")
        print("⚠️  Use at your own risk. Accounts may be banned.\n")
        
        self.comment_text = comment_text
        
        # Use provided credentials or generate placeholders
        if account_credentials:
            accounts = account_credentials
            print(f"Using {len(accounts)} provided account(s)...")
        else:
            print(f"Generating {num_accounts} test account credentials (placeholders)...")
            accounts = self.create_test_accounts(num_accounts)
            print("\n⚠️  NOTE: These are placeholder credentials!")
            print("⚠️  You need to provide real account credentials to use this script.")
            print("⚠️  See README.md for instructions.\n")
            return
        
        # Login to accounts
        print("\nLogging in to accounts...")
        for acc in accounts:
            if 'username' not in acc or 'password' not in acc:
                print(f"✗ Invalid account format: {acc}")
                continue
            client = self.login_account(acc['username'], acc['password'])
            if client:
                self.clients.append(client)
                time.sleep(random.uniform(2, 5))  # Random delay between logins
        
        if not self.clients:
            print("✗ No accounts successfully logged in. Exiting.")
            return
        
        print(f"\n✓ Successfully logged in to {len(self.clients)} account(s)")
        
        # Get media ID from post URL
        print(f"\nExtracting media ID from post URL...")
        print(f"URL: {post_url}")
        sample_client = self.clients[0]
        target_media_id = self.get_media_id_from_url(sample_client, post_url)
        
        if not target_media_id:
            print("✗ Could not get media ID from URL. Exiting.")
            return
        
        print(f"✓ Found target media ID: {target_media_id}")
        
        # Post comments
        print(f"\nStarting comment bombing...")
        print(f"Target Post URL: {post_url}")
        print(f"Comment: {comment_text}")
        print(f"Accounts: {len(self.clients)}")
        print(f"Comments per account: {comments_per_account}")
        print("-" * 60)
        
        total_comments = 0
        for account_num, client in enumerate(self.clients, 1):
            print(f"\nAccount {account_num}/{len(self.clients)}")
            for comment_num in range(comments_per_account):
                success = self.post_comment(client, target_media_id, comment_text)
                if success:
                    total_comments += 1
                
                # Delay between comments
                if comment_num < comments_per_account - 1:
                    delay = delay_between_comments + random.uniform(-1, 1)
                    print(f"  Waiting {delay:.1f} seconds before next comment...")
                    time.sleep(delay)
            
            # Longer delay between accounts
            if account_num < len(self.clients):
                account_delay = delay_between_comments * 2 + random.uniform(0, 5)
                print(f"  Waiting {account_delay:.1f} seconds before next account...")
                time.sleep(account_delay)
        
        print("\n" + "=" * 60)
        print(f"Comment bombing completed!")
        print(f"Total comments posted: {total_comments}")
        print("=" * 60)


def main():
    """Main entry point"""
    print("\n" + "=" * 60)
    print("Instagram Comment Automation")
    print("=" * 60)
    print("\n⚠️  WARNING: This script is for educational purposes only!")
    print("⚠️  Using this may violate Instagram's Terms of Service!")
    print("⚠️  Accounts may be banned or restricted!\n")
    
    # Get user input
    try:
        post_url = input("Enter Instagram post URL: ").strip()
        if not post_url:
            print("✗ Post URL cannot be empty!")
            return
        
        # Validate URL format
        if 'instagram.com' not in post_url.lower():
            print("✗ Invalid Instagram URL! Please enter a valid Instagram post URL.")
            print("   Example: https://www.instagram.com/p/ABC123xyz/")
            return
        
        comment_text = input("Enter comment text: ").strip()
        if not comment_text:
            print("✗ Comment text cannot be empty!")
            return
        
        num_accounts = input("Number of accounts to use (default: 5): ").strip()
        num_accounts = int(num_accounts) if num_accounts.isdigit() else 5
        
        comments_per_account = input("Comments per account (default: 1): ").strip()
        comments_per_account = int(comments_per_account) if comments_per_account.isdigit() else 1
        
        print("\n" + "=" * 60)
        print("Configuration:")
        print(f"  Target Post URL: {post_url}")
        print(f"  Comment: {comment_text}")
        print(f"  Accounts: {num_accounts}")
        print(f"  Comments per account: {comments_per_account}")
        print("=" * 60)
        
        # Ask for account credentials
        print("\n" + "=" * 60)
        print("ACCOUNT CREDENTIALS REQUIRED")
        print("=" * 60)
        print("You need to provide Instagram account credentials.")
        print("Format: username:password (one per line)")
        print("Enter 'done' when finished, or 'skip' to use placeholder accounts")
        print("=" * 60 + "\n")
        
        account_credentials = []
        while True:
            cred_input = input("Enter credentials (username:password) or 'done'/'skip': ").strip()
            if cred_input.lower() == 'done':
                break
            if cred_input.lower() == 'skip':
                account_credentials = None
                break
            if ':' in cred_input:
                username, password = cred_input.split(':', 1)
                account_credentials.append({
                    'username': username.strip(),
                    'password': password.strip()
                })
                print(f"✓ Added account: {username.strip()}")
            else:
                print("✗ Invalid format. Use username:password")
        
        confirm = input("\n⚠️  Continue? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Cancelled.")
            return
        
        # Initialize and run
        bomber = InstagramCommentBomber()
        bomber.run_bombing(
            post_url=post_url,
            comment_text=comment_text,
            num_accounts=num_accounts,
            comments_per_account=comments_per_account,
            delay_between_comments=5,
            account_credentials=account_credentials
        )
        
    except KeyboardInterrupt:
        print("\n\n✗ Interrupted by user. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

