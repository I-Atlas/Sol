# Imports
import platform
import discord
from discord.ext import commands


# Main Command Class
class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that displays bot stats."
        self.usage = "stats"

    @commands.command(name='stats', aliases=['st'])
    @commands.has_permissions()
    async def stats(self, ctx):
        number_of_servers = str(len(self.bot.guilds))
        number_of_members = str(len(set(self.bot.get_all_members())))
        author_id = '<@271684584863825920>'

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', color=ctx.author.color)

        embed.add_field(name='Python version', value=platform.python_version(), inline=False)
        embed.add_field(name='discord.py version', value=discord.__version__, inline=False)
        embed.add_field(name='Total guilds', value=number_of_servers, inline=False)
        embed.add_field(name='Total users', value=number_of_members, inline=False)
        embed.add_field(name='Bot developers', value=author_id, inline=False)

        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
        embed.set_author(name=f" | Stats", icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Stats(bot))