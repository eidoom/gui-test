#!/usr/bin/env python
# coding=UTF-8

import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    label = tk.Label(root, text="Hello world")
    label.pack(padx=40, pady=20)

    root.mainloop()
