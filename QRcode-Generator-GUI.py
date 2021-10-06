#Code By Harshit Ratan Shukla
#QR code stands for Quick Response Code. QR codes may look simple but they are capable of storing lots of data. 
#Irrespective of how much data they contain when scanned QR code allows the user to access information instantly. That is why they are called Quick Response Code.
#These are being used in many scenarios these days.
#QR codes can be used to store(encode) lots of data and that too of various types. 
#For example, they can be used to encode: Contact details, Facebook ids, Instagram ids, Twitter ids, WhatsApp ids,Event Details,Youtube links,Product details,Link #directly to download an app on the Apple App Store or Google Play.
#They are also being used in doing digital transactions by simply scanning QR codes.

import qrcode
from tkinter import *
import tkinter as tk

#GUI
root = tk.Tk()
root.geometry('700x280')
root.title('QR code Generator GUI')
root.resizable(False, False)

#Define Show Button Function
def showQR():
	 if(len(info.get()) != 0):
	 	img = qrcode.make(info.get())
	 	img.show()
	 	#info.delete(0, END)
	 else:
	 	info.insert(0,"Enter your Data Here to convert it into QR Code... Press 'Clear' Button to Clear this Field.")
	 
#Define Clear Button Function
def clear():
   info.delete(0, END)


#Define Exit Button Function
def exit():
    root.destroy()


w1_label = Label(root, text="QR codes can be used to store(encode) lots of data and that too of various types.", font=('verdana', '10', 'bold'))
w1_label.place(x=1, y=1)

w2_label = Label(root, text="For example, they can be used to encode:", font=('verdana', '10', 'bold'))
w2_label.place(x=1, y=20)

w2_label = Label(root, text="1.) Contact details, Facebook ids, Instagram ids, Twitter ids, WhatsApp ids.", font=('verdana', '10', 'bold'))
w2_label.place(x=1, y=40)

w3_label = Label(root, text="2.) Event Details,Youtube links,Product details.", font=('verdana', '10', 'bold'))
w3_label.place(x=1, y=60)

w4_label = Label(root, text="3.) Link directly to download an app on the Apple App Store or Google Play.", font=('verdana', '10', 'bold'))
w4_label.place(x=1, y=80)

w5_label = Label(root, text="4.) They are also being used in doing digital transactions by simply scanning QR codes.", font=('verdana', '10', 'bold'))
w5_label.place(x=1, y=100)


w6_label = Label(root, text="Enter your Data to convert it into QR Code::::::::: ", font=('verdana', '10', 'bold'))
w6_label.place(x=1, y=150)


info = Entry(root, width=85, relief=RIDGE, borderwidth=2)
info.place(x=1, y=180)


show = Button(root, text="Show_QR", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=showQR)
show.place(x=550, y=225)

clear = Button(root, text="Clear", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=clear)
clear.place(x=450, y=225)

exit = Button(root, text="Exit", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=exit)
exit.place(x=1, y=225)

root.mainloop()