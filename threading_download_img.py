import requests
import threading
import time

def thread_down_img(urls):

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

    def download(url):
        start_time = time.time()
        response = requests.get(url, headers=headers)
        # filename = 'thread_' + url.replace('https://', '').replace('/', '')
        file_temp = url.split('/')
        filename = file_temp[-1]
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Download {url} in {time.time() - start_time:.2f} seconds')

    threads = []


    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
