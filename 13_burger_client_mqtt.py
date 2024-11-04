import httpx
import asyncio
import time

async def make_order(path: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://localhost:8000{path}')
        print(response.json())

async def main():
    t0 = time.time()
    # Lista de pedidos de bebidas
    orders = [
        "/order/drinks/coke",
        "/order/drinks/water",
        "/order/drinks/lemonade",
        "/order/burgers/1",
        "/order/burgers/2",
        "/order/burgers/4",
    ]
    # Ejecutar todas las órdenes en paralelo
    tasks = [make_order(order) for order in orders]
    await asyncio.gather(*tasks)
    print(f"Orders took {time.time()-t0:.2f} seconds")

if __name__ == '__main__':
    asyncio.run(main())