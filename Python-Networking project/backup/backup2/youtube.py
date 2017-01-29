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

  

def fetch():
	os.system("start cmd /C pause")
	os.system("youtube-dl "+ent.get()) 
            

root = Tk()
root.title('Alpha-Youtube')
ent = Entry(root,bd =5,width=50)
ent.insert(0, 'Youtube-downloader')               
ent.pack(side=TOP, fill=X)                     

ent.focus()                                    
ent.bind('<Return>', (lambda event: fetch()))  
btn = Button(root, text='Fetch Video', command=fetch) 
btn.pack(side=RIGHT)


