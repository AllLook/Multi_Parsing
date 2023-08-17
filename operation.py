import asyncio

from threading_download_img import thread_down_img
from multiprocessing_download_img import mult_proc_down
from Multi_Parsing.async_download_img import async_down_img
import argparse as argp
import time


def operation_command():
    start_time = time.time()
    urls = []
    with open('urls.txt', 'r', encoding='utf-8') as f:
        for line in f:
            urls.append(line.replace('\n', ''))
    print(urls)

    parser = argp.ArgumentParser(prog='operation', description='parsing images from links', epilog='end of help')
    parser.add_argument('-m', '--mode', choices=['a', 't', 'm'], default='t', help='Режим выполнения')
    args = parser.parse_args()
    if args.mode == 'm':
        mult_proc_down(urls)
    elif args.mode == 't':
        thread_down_img(urls)
    elif args.mode == 'a':
        asyncio.run(async_down_img(urls))
    else:
        print('Сделайте корректный ввод!')
    print((f'Время выполнения: {time.time() - start_time: .2f}'))


if __name__ == '__main__':
    operation_command()
