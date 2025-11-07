# Instagram Comment Automation Script

⚠️ **WARNING: This script violates Instagram's Terms of Service. Use at your own risk. Accounts may be banned or restricted. This is for educational purposes only.**

## Description

This Python script automates commenting on Instagram posts from multiple accounts. It allows you to:
- Target a specific Instagram post by URL
- Post comments from multiple accounts
- Automate the entire process

## Features

- Interactive command-line interface
- Support for multiple accounts
- Automatic rate limiting and delays
- Error handling and retry logic
- Random delays to appear more natural

## Installation

1. **Install Python 3.7+** if you haven't already

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script:**
   ```bash
   python instagram_comment_bomber.py
   ```

2. **Follow the prompts:**
   - Enter the Instagram post URL (e.g., https://www.instagram.com/p/ABC123xyz/)
   - Enter the comment text you want to post
   - Specify number of accounts to use
   - Specify comments per account
   - Provide account credentials (username:password format)

**Supported URL formats:**
- `https://www.instagram.com/p/SHORTCODE/`
- `https://www.instagram.com/reel/SHORTCODE/`
- `https://www.instagram.com/tv/SHORTCODE/`

## Account Credentials

**IMPORTANT:** You need to provide actual Instagram account credentials. The script will prompt you to enter them in the format:
```
username:password
```

You can enter multiple accounts, one per line. Type 'done' when finished.

**Note:** 
- Using fake or automated accounts violates Instagram's Terms of Service
- Creating multiple accounts for automation purposes is against Instagram's policies
- Your accounts may be banned or restricted
- Use only accounts you own and control

## Configuration Options

- **Number of accounts**: How many different accounts to use
- **Comments per account**: How many comments each account should post
- **Delays**: Built-in delays between comments to avoid rate limiting

## Legal and Ethical Considerations

⚠️ **This script is provided for educational purposes only.**

- **Violates Terms of Service**: This script violates Instagram's Terms of Service
- **Account Bans**: Using this script may result in permanent account bans
- **Rate Limiting**: Instagram actively detects and blocks automated behavior
- **Legal Issues**: Mass commenting may be considered harassment or spam
- **Ethical Concerns**: Spamming comments is harmful to the community

## How It Works

1. The script logs into multiple Instagram accounts
2. Extracts the media ID from the provided post URL
3. Posts comments from each account with delays between them
4. Includes random delays to appear more natural

## Troubleshooting

### Login Issues
- Make sure your account credentials are correct
- Disable 2FA temporarily (not recommended) or handle challenges manually
- Instagram may require phone verification for new logins

### Rate Limiting
- Instagram has strict rate limits
- The script includes delays, but you may still get rate limited
- Wait longer between operations if you encounter rate limits

### Account Bans
- If accounts get banned, you'll need to create new ones (violates ToS)
- Use the script sparingly to reduce detection risk

## Disclaimer

This software is provided "as is" without warranty of any kind. The authors are not responsible for:
- Account bans or restrictions
- Legal consequences of using this script
- Any damage or loss resulting from use of this software

**Use at your own risk.**

## Alternative Approaches

Instead of using automation scripts, consider:
- Engaging authentically with content
- Building genuine relationships on the platform
- Following Instagram's community guidelines
- Using Instagram's official features and tools

