import discord
import random
from datetime import datetime
from pytz import timezone
import pytz

TOKEN = []

client = discord.Client()

#timezones
utc = pytz.utc
tz_PT = pytz.timezone('US/Pacific')
datetime_PT = datetime.now(tz_PT)

tz_MT = pytz.timezone('US/Mountain')
datetime_MT = datetime.now(tz_MT)

tz_CT = pytz.timezone('US/Central')
datetime_CT = datetime.now(tz_CT)

tz_ET = pytz.timezone('US/Eastern')
datetime_ET = datetime.now(tz_ET)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    #prevents bot from responding to itself
    if message.author == client.user:
        return
    
    #commands that only work in specified channel
    if message.channel.name == 'project-testspace':
        if user_message.lower() == '!teamcall':
            await message.channel.send(f'TOHOGA F**** YEAH')
            return

    #time commands
    if user_message.lower() == '!pacific':
        response = f'Pacific time: {datetime_PT.strftime("%H:%M:%S")}'
        await message.channel.send(response)
        return
    elif user_message.lower() == '!mountain':
        response = f'Mountain time: {datetime_MT.strftime("%H:%M:%S")}'
        await message.channel.send(response)
        return
    elif user_message.lower() == '!central':
        response = f'Central time: {datetime_CT.strftime("%H:%M:%S")}'
        await message.channel.send(response)
        return
    elif user_message.lower() == '!eastern':
        response = f'Eastern time: {datetime_ET.strftime("%H:%M:%S")}'
        await message.channel.send(response)
        return
    elif user_message.lower() == '!time':
        response = f'Current local time: {datetime.now().strftime("%H:%M:%S")}'
        await message.channel.send(response)
        return

    #more global commands
    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}!')
        return
    elif user_message.lower() == 'bye':
        await message.channel.send(f'See you later {username}!')
        return
    elif user_message.lower() == '!random':
        response = f'This is your random number: {random.randrange(100000)}'
        await message.channel.send(response)
        return


client.run(TOKEN)
