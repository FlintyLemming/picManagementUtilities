from pynput import keyboard
import pandas as pd
from win10toast import ToastNotifier


def on_activate():
    df = pd.read_clipboard()
    toster = ToastNotifier()
    toster.show_toast("title", df.columns[0], duration=5)


with keyboard.GlobalHotKeys({
    '<ctrl>': on_activate}) as h:
    h.join()
