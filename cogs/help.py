import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
                    color = ctx.author.colour,
                    title="Help",
                    description="For more info about a command use `.help command`",
                )
        admin = """`Kick` `Ban` `Unban` `addrole` `remrole` `poll` `pollresults`"""
        games = """`8ball`"""
        Other = """`Ping`"""
        em.add_field(name="Mods:", value=admin, inline=False)
        em.add_field(name="Games:", value=games, inline=False)
        em.add_field(name="Other:", value=Other, inline=False)
        await ctx.send(embed = em)
    @help.command()
    async def pollresults(self, ctx):
      em = discord.Embed(
                    title="Poll Results",
                    description="Creates a Poll",
                )
      em.add_field(name="**Syntax**", value=".pollresults <pollid>")
      em.set_footer(text="This will close the Poll related (the message will still be avaible but you can no longer vote)")
      await ctx.send(embed = em)

    @help.command()
    async def poll(self, ctx):
        em = discord.Embed(
                    title="Poll",
                    description="Creates a Poll",
                )
        em.add_field(name="Important", value="Make sure to save the poll id, you will need it to get your poll results", inline=False)
        em.add_field(name="**Syntax**", value=".poll \"<question>\" \"<option1>\" \"<option2>\" ...", inline=False)
        em.set_footer(text="you need to include the \"\" while adding question and options")
        await ctx.send(embed = em)

    @help.command()
    async def ping(self, ctx):
        em = discord.Embed(
                    title="ping",
                )
        em.add_field(name="**Syntax**", value=".ping")
        await ctx.send(embed = em)

    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(
                    title="Kick",
                    description="Kicks a member from the guild",
                )
        em.add_field(name="**Syntax**", value=".kick <member> [reason]")
        await ctx.send(embed = em)

    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(
                    title="Ban",
                    description="Ban a member from the guild",
                )
        em.add_field(name="**Syntax**", value=".ban <member> [reason] \"delete member messages(days)\"")
        await ctx.send(embed = em)

    @help.command()
    async def unban(self, ctx):
        em = discord.Embed(
                    title="Unban",
                    description="Unban a member from the guild",
                )
        em.add_field(name="**Syntax**", value=".Unban <member> [reason]")
        await ctx.send(embed = em)

    @help.command()
    async def clear(self, ctx):
        em = discord.Embed(
                    title="Clear",
                    description="Clear messages",
                )
        em.add_field(name="**Syntax**", value=".clear <amount>")
        await ctx.send(embed = em)

    @help.command()
    async def addrole(self, ctx):
        em = discord.Embed(
                    title="Addrole",
                    description="Add role to user",
                )
        em.add_field(name="**Syntax**", value=".addrole <role> <user>")
        em.set_footer(text="Capital words do matter in <role>")
        await ctx.send(embed = em)

    @help.command()
    async def remrole(self, ctx):
        em = discord.Embed(
                    title="remrole",
                    description="Remove a role from user",
                )
        em.add_field(name="**Syntax**", value=".remrole <role> <user>")
        em.set_footer(text="Capital words do matter in <role>")
        await ctx.send(embed = em)

    @help.command(aliases=['8ball'])
    async def _8ball(self, ctx):
        em = discord.Embed(
                    title="8ball",
                    description="Play 8ball",
                )
        em.add_field(name="**Syntax**", value=".8ball <a question>")
        await ctx.send(embed = em)

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
        # if isinstance(error):
        #     await ctx.send(f'{error}. Check `.help` for more info')

def setup(bot):
    bot.add_cog(help(bot))