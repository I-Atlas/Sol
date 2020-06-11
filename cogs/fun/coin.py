# Imports
import random
import discord
from discord.ext import commands


# Main Command Class
class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Flips a coin."
        self.usage = "coin"

    @commands.command(name='coin')
    @commands.has_permissions()
    async def coin(self, ctx):
        embed = discord.Embed(title=f"Try to toss the coin, heads or tails, you know.\n\nThat leaves you with a ``{random.choice(['heads', 'tails'])}``!", color=ctx.author.color)
        embed.set_author(name=" | Coin", icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
        return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Coin(bot))