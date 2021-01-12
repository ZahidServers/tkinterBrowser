# Code By Mohammed Zahid Imtiyaz Wadiwale
from tkinter import *
from tkhtmlview import HTMLScrolledText
import requests
from bs4 import BeautifulSoup
browser=Tk(className=" Zahid Browser")
browser.state("zoomed")
def frame():
	address=str(url.get())
	try:
		page=requests.get(address)
		vfs=str(BeautifulSoup(page.content,'html.parser').prettify())
	except Exception as e:
		vfs="<h1>Zahid Browser</h1><h2>404 Error</h2><h3>Check your Internet Connection</h3>"
	html_label.set_html(vfs)
url=Entry(browser,font=("times",10,"normal"),width=180)
url.grid(row=1,column=1)
go=Button(browser,text="GO",command=frame)
go.grid(row=1,column=2)
html_label=HTMLScrolledText(browser, html='<h1 style="color:red; text-align: center;"> Hello Welcome To Zahid Browser !</h1>')
html_label.grid(row=2,column=1,columnspan=2)
html_label.config(height=40,width=150)
browser.mainloop()
