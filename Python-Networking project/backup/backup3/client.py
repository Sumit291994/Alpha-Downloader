import asyncore
import socket
import time
import thread
from time import *
import threading, urllib2,urllib
import Queue
import sys
from Tkinter import *
import tkFileDialog, Tkconstants
import os
import ttk
from urllib2 import Request, HTTPError, URLError
import httplib
import tkMessageBox
from Tkinter import *

 


def foo1():
  execfile("client1.py")
  
def foo2():
  execfile("pong.py")

def foo3():
  execfile("s.py")
  
root = Tk()
root.title('Alpha-Smart_Client')
ent = Entry(root,bd =5,width=50,background="lightyellow")
ent.insert(0, 'Smart Client ALPHA++')               
ent.pack(side=TOP, fill=X)                     
 
btn = Button(root, text='Game', background="pink",command=foo2) 
btn.pack(side=RIGHT)
btn1 = Button(root, text='File transfer', background="lightblue",command=foo1) 
btn1.pack(side=LEFT)
btn2 = Button(root, text='File Accept', background="lightblue",command=foo3) 
btn2.pack(side=LEFT)
root.mainloop()