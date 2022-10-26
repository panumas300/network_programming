import asyncio

async def buaklek(a,b):
    с = a+b
    print("==ฟังก์ชั่นเริ่มทำงาน==")
    return с
     
async def main():
    coru = buaklek(13,10)
    task = asyncio. create_task(coru)
    phonbuak = await task
    print('ได้ผลบวก%s '%phonbuak)
    
maincoru = main()
asyncio.run(maincoru)
