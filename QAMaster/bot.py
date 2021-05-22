from discord.ext import commands
from settings import BOT_TOKEN,PREFIX

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}!')
    print(f'with prefix: {PREFIX}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

bot.load_extension('cogs.judge')
bot.run(BOT_TOKEN)