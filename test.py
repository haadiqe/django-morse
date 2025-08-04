import asyncio

#چاپ عدد 1 تا 5 با تاخیر یک ثانیه ای

async def counter(num):
    for n in range(1,num+1):
        await asyncio.sleep(1)
        print(n)

async def main():
    await asyncio.gather(counter(5))
asyncio.run(main())


# چاپ سه پیام در فاصله زمانی مختلف

async def message():
    print ("is typing...")
    await asyncio.sleep(1)
    print ("hello!")
    await asyncio.sleep(1)
    print ("is typing...")
    await asyncio.sleep(3)
    print ("This is haadiqe.")

async def main():
    await asyncio.gather(message())

asyncio.run(main())


# جمع سه عدد

async def sum(a,b,c):
    await asyncio.sleep(2)
    print (f"Result : {a}+{b}+{c}={a+b+c}")

async def main(a,b,c):
    await asyncio.gather(sum(a,b,c))

asyncio.run(main(12,2,3))