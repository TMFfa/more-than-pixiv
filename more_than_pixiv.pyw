# from: https://api.pixivweb.com/
from os import mkdir
from requests import get
from webbrowser import open as open_web
import tkinter as tk
from threading import Thread

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'
}

写真 = 'https://api.pixivweb.com/api.php?return=https'
二次元 = 'https://api.pixivweb.com/anime18r.php?return=https'
黑白 = 'https://api.pixivweb.com/bw.php?return=https'


def mk_dir():
    try:
        mkdir('imgs')
    except:
        pass


def get_img(url):
    r = get(url, headers)
    open_web(r.url)
    title = r.url.split('/')[-1]
    with open('imgs/'+title, 'wb') as f:
        f.write(r.content)


def get_url():
    option = var.get()
    if option == '二次元':
        url = 二次元
    elif option == '写真':
        url = 写真
    elif option == '黑白':
        url = 黑白
    return url


def run():
    url = get_url()
    t = Thread(target=get_img, args=(url,))
    t.start()


if __name__ == '__main__':
    mk_dir()

    win = tk.Tk()
    win.wm_attributes('-topmost', 1)

    var = tk.StringVar()
    r1 = tk.Radiobutton(win, text='二次元', value='二次元', variable=var)
    r2 = tk.Radiobutton(win, text='写真', value='写真', variable=var)
    r3 = tk.Radiobutton(win, text='黑白', value='黑白', variable=var)
    var.set('二次元')

    bt = tk.Button(win, text='next', command=run)

    r1.pack()
    r2.pack()
    r3.pack()
    bt.pack()
    win.mainloop()
