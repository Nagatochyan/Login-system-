from sre_constants import SUCCESS
import tkinter
import tkinter as tk
import subprocess
import threading
from turtle import color
import sqlite3
import csv

def widgets():
    A =("設定したいユーザーネーム")
    B =("設定したいパスワード")
    root = tk.Tk()
    root.title("Naganegi Raider Ver1.7")
    root.geometry("400x300")
    def close_window():
        root.destroy()
    root['bg'] = "#d0d0d0"
    
    user= tk.Label(text = "User name",fg="black",bg="#d0d0d0",font=("20"))
    user.place(x=40, y=40)
    
    userw = tk.Entry(fg="black")
    userw.place(x=200, y=48, width=170, height=20)
    
    pasw= tk.Label(text = "Password",fg="black",bg="#d0d0d0",font=("20"))
    pasw.place(x=40, y=100)
    
    pasww = tk.Entry(fg="black",show="●")
    pasww.place(x=200, y=108, width=170, height=20)
    def click():
        username = userw.get()
        papapa= pasww.get()
        if username == A and papapa==B:
            print ("SUCCESS")
        else:
            print("fail")
    button = tk.Button(text = "Login",fg="green",bg="#d0d0d0",font=("30"),activebackground="#57fb19",command=click)
    button.place(x=110, y=150, width=170)
    root.mainloop()
th1 = threading.Thread(target=widgets)
th1.start()
