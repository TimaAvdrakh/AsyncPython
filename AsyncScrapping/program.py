import requests
import bs4
from  colorama import Fore
import aiohttp
import asyncio


async def get_html(episode_number: int):
    print( Fore.YELLOW + f"Getting Html for episode {episode_number}", flush=True)

    url = f'http://talkpython.fm/{episode_number}'
    # resp = requests.get(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            return await resp.text()


def get_title(html, episode_number):
    print(Fore.CYAN + f"Totle for {episode_number},", flush=True)
    soup = bs4.BeautifulSoup(html,'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "No Heading"

    return header.text.strip()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range())
    print("done")


async def get_title_range_old_one():
    for n in range(150,160):
        html = await get_html(n)
        title =  get_title(html, n)
        print(Fore.GREEN + f"Title :  {title}", flush = True)


async def get_title_range():
    tasks = []

    for  n in range(150,160):
        tasks.append((n, asyncio.create_task(get_html(n))))

    for n,t in tasks:
        html = await t
        title =  get_title(html, n)
        print(Fore.GREEN + f"Title :  {title}", flush = True)

if __name__ == '__main__':
    main()



