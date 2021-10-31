import discord

token = ''
client = discord.Client()


'''
def community_report(guild):
    online = 0
    idle = 0
    offline = 0

    for m in guild.members:
        if str(m.status) == "online":
            online += 1
        if str(m.status) == "offline":
            offline += 1
        else:
            idle += 1

    return online, idle, offline

'''

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    print(f"Message is written by {message.author}\n In the server {message.guild}\n The message is {message.content}\n Written at time {message.created_at}\n \n")
    arjun_guild = client.get_guild(540544791730061334)
    try:
        if "hello" == message.content.lower():
            await message.channel.send('Hi!')

        elif "member_count" == message.content.lower():
            await message.channel.send(f"```{arjun_guild.member_count}```")

        elif "community_report" == message.content.lower():
            online = 0
            idle = 0
            offline = 0

            for m in arjun_guild.members:
                if str(m.status) == "online":
                    online += 1
                if str(m.status) == "offline":
                    offline += 1
                else:
                    idle += 1

            await message.channel.send(f"```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")

        elif "logout()" == message.content.lower():
            await client.close()

        elif 'show_avatar'==message.content.lower():
            await message.channel.send(discord.ClientUser.default_avatar_url)


    except Exception as e:
        print(e)


@client.event
async def on_member_join(message):
    await message.channel.send('Hi!')



client.run(token)
