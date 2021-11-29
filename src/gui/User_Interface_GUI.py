#!/usr/bin/env python3
"""
Created on Wed Oct 27 17:56:15 2021

@author: Yiru Xiong
"""
#!pip install tk
from tkinter import *
from tkinter.ttk import Combobox
import webbrowser


# create the interface for the toolbox
gui = Tk()
label = Label(gui, text="Welcome to Big Data Processing Application", fg='skyblue1', font=("Book Antiqua", 32))
label.place(x=180, y=60)
label.configure(bg='lavender')
button1 = Button(gui, text = "1. Apache Hadoop", fg='palevioletred3', font=("Book Antiqua", 16),height=2, width=15)
button1.place(x=50, y=150)
button2 = Button(gui, text = "2. Apache Spark", fg='palevioletred3', font=("Book Antiqua", 16), height=2, width=15)
button2.place(x=280, y=150)
button3 = Button(gui, text = "3. Jupyter Notebook", fg='palevioletred3', font=("Book Antiqua", 16), height=2, width=15)
button3.place(x=510, y=150)
button4 = Button(gui, text = "4. SonarQube & SonarScanner", fg='palevioletred3', font=("Book Antiqua", 16), height=2, width=22)
button4.place(x=740, y=150)

# ask for the user input
# create the list box for user input
L2 = Label(gui, text="Please select the number that corresponds to the application you would like to run", fg='mediumturquoise', font=("Book Antiqua", 19))
L2.place(x=30, y=230)
L2.configure(bg='lavender')
# select from combobox
button_list = ["1. Apache Hadoop", "2. Apache Spark", "3. Jupyter Notebook", "4. SonarQube & SonarScanner"]
optionlist = Combobox(gui, values=button_list, height=20, width=25)
optionlist.place(x=420, y=260)
confirm_button = Button(gui, text = "confirm", fg='mediumturquoise', font=("Book Antiqua", 16),height=2, width=6,command=lambda: confirm())
confirm_button.pack()
confirm_button.place(x=510, y=300)
def confirm():
    if optionlist.get() == "1. Apache Hadoop":
        webbrowser.open('http://35.239.106.172:9870/')
    elif optionlist.get() == "2. Apache Spark":
        webbrowser.open('http://34.132.229.113:8080/')
    elif optionlist.get() == "3. Jupyter Notebook":
        webbrowser.open('http://35.232.118.254:8888/')
    elif optionlist.get() == "4. SonarQube & SonarScanner":
        webbrowser.open('http://104.197.148.211:9000/')
    else:
        return

# enter the option
L2 = Label(gui, text="Or type the number that corresponds to the application you would like to run. Valid Inputs are 1,2,3,4", fg='mediumturquoise', font=("Book Antiqua", 19))
L2.place(x=30, y=390)
L2.configure(bg='lavender')
var= StringVar()

user_entry = Entry(gui, textvariable=var, bd=2)
user_entry.pack()
user_input = user_entry.get()
user_entry.place(x=450,y=420)

# valid input: 1,2,3,4
app_nums = ["1","2","3","4"]
def submit():
    global user_entry
    global input_string
    input_string = user_entry.get()
    if input_string not in app_nums:
    	print("Please enter a valid application number")
    else:
        print("user input is:", input_string)
        if (input_string == "1"):
        	webbrowser.open('http://35.239.106.172:9870/')
        elif (input_string == "2"):
        	webbrowser.open('http://34.132.229.113:8080/')
        elif (input_string == "3"):
        	webbrowser.open('http://35.232.118.254:8888/')
        elif (input_string == "4"):
        	webbrowser.open('http://104.197.148.211:9000/')
        else:
        	return

submit_button = Button(gui, text = "Submit", fg='mediumturquoise', font=("Book Antiqua", 16),height=2, width=6,command=lambda: submit())
submit_button.pack()
submit_button.place(x=510, y=460)

gui.title('Data Science Toolbox v.1.5.1')
gui.geometry("500x500+11+11")
gui.configure(bg='lavender')

gui.mainloop()



    