import discord
from discord.ext import commands

class tts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def join(self, message):
        await message.channel.send('未実装です\nしばらくお待ちください')
def setup(bot):
    bot.add_cog(tts(bot))