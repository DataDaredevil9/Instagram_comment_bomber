"""
Example configuration file for Instagram Comment Bomber

WARNING: Never commit this file with real credentials!
Copy this to config.py and add your actual credentials.
Add config.py to .gitignore
"""

# Example account credentials
# Format: List of dictionaries with 'username' and 'password' keys
ACCOUNTS = [
    {
        'username': 'your_account_1',
        'password': 'your_password_1'
    },
    {
        'username': 'your_account_2',
        'password': 'your_password_2'
    },
    # Add more accounts as needed
]

# Default settings
DEFAULT_SETTINGS = {
    'comments_per_account': 1,
    'delay_between_comments': 5,  # seconds
    'delay_between_accounts': 10,  # seconds
}

