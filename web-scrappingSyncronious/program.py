import requests
import bs4


def get_html(episode_number: int):
    print( f"Getting Html for episode {episode_number}", flush=True)

    url = f'http://talkpython.fm/{episode_number}'
    resp = requests.get(url)
    resp.raise_for_status()

    return resp.text

def get_title(html, episode_number):
    print(f"Totle for {episode_number},", flush=True)
    soup = bs4.BeautifulSoup(html,'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "No Heading"

    return header.text.strip()

def main():
    get_title_range()
    print("done")

def get_title_range():
    for n in range(150,160):
        html = get_html(n)
        title = get_title(html, n)
        print( f"Title :  {title}", flush = True)

if __name__ == '__main__':
    main()



