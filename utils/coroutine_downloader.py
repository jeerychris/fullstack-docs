import urllib.request
import os
import sys
import gevent
from gevent import monkey

monkey.patch_all()

download_dir = r'E:\BaiduNetdiskDownload'
url = "https://download-cf.jetbrains.com/cpp/CLion-2019.1.4.win.zip"
file_name = url[url.rindex('/') + 1:]
file = os.path.join(download_dir, file_name)


def downloader(file, url):
    print(url)
    req = urllib.request.urlopen(url)

    with open(file, "wb") as f:
        while True:
            img_content = req.read(1024 * 1024)
            if not img_content:
                print("%s completed" % file)
                break
            else:
                f.write(img_content)


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(downloader, file, url),
    ])
