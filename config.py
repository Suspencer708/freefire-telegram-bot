"""
Configuration file for Free Fire Telegram Bot
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv(
    'TELEGRAM_BOT_TOKEN',
    'YOUR_TELEGRAM_BOT_TOKEN_HERE'
)

# Free Fire API Configuration
FREEFIRE_API_KEY = os.getenv(
    'FREEFIRE_API_KEY',
    'YOUR_FREE_FIRE_API_KEY_HERE'
)

FREEFIRE_API_BASE_URL = os.getenv(
    'FREEFIRE_API_BASE_URL',
    'https://api.hlgamingofficial.com/api'  # Example: HL Gaming API
)

# Bot Configuration
BOT_NAME = "Free Fire Stats Bot"
BOT_VERSION = "1.0.0"
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Supported Regions
SUPPORTED_REGIONS = [
    'pk',  # Pakistan
    'in',  # India
    'br',  # Brazil
    'id',  # Indonesia
    'th',  # Thailand
    'vn',  # Vietnam
    'us',  # United States
    'eu',  # Europe
]

# API Rate Limiting (requests per minute)
RATE_LIMIT = int(os.getenv('RATE_LIMIT', '30'))

# Database Configuration (optional)
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'sqlite:///freefire_bot.db'
)

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Error Messages
MESSAGES = {
    'invalid_player_id': "❌ Invalid player ID format",
    'player_not_found': "❌ Player not found",
    'api_error': "❌ API Error",
    'rate_limit': "⏱️ Too many requests. Please wait a moment.",
    'invalid_region': "❌ Invalid region",
}

# Features
FEATURES = {
    'stats': True,
    'profile': True,
    'leaderboard': True,
    'match_history': False,  # Can be enabled if API supports it
    'guild_info': False,  # Can be enabled if API supports it
}
