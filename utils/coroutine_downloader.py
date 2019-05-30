import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    print(img_url)
    req = urllib.request.urlopen(img_url)

    with open(img_name, "wb") as f:
        while True:
            img_content = req.read(1024 * 1024)
            if not img_content:
                break
            else:
                f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "vscode.zip", "https://github.com/microsoft/vscode/archive/1.34.0.zip"),
        gevent.spawn(downloader, "4.jpg", "https://rpic.douyucdn.cn/appCovers/2017/09/17/2308890_20170917232900_big.jpg")
    ])


if __name__ == '__main__':
    main()

