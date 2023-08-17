import asyncio
import aiohttp
import time
import requests

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

# urls = [
#     'https://adonius.club/uploads/posts/2022-07/1657235543_1-adonius-club-p-ptitsa-sekretar-ptitsi-krasivo-foto-1.jpg',
#     'https://w.forfun.com/fetch/78/783f6d9bd74ca60727bb580dda1017fd.jpeg',
#     'https://newcoin.ru/wa-data/public/shop/img/lsoagyh-kopirovat.jpg',
#     'https://art-fresco.ru/upload/iblock/24c/dm8goa3xd7tjyyfjeyzr7l86eil51xw6.jpg',
#     'https://u-stena.ru/upload/iblock/6fb/6fb425210836f5c7eeb8f0093ed2dbdf.jpg'
# ]

start_time = time.time()


async def download(url):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            content = await response.read()
            # filename = 'async_' + url.replace('https://', '').replace('/', '')
            file_temp = url.split('/')
            filename = file_temp[-1]
            with open(filename, 'wb') as f:
                f.write(content)
            print(f'Download {url} in {time.time() - start_time:.2f} seconds')


async def async_down_img(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
  


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete()
