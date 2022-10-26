import asyncio

async def hanlek(a,b):
    print('%s/%s'%(a,b))
    return a/b

loop = asyncio.get_event_loop() 
phonhan = loop.run_until_complete(hanlek(10,2)) 
print('ผลลัพธ์: %.3f '%phonhan)