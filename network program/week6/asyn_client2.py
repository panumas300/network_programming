from http import client
from sockettio import AsyncCleint
import asyncio
from json import dumps
from aioconsole import ainput

if __name__ == '__main__':
# ------------------------------------------=------------------------------=------------------
#-------------------------------------------=------------------------------=------------------

    IpAddress = '127.0.0.1' # Change Ip Address

    PORT = '8080'

    clientName = 'Iron Man'

    roomName = 'Marvel'

    messageToSend = ''

#-------------------------------------------=------------------------------=------------------
#-------------------------------------------=------------------------------=------------------

    sio = AsyncClient() 
    FullIp = 'http://'+IpAddress+':'+PORT

    @sio.event
    async def connect():
        print('Connected to server')
        await sio.emit('join_chat', {'room': roomName,'name': clientName})

    @sio.event
    async def get_message(message):
        if clientName == message['from']:
            print('You : ' + message['message'])
        else:
            print(message['from']+' : '+message['message'])
    
    async def send_message():
        while True:
            await asyncio.sleep(0.01)
            messageToSend = await ainput()
            await sio.emit('send_chat_room', {'message','name': clientName, 'room': roomName})

    async def connectToServer():
        await sio.connect(FullIp)
        await sio.wait()

    async def main(IpAddress):
        await asyncio.gather(
            connectToServer(),
            send_message()
        )
    
    loop = asyncio.get_event_loop()
    loop.run.until_complete(main(FullIp))