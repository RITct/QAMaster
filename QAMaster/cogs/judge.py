"""
Cog to judge if a question is asked in the right channel
"""

from discord.ext import commands
import discord

class Judge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message: discord.Message):
        """captures all inputs"""
        if message.author == self.bot.user:
            return
        pass

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        await ctx.send('Hello {0.name}~'.format(member))

def setup(bot):
    bot.add_cog(Judge(bot))