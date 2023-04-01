import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        spy = True

        if message.author.bot:
            return False
        #if message.author.id == 1077084645100884038 // guild owner id
            #return await message.channel.send('Message not logged, its faint!') // message sent if author is owner
        if spy == False:
            if message.attachments:
                for attachments in message.attachments:
                    await message.channel.send(f'```Image Logged```\n >{message.author}\n >{attachments.url}\n')
                    print(f'image logged | {message.author}')
            else:
                await message.channel.send(f'```Message Logged```\n >{message.author}\n >{message.content}\n')
                print(f'message logged | {message.author}')
        else:
            logs = open('logs.txt','a')
            if message.attachments:
                for attachments in message.attachments:
                    logs.write(f'```Image Logged```\n >{message.author}\n >{attachments.url}\n')
                    print(f'image logged | {message.author}')
            else:
                logs.write(f'```Message Logged```\n >{message.author}\n >{message.content}\n')
                print(f'message logged | {message.author}')

intents = discord.Intents.all()

client = MyClient(
    intents=discord.Intents.all()
)

client.run('')
