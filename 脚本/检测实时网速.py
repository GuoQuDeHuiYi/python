import psutil
import time
from tkinter import *


# while True:
#     s1 = psutil.net_io_counters()
#     time.sleep(1)
#     s2 = psutil.net_io_counters()
#     result = s2.bytes_recv - s1.bytes_recv
#     print(result/1024)

def make_app():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')
    Label(
        text='Speed Monitor',
        font=('Arial', 25, 'bold'),
        bg='#303030',
        fg='white').pack()

    Label(
        name='lb2',
        text='_kb/s',
        font=('Arial', 20, 'bold'),
        bg='#303030',
        fg='white'
    ).pack()
    return app


def speed_test():
    s1 = psutil.net_io_counters()
    time.sleep(1)
    s2 = psutil.net_io_counters()
    result = s2.bytes_recv - s1.bytes_recv
    return str(result // 1024) + 'kb/s'


def ui_update(do, app):
    data = do()
    lb2 = app.children['lb2']
    lb2.config(text=data)
    app.after(1000, lambda: ui_update(do, app))


app = make_app()
app.after(1000, lambda: ui_update(speed_test, app))
app.mainloop()
