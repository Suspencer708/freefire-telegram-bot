````markdown
# 🔥 Free Fire Telegram Bot

A powerful Telegram bot for checking Free Fire player statistics, profiles, and leaderboards.

## ✨ Features

- 📊 **Player Stats** - Get detailed player statistics (kills, wins, K/D ratio, etc.)
- 👤 **Player Profile** - View player information and guild details
- 🏆 **Leaderboards** - Check top players by region
- 🌍 **Multi-Region Support** - Support for multiple regions (PK, IN, BR, ID, TH, VN, etc.)
- ⚡ **Async/Await** - Fast and efficient API calls
- 🔐 **Secure** - Uses environment variables for sensitive data

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Telegram account and a bot token (from BotFather)
- Free Fire API key

### 1. Clone/Setup the Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/freefire-telegram-bot.git
cd freefire-telegram-bot

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your tokens
nano .env
```

**Edit `.env` with:**
```
TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather
FREEFIRE_API_KEY=your_api_key_from_hl_gaming
FREEFIRE_API_BASE_URL=https://api.hlgamingofficial.com/api
```

### 4. Get Your Tokens

#### Telegram Bot Token:
1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Follow the instructions to create a bot
4. Copy your bot token

#### Free Fire API Key:
1. Visit [HL Gaming Developer](https://hlgamingofficial.com/developer/api)
2. Register and create an API key
3. Copy the API key to your `.env` file

### 5. Run the Bot

```bash
python main.py
```

## 📖 Bot Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Show welcome message | `/start` |
| `/help` | Show all available commands | `/help` |
| `/stats <uid> [region]` | Get player statistics | `/stats 5351564274 pk` |
| `/profile <uid> [region]` | Get player profile | `/profile 12345678 in` |
| `/leaderboard [region]` | View top 10 players | `/leaderboard br` |

## 🌍 Supported Regions

- `pk` - Pakistan
- `in` - India
- `br` - Brazil
- `id` - Indonesia
- `th` - Thailand
- `vn` - Vietnam
- `us` - United States
- `eu` - Europe

## 📝 Example Usage

### Get Player Stats
```
User: /stats 5351564274 pk
Bot: 📊 Player Statistics
     Name: Example Player
     Level: 50
     K/D Ratio: 2.45
     ...
```

### Check Leaderboard
```
User: /leaderboard in
Bot: 🏆 Top 10 Players - IN
     1. Player Name - Level 60
        K/D: 3.20 | Wins: 150
     ...
```

## 📁 Project Structure

```
freefire-telegram-bot/
├── main.py              # Main bot application
├── freefire_api.py      # API client for Free Fire
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment file
├── .env                 # Your credentials (git ignored)
└── README.md           # This file
```

## 🔧 Configuration

Edit `config.py` to customize:
- Supported regions
- Rate limiting
- Feature toggles
- Log level
- Database settings

## 🚢 Deployment

### Using Heroku

1. Install Heroku CLI
2. Create a Procfile:
   ```
   worker: python main.py
   ```

3. Deploy:
   ```bash
   heroku create your-bot-name
   heroku config:set TELEGRAM_BOT_TOKEN=your_token
   heroku config:set FREEFIRE_API_KEY=your_key
   git push heroku main
   ```

### Using VPS/Server

```bash
# Install screen or tmux
sudo apt install screen

# Run bot in background
screen -S ffbot python main.py

# Detach with: Ctrl+A then D
# Reattach with: screen -r ffbot
```

## 🐛 Troubleshooting

### Bot not responding:
- Check if bot token is correct in `.env`
- Ensure bot is in the correct chat
- Check logs: `python main.py 2>&1 | tee bot.log`

### API errors:
- Verify API key is valid
- Check if Free Fire API is online
- Check rate limits (max 30 requests/min by default)

### Player not found:
- Verify player UID is correct
- Check if region is supported
- Try with a known valid player UID

## 📚 API Documentation

### Free Fire API (HL Gaming)
- [Official Docs](https://hlgamingofficial.com/developer/api)
- [Python Package](https://pypi.org/project/hl-gaming-official-ff-data/)

### Telegram Bot API
- [Official Docs](https://core.telegram.org/bots/api)
- [Python Telegram Bot](https://docs.python-telegram-bot.org/)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

This bot is unofficial and not affiliated with Garena or Free Fire. Use at your own risk. Ensure you comply with:
- Telegram's Terms of Service
- Free Fire's Terms of Service
- All applicable laws and regulations

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 💬 Support

For issues, questions, or suggestions:
1. Create an issue on GitHub
2. Check existing issues for solutions
3. Join our [Telegram community](https://t.me/yourbot)

## ���� Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [HL Gaming](https://hlgamingofficial.com/)
- [Garena Free Fire](https://www.freefiremobile.com/)

---

Made with ❤️ for Free Fire players
````
