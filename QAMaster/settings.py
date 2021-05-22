import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "!"

# The bot token. Keep this secret!
if 'DISCORD_TOKEN' not in os.environ:
    raise Exception("Invalid token")
BOT_TOKEN = os.environ.get('DISCORD_TOKEN')

# bot prefix
PREFIX = '!'

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
