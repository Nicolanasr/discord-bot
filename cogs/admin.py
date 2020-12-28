import discord
from discord.ext import commands
import datetime, time

def permissionCheck(author, rolename):
    rolesc = 0
    for role in author.roles:
        rolesc = rolesc + 1
        for role_name in rolename:
            if role.name == role_name:
                rolesc = -100
                return True
    if rolesc > 0:
        return False

def permissionCheckrole(author, role, member):
    for roleauth in author.roles:
      if role.position <= roleauth.position :
        for memrole in member.roles :
          if memrole.position <= roleauth.position:
            count = 100
          else:
            count = -100
      else:
        count = -100
    if count > 0:
      return True
    else:
      return False

class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def admincheck(self, ctx, member:discord.Member):
      await ctx.send("check")
      # if member.guild_permissions.administrator :
      #   await ctx.send("admin")
      # else:
      #   await ctx.send("nope")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, reason=None):
        await member.kick(reason=reason)
        if reason == None :
            await ctx.channel.purge(limit = 1)
            await ctx.send(f'{member.mention} was kicked')
        else:
            await ctx.channel.purge(limit = 1)
            await ctx.send(f'{member.mention} was kicked for the following reason:  \' {reason} \'')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, reason=None,  delete_message_days=1):
        await member.ban(reason=reason)
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'{member.mention} was Banned')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.purge(limit = 1)
                await ctx.send(f'{user.mention} Is now Unbanned')
                return
       

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit = amount)

    # @commands.command()
    # async def pm(self, ctx, member: discord.Member, msg):
    #     await ctx.send(member)
    #     await member.send(msg)

    @commands.command()
    async def rolepos(self, ctx, role:discord.Role):
        await ctx.send(f"{role.position} {ctx.author.roles}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, role: discord.Role, member:discord.Member):
        if(permissionCheckrole(ctx.author, role, member)):
          await member.add_roles(role)
          await ctx.send(f'Role {role.mention} added to {member.mention}')
        else:
          await ctx.send(f"{ctx.author.mention} You do not have permission to perform this action. Please check `.help yourcommand` for more info")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def remrole(self, ctx, role: discord.Role, member:discord.Member):
        if(permissionCheckrole(ctx.author, role, member)):
            await member.remove_roles(role)
            await ctx.send(f'Role {role.mention} Removed from {member.mention}')
        else:
            await ctx.send(f"{ctx.author.mention} You do not have permission to perform this action. Please check `.help yourcommand` for more info")
        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def poll(self, ctx, question, *, options):
        allowed = ["admin", 'moderator']
        if(permissionCheck(ctx.author, allowed)):
            options = options.split("\" ")
            if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
                reactions = ['✅', '❌']
            else:
                reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

            description = []
            x=0
            for option in options:
                description += '\n {} {}'.format(reactions[x], options[x].strip("\""))
                x=x+1
            description = ''.join(description)

            embed = discord.Embed(
                        title=":red_circle: **POLL** :red_circle: " ,
                        description="React with the corresponding emoji to vote",
                        colour=ctx.author.colour,
                        timestamp=datetime.datetime.now(),
            )

            embed.add_field(name="Question: ", value=question, inline=True)
            embed.add_field(name="Options: ", value=description, inline=False)
            message = await ctx.send(embed = embed)
            await message.pin()
            for reaction in reactions[:len(options)]:
                await message.add_reaction(reaction)
            
            new_embed = embed.set_footer(text='Poll ID: {} \nBy {}'.format(message.id, ctx.author))

            await message.edit(embed=new_embed)
            
        else:
            await ctx.send(f"{ctx.author.mention} You do not have permission to perform this action. Please check `.help yourcommand` for more info")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def pollresults(self, ctx, pollid):
      msg = await ctx.fetch_message(pollid)
      options = []
      for me in msg.embeds:
        quest_title = me.fields
        options.append(quest_title[1].value)

      options2 =[]
      for option in options:
        options2 = (option.split("\n"))

      description=[]
      embed = discord.Embed(
                        title = f"Polls result for `{quest_title[0].value}` ",
                        colour=ctx.author.colour,
                        )
      embed.set_footer(text=f"Original message id `{pollid}`")
      x=0
      for reaction in msg.reactions:
        if x < len(options2):
          description += '\n {} : {}'.format(options2[x], reaction.count)
        x=x+1
      description = ''.join(description)
      embed.add_field(name="Options    |    Votes", value=description, inline=False)
      await ctx.send(embed = embed)
      for reaction in msg.reactions:
        await msg.clear_reaction(reaction)
      await msg.unpin()




    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send(f'{error}. Check `.help yourcommand` for more info')
    #     if isinstance(error, commands.MemberNotFound):
    #         await ctx.send(f'{error}. Check `.help yourcommand` for more info')
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(f'{error}. Check `.help yourcommand` for more info')
        

def setup(bot):
    bot.add_cog(admin(bot))