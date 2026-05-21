"""
Free Fire Telegram Bot
Main bot application with command handlers
"""

import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from config import TELEGRAM_BOT_TOKEN
from freefire_api import FFAPIClient

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize API client
ff_api = FFAPIClient()


# Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    welcome_message = """
🔥 Welcome to Free Fire Stats Bot! 🔥

I can help you check player statistics and information.

📋 Available Commands:
/stats <player_id> - Get player statistics
/profile <player_id> - Get player profile info
/leaderboard <region> - View top players
/help - Show all commands

Example: /stats 5351564274

Start by sending a player ID to check stats!
    """
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
📚 Command Help:

/start - Show welcome message
/help - Show this help message
/stats <player_id> - Get full player statistics
/profile <player_id> - Get player profile
/leaderboard <region> - Top 10 players by region
    Regions: pk, in, br, id, th, vn, etc.

Example usage:
  /stats 5351564274
  /profile 12345678
  /leaderboard in

💡 Tips:
- Replace <player_id> with actual Free Fire UID
- Region codes: pk (Pakistan), in (India), br (Brazil), id (Indonesia)
    """
    await update.message.reply_text(help_text)


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /stats command"""
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a player ID.\nUsage: /stats <player_id>"
        )
        return

    player_id = context.args[0]
    region = context.args[1] if len(context.args) > 1 else "pk"

    await update.message.reply_text(f"🔄 Fetching stats for player {player_id}...")

    try:
        stats = await ff_api.get_player_stats(player_id, region)
        if stats:
            message = format_stats_message(stats)
            await update.message.reply_text(message, parse_mode="HTML")
        else:
            await update.message.reply_text(
                "❌ Player not found. Please check the player ID and region."
            )
    except Exception as e:
        logger.error(f"Error fetching stats: {e}")
        await update.message.reply_text(
            f"❌ Error fetching stats: {str(e)}\n\nMake sure you have a valid API key configured."
        )


async def profile_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /profile command"""
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a player ID.\nUsage: /profile <player_id>"
        )
        return

    player_id = context.args[0]
    region = context.args[1] if len(context.args) > 1 else "pk"

    await update.message.reply_text(f"🔄 Fetching profile for player {player_id}...")

    try:
        profile = await ff_api.get_player_profile(player_id, region)
        if profile:
            message = format_profile_message(profile)
            await update.message.reply_text(message, parse_mode="HTML")
        else:
            await update.message.reply_text(
                "❌ Player profile not found."
            )
    except Exception as e:
        logger.error(f"Error fetching profile: {e}")
        await update.message.reply_text(
            f"❌ Error fetching profile: {str(e)}"
        )


async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /leaderboard command"""
    region = context.args[0] if context.args else "pk"

    await update.message.reply_text(f"🔄 Fetching leaderboard for {region.upper()}...")

    try:
        leaderboard = await ff_api.get_leaderboard(region)
        if leaderboard:
            message = format_leaderboard_message(leaderboard, region)
            await update.message.reply_text(message, parse_mode="HTML")
        else:
            await update.message.reply_text(
                "❌ Could not fetch leaderboard."
            )
    except Exception as e:
        logger.error(f"Error fetching leaderboard: {e}")
        await update.message.reply_text(
            f"❌ Error: {str(e)}"
        )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo any text that's not a command"""
    await update.message.reply_text(
        "👋 I didn't understand that. Use /help to see available commands."
    )


# Message Formatting
def format_stats_message(stats: dict) -> str:
    """Format player stats for display"""
    try:
        return f"""
<b>📊 Player Statistics</b>

<b>Name:</b> {stats.get('nickname', 'N/A')}
<b>UID:</b> {stats.get('uid', 'N/A')}
<b>Level:</b> {stats.get('level', 'N/A')}
<b>Rank:</b> {stats.get('rank', 'N/A')}

<b>🎮 Game Stats:</b>
<b>Matches:</b> {stats.get('matches', 0)}
<b>Wins:</b> {stats.get('wins', 0)}
<b>Win Rate:</b> {stats.get('win_rate', 'N/A')}%
<b>Kills:</b> {stats.get('kills', 0)}
<b>K/D Ratio:</b> {stats.get('kd_ratio', 'N/A')}
<b>Headshots:</b> {stats.get('headshots', 0)}
<b>Top 10:</b> {stats.get('top10', 0)}
<b>Top 25:</b> {stats.get('top25', 0)}

<b>💰 Resources:</b>
<b>Gold:</b> {stats.get('gold', 0)}
<b>Diamonds:</b> {stats.get('diamonds', 0)}
        """
    except Exception as e:
        return f"Error formatting stats: {str(e)}"


def format_profile_message(profile: dict) -> str:
    """Format player profile for display"""
    try:
        return f"""
<b>👤 Player Profile</b>

<b>Name:</b> {profile.get('nickname', 'N/A')}
<b>UID:</b> {profile.get('uid', 'N/A')}
<b>Level:</b> {profile.get('level', 'N/A')}
<b>Rank:</b> {profile.get('rank', 'N/A')}
<b>Guild:</b> {profile.get('guild_name', 'No Guild')}

<b>Status:</b> {profile.get('status', 'Offline')}
<b>Last Login:</b> {profile.get('last_login', 'N/A')}
        """
    except Exception as e:
        return f"Error formatting profile: {str(e)}"


def format_leaderboard_message(leaderboard: list, region: str) -> str:
    """Format leaderboard for display"""
    try:
        message = f"<b>🏆 Top 10 Players - {region.upper()}</b>\n\n"
        for idx, player in enumerate(leaderboard[:10], 1):
            message += f"{idx}. <b>{player.get('nickname', 'N/A')}</b> - Level {player.get('level', 'N/A')}\n"
            message += f"   K/D: {player.get('kd_ratio', 'N/A')} | Wins: {player.get('wins', 0)}\n\n"
        return message
    except Exception as e:
        return f"Error formatting leaderboard: {str(e)}"


def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("profile", profile_command))
    application.add_handler(CommandHandler("leaderboard", leaderboard_command))

    # Handle all other messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot
    application.run_polling()


if __name__ == '__main__':
    logger.info("🚀 Starting Free Fire Telegram Bot...")
    main()
