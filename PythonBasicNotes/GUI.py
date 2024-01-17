##'''GUI : Graphical User Interface'''
##
##import tkinter
##
##window = tkinter.Tk()   #to create window
##
###creating simple button
##
##def hello():
##    print('hello world')
##
##
###here background overwrites bg
##button1 = tkinter.Button(window,text = 'Hello World',command = hello,bg = 'blue',background = 'white',fg = 'black')
##
##button2 = tkinter.Button(window,text = 'Hello World',command = hello,bg = 'blue',background = 'white',fg = 'black')
### side-top,bottom,left,right, padding, 
###button.pack(side = 'top',expand = True)
##
###PACK VALUE OPTIONS: -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
##button1.pack(side = 'top',padx = 25, pady = 50,expand = True)  
##
##button2.pack(side = 'top',padx = 25, pady = 50,expand = False,)
##
##
##
##window.mainloop()    #to run window in infinite loop

##
##
##'''LABEL,BUTTON,ENTRY : INPUT FIELD'''
##
##import tkinter
##
##def hello():
##    print('Hello World')
##
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title('Tkinter First App')
##    window.geometry('700x500')   #width x height
##
##    label = tkinter.Label(window,text = 'WELCOME',bg = 'yellow')  #parent is window
##
##    label.pack() #show element on the position
##
##    button = tkinter.Button(window,text = 'Hello World',command = hello) #function call
##    button.pack()
##
##    window.mainloop()
####
##    print('The End') #will get printed while closing the window
##    
##    
##    
##
##'''NESTING'''
##
##import tkinter
##
##def hello():
##    print('Hello World')
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title('Tkinter First App')
##    window.geometry('700x500')
##
##    frame = tkinter.Frame(window)
##    frame.pack()
##
##    label = tkinter.Label(frame,text = 'Hello World')
##    label.pack()
##
##    button = tkinter.Button(frame,text = 'Hello World',command = hello)
##    button.pack()
##
##    window.mainloop()
##
##
##
##
##
##
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##
##    def printHello():
##        print(textentry.get())
##
##        
##    window.title('Tkinter First App')
##    window.geometry('700x1100')
##
##    label = tkinter.Label(window,text = 'Hello World',bg = 'red',fg = 'blue',height = 00,width = 15)
##    label.pack()
##
##      # state disables/enables the entry box
##    #textentry = tkinter.Entry(window,text = 'Hello',bg = '#fdbce1',state = tkinter.DISABLED)      
##    textentry = tkinter.Entry(window,text = 'Hello',bg = '#fdbce1',show = '*')
##    textentry.pack()
##
##
##        # button's background/foreground colour changes when pressed
##    button = tkinter.Button(window,text = 'Hello',bg = '#cdfe34',activebackground = 'orange',activeforeground = 'red',command = printHello)
##    button.pack()
##
##    
##
####
####
##for item in label.keys():
##    print(item,"",label[item])
####    print(button.keys())
##
####    print(label['width'])
####
####
##
##
##def computePrice():
##    totalprice = int(priceperitem_entry.get())*int(numberofitems_entry.get())
##    #Clears the entry before inserting the new value
##    totalprice_entry.delete(0, tkinter.END)
##
##    totalprice_entry.insert(0, str(totalprice))
##
##window = tkinter.Tk()
##window.title('Price Calculator')
##window.geometry('400x200')
##
##priceperitem_label = tkinter.Label(window, text = 'price per item')
##priceperitem_label.pack()
##
##priceperitem_entry = tkinter.Entry(window)
##priceperitem_entry.pack()
##
##
##numberofitems_label = tkinter.Label(window, text = 'no. of items')
##numberofitems_label.pack()
##
##numberofitems_entry = tkinter.Entry(window)
##numberofitems_entry.pack()
##
##
##calculate_button = tkinter.Button(window, text = 'Calculate Total', command = computePrice)
##calculate_button.pack()
###calculate_button.pack(fill = 'x')
##
##
##
##totalprice_label = tkinter.Label(window, text = 'Total Price')
##totalprice_label.pack()
###totalprice_label.pack(side = 'left')
##
##totalprice_entry = tkinter.Entry(window)
##totalprice_entry.pack()
###totalprice_entry.place(x=287, y = 130)
##totalprice_entry.place()
##totalprice_entry.pack(side = 'left',expand = True)
##
##
##
##
##
##widgets = [priceperitem_label,priceperitem_entry,numberofitems_label,
##           numberofitems_entry,totalprice_label,totalprice_entry,calculate_button]
##
##
##for i in range(len(widgets)):
##    widgets[i].place(x=0,y=i*20)
##
##    
##'''GRID'''
##
##priceperitem_label.grid(row = 0,column = 0)
##priceperitem_entry.grid(row = 0,column = 1)
##numberofitems_label.grid(row = 1,column = 0)
##numberofitems_entry.grid(row = 1,column = 1)
##totalprice_label.grid(row = 2,column = 0)
##totalprice_entry.grid(row = 2,column = 1)
##calculate_button.gride(row = 3,column = 0,columnspan = 2)
##
##
##
##
##
##
##
##'''FRAME'''
##
##def computePrice():
##    totalprice = int(priceperitem_entry.get())*int(numberofitems_entry.get())
##    #Clears the entry before inserting the new value
##    totalprice_entry.delete(0, tkinter.END)
##
##    totalprice_entry.insert(0, str(totalprice))
##
##window = tkinter.Tk()
##window.title('Price Calculator')
##window.geometry('400x200')
##
##
##frame = tkinter.Frame(window)
##frame.pack()
##
##priceperitem_label = tkinter.Label(frame, text = 'price per item')
##priceperitem_label.pack()
##
##priceperitem_entry = tkinter.Entry(frame)
##priceperitem_entry.pack()
##
##
##numberofitems_label = tkinter.Label(frame, text = 'no. of items')
##numberofitems_label.pack()
##
##numberofitems_entry = tkinter.Entry(frame)
##numberofitems_entry.pack()
##
##
##calculate_button = tkinter.Button(frame, text = 'Calculate Total', command = computePrice)
##calculate_button.pack()
###calculate_button.pack(fill = 'x')
##
##
##
##totalprice_label = tkinter.Label(frame, text = 'Total Price')
##totalprice_label.pack()
###totalprice_label.pack(side = 'left')
##
##totalprice_entry = tkinter.Entry(frame)
##totalprice_entry.pack()
###totalprice_entry.place(x=287, y = 130)
####totalprice_entry.place()
####totalprice_entry.pack(side = 'left',expand = True)
##
##
##
##
##'''SPINBOX'''
##
##window = tkinter.Tk()
##window.title('Tkinter tutorial')
##
##spin = tkinter.Spinbox(window,from_ = 0,to = 10)
##spin.pack()
##spin = tkinter.Spinbox(window,from_ = 0,to = 10,values = ['hello','hi','yes','no'])
##spin.pack()
##spin = tkinter.Spinbox(window,values = ['hello','hi','yes','no'])
##spin.pack()
##
##
##def spinPressed():
##    print(spinvar.get())
##
##spinvar = tkinter.StringVar()
##spin = tkinter.Spinbox(window,values = ['hello','hi','yes','no',11],textvariable = spinvar,command = spinPressed)
##spin.pack()
##
##
##window.geometry('700x500')    
##window.mainloop()
##
##
##
##
##
##'''
##LAYOUT MANAGERS/GEOMETRY MANAGERS for positioning:
##
##.pack(fill = ,side = ,padx = ,pady = ,expand = True)
##.place(x = ,y = )
##.grid(row = ,col = ,rowspan = ,colspan = )
##'''
## 
##
##'''StringVar()'''
##
##
##import tkinter
####from tkinter import StringVar, Label
##from tkinter import *
##
##window = tkinter.Tk()
##var_1 = StringVar()
##
##label1 = Label(window,font = 'Times 22 bold',relief = 'sunken')
###relief = flat, groove, raised, ridge, solid, or sunken
##label1.pack()
##
##label2 = Label(window,font = 'Times 22 italic',textvariable = var_1)
##label2.pack()
##
##label1.config(text = 'hello')  #UPDATE
####label1['text'] = 'hello1'
##var_1.set('Using textvariable and StringVar()')
##
##button1 = Button(window,text = 'button',relief = 'groove')
##button1.pack()
##
##
##window.mainloop()
##
##
##'''CHECKBUTTON'''
##           
##
##import tkinter
##from tkinter import *
##
##def checkpressed():
##    print(checkvar.get())
##
##
##window = tkinter.Tk()    
##window.title('Title')
##
##
##checkvar = tkinter.StringVar()
##check = tkinter.Checkbutton(window,text = 'Check me!',variable = checkvar,onvalue = 1,offvalue = 0,command = checkpressed)
##check.pack()
##check1 = tkinter.Checkbutton(window,text = 'Check me1!',variable = checkvar,onvalue = 0,offvalue = 1,command = checkpressed)
##check1.pack()
##
##window.mainloop()
##
##
##'''RADIOBUTTON'''
##
##
##import tkinter
####from tkinter import *
##
##
##window = tkinter.Tk()
##
####window = Tk()
##
##window.title('Title')
##
##def radioPressed():
##    print(radiovar.get())
##
##
##radiovar = tkinter.StringVar()
##
##radiom = tkinter.Radiobutton(window,variable = radiovar,text = 'male',value = 'Male',command = radioPressed)
##radiof = tkinter.Radiobutton(window,variable = radiovar,text = 'female',value = 'Female',command = radioPressed)
##radion = tkinter.Radiobutton(window,variable = radiovar,text = 'Other',value = 'Not Specified',command = radioPressed)
##
##
##radiom.pack()
##radiof.pack()
##radion.pack()
##
##window.config(bg = '#ccffb3')
##
##
##
##window.mainloop()
##                            
##
##'''COMBOBOX'''
##
##
##import tkinter
##from tkinter import ttk
##
##def comboFunction(event):
##    print(combo.get())
##
##combo.set('Selection tutorial')
##
##window = tkinter.Tk()
##window.title('Title')
##
##combo = ttk.Combobox(window,values = ['mon','tue','wed','thu','fri'])
##combo.pack()
##
##combo.set('selection day')
##combo.bind('<<ComboboxSelected>>',comboFunction)   #virtual method
##combo['state'] = 'readonly'
##
##combo['values'] = ['july','august','september']
##
##window.mainloop()
##
##
##
##
##
##window.mainloop()




##import tkinter
##
##window = tkinter.Tk()
##
####label = tkinter.Entry(window)
####label.pack()
####
####print(label.keys())
####
##
##
##button = tkinter.Button(window)
##button.pack()
##
##pack_info = button.pack_info()
##print('pack info')
##for key,value in pack_info.items():
##    print(f'{key}:{value}')
##    
##
##window.mainloop()



##'''LISTBOX'''
##
##import tkinter
##
##def listSelected(event):
##    print(listbox.get(listbox.curselection()))
##
##window = tkinter.Tk()
##window.title('Tkinter Tutorial')
##
##listvar = tkinter.StringVar(value = ['mon','tue','wed','thu','sun'])
##listbox = tkinter.Listbox(window, listvariable = listvar,height = 2,selectmode = 'extended')
##listbox.pack()
##listbox.bind('<<ListboxSelect>>',listSelected)
##
##window.mainloop()



##'''TEXT WIDGET'''
##
##
##import tkinter
##
##window = tkinter.Tk()
##
###creating the text
##text = tkinter.Text(window,width = 40,height = 10,font = ('Arial',14))
##text.pack()
##
##
##def gettext():
####    print(text.get('0.0','0.3'))     #ERROR
##    print(text.get('0.0','1.1'))
####    print(text.get('1.0','1.4'))
####    print(text.get('1.0','end'))
##
##
##get_button = tkinter.Button(window, text = 'get text',command = gettext)
##get_button.pack()
##
##
##def inserttext():
##    text.insert('1.0','just inserted text')
##
##
##insert_button = tkinter.Button(window, text = 'insert text',command = inserttext)
##insert_button.pack()
##
##
##def deletetext():
####    text.delete('0.0','end')
##    text.delete('0.0','1.5')
##
##
##delete_button = tkinter.Button(window,text = 'delete text',command = deletetext)
##delete_button.pack()
##    
##          
##window.mainloop()



##'''MESSAGE BOX & POPUPS'''
##
##import tkinter
##from tkinter import messagebox
##
##window = tkinter.Tk()
##
##def openmessagebox():
##    messagebox.showinfo('message','Button was pressed')
##
####    messagebox.showerror('message','Button was pressed')
##    
####    messagebox.showwarning('message','Button was pressed')
##
####    messagebox.askquestion('message','Button was pressed')
##    
####    messagebox.
##
##
##    result_question = messagebox.askquestion(title = 'question',message = 'Do want to Proceed?')
##    if result_question == 'Yes':
##        print('user chose yes')
##
##    else:
##        print('user chose no')
##        print(result_question)
##
##button = tkinter.Button(window,text = 'Press Me',command = openmessagebox)
##button.pack()
##window.mainloop()



##"notes"


##creating simple button ex:
##def hello():
##    print("Hello World")
##
##window = tkinter.Tk()
##button = tkinter.Button(window, text='Hello World',command=hello,bg="yellow",fg="blue")
##button.pack(side="bottom",padx=5,pady=20,expand=True)
##window.mainloop()

####Label, Button, Entry (Input Field)

##def hello():
##    print("Hello World")
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title("Tkinter First App")
##    window.geometry('600x400')
##
##    label = tkinter.Label(window, text="Hello World",)##here parent is window
##    label.pack()##show  element on the position
##    
##    button = tkinter.Button(window, text='Hello World', command=hello)##it calling func
##    button.pack()
##    window.mainloop()
##    print("Hi")##hi will always print after close


##def hello():
##    print("Hello World")
##
##window = tkinter.Tk()
##window.title("Tkinter First App")
##window.geometry('600x400')
##
##
##button = tkinter.Button(window, text='Hello World',command=hello,bg="yellow",fg="blue")
##button.pack(side="bottom",padx=5,pady=20,expand=True)
##window.mainloop()




##
##def hello():
##    print("Hello World")
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title("Tkinter First App")
##    window.geometry('600x400')
##    
##    frame = tkinter.Frame(window)
##    frame.pack()
##    
##    label = tkinter.Label(frame, text="Hello World")
##    label.pack()
##    
##    button = tkinter.Button(frame, text='Hello World', command=hello)
##    button.pack()
##    
##    print(str(label))
##    
##    window.mainloop()
##    print("Hi")



##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title("Tkinter First App")
##    window.geometry('600x400')
##
##    label = tkinter.Label(window, text="Hello World", bg="red", fg="blue", width=50)
##    label.pack()
##
##    textentry = tkinter.Entry(window)
##    textentry.pack()
##
##    button = tkinter.Button(window, text='Click Me')
##    button.pack()
##
##    window.mainloop()



##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title("Tkinter First App")
##    window.geometry('600x400')
##
##    label = tkinter.Label(window, text="Hello World", fg="blue", width=50,)
##    label.pack()
##
##    textentry = tkinter.Entry(window, bg="#fdbce1",show="#")
##    textentry.pack()
##
##    button = tkinter.Button(window, text='Hello', bg="#cdfe34")
##    button.pack()
##
##    window.mainloop()



##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title("Tkinter First App")
##    window.geometry('600x400')
##
##    label = tkinter.Label(window, text="Hello World", fg="blue", width=50)
##    label.pack()
##
##    textentry = tkinter.Entry(window, bg="#fdbce1",width=50,state=tkinter.DISABLED)
##    textentry.pack()
##
##    button = tkinter.Button(window, text='Hello', bg="#cdfe34",activebackground="red",activeforeground="white")
##    button.pack()
##    
##    for item in label.keys():
##        print(item,"",label(item))
##    print(label.keys())
##    window.mainloop()

##import tkinter
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##
##    def printHello():
##        print(textentry.get())
##
##    window.title("Tkinter First App")
##    window.geometry('600x400')
##
##    label = tkinter.Label(window, text="Hello World", fg="blue", width=50)
##    label.pack()
##
##    textentry = tkinter.Entry(window, bg="#fdbce1",show="*")
##    textentry.pack()
##
##    button = tkinter.Button(window, text='Hello', bg="#cdfe34", command=printHello).pack()
##    button.pack()
##
##    for item in label.keys():
##        print(item,"",label[item])
##    print(button.keys())
####    print(label["width"])
##
##    window.mainloop()

##import tkinter
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##
##    def printHello():
##        print(textentry.get())
##
##    window.title("Tkinter First App")
##    window.geometry('600x400')
##
##    label = tkinter.Label(window, text="Hello World", fg="blue", width=50)
##    label.pack()
##
##    textentry = tkinter.Entry(window, bg="#fdbce1", show="*")
##    textentry.pack()
##
##    button = tkinter.Button(window, text='Hello', bg="#cdfe34", command=printHello)
##    button.pack()
##
####    for item in button.keys():
####        print(item, "", button[item])
##    
##    pack_info = button.pack_info()
##    print("Pack Info:")
##    for key, value in pack_info.items():
##        print(f"{key}: {value}")
##    window.mainloop()
##
##

##Layout Managers - position with pack(), place(), grid()
####pack()
##
##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.delete(0, tkinter.END)  # Clear the entry before inserting the new value
##    totalprice_entry.insert(0, str(totalprice))
##
##window = tkinter.Tk()
##window.title("Price Calculator")
##window.geometry('400x200')
##
##priceperitem_label = tkinter.Label(window, text="Price per item")
##priceperitem_label.pack()
##priceperitem_entry = tkinter.Entry(window)
##priceperitem_entry.pack()
##
##numberofitems_label = tkinter.Label(window, text="Number of items")
##numberofitems_label.pack()
##numberofitems_entry = tkinter.Entry(window)
##numberofitems_entry.pack()
##
##totalprice_label = tkinter.Label(window, text="Total price:")
##totalprice_label.pack()
####totalprice_label.pack(side="left")
##totalprice_entry = tkinter.Entry(window)
##totalprice_entry.pack()
####totalprice_entry.pack(side="right")
##
##calculate_button = tkinter.Button(window, text="Calculate total", command=computePrice)
##calculate_button.pack()
####calculate_button.pack(fill='x')
##
##window.mainloop()
##
##

##place
##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.insert(0, string=str(totalprice))
##    
##window = tkinter. Tk()
##priceperitem_label = tkinter.Label(window, text = "Price per item")
##priceperitem_entry = tkinter. Entry(window)
##numberofitems_label = tkinter.Label(window, text = "Numebr of items")
##numberofitems_entry = tkinter. Entry(window)
##totalprice_label = tkinter.Label(window, text="Total price:")
##totalprice_entry = tkinter.Entry(window)
##calculate_button = tkinter.Button(window, text="Calculate total", command=computePrice)
##
##priceperitem_label.place(x=0, y=0)
##priceperitem_entry.place(x=0, y=50)
##window.mainloop()


##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.delete(0, tkinter.END)  # Clear the entry before inserting the new value
##    totalprice_entry.insert(0, str(totalprice))
##
##window = tkinter.Tk()
##window.title("Price Calculator")
##window.geometry('400x200')
##
##priceperitem_label = tkinter.Label(window, text="Price per item")
##priceperitem_label.place(x=0, y=0)
##priceperitem_entry = tkinter.Entry(window)
##priceperitem_entry.place(x=0, y=20)
##
##numberofitems_label = tkinter.Label(window, text="Number of items")
##numberofitems_label.place(x=0, y=50)
##numberofitems_entry = tkinter.Entry(window)
##numberofitems_entry.place(x=0, y=70)
##
##totalprice_label = tkinter.Label(window, text="Total price:")
##totalprice_label.place(x=0, y=100)
##totalprice_entry = tkinter.Entry(window)
##totalprice_entry.place(x=0, y=120)
##
##calculate_button = tkinter.Button(window, text="Calculate total", command=computePrice)
##calculate_button.place(x=0, y=150)
##
##window.mainloop()



##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.insert(0, string=str(totalprice))
##    
##window = tkinter. Tk()
##priceperitem_label = tkinter.Label(window, text = "Price per item")
##priceperitem_entry = tkinter. Entry(window)
##numberofitems_label = tkinter.Label(window, text = "Numebr of items")
##numberofitems_entry = tkinter. Entry(window)
##totalprice_label = tkinter.Label(window, text="Total price:")
##totalprice_entry = tkinter.Entry(window)
##calculate_button = tkinter.Button(window, text="Calculate total", command=computePrice)

##
####widgets = [priceperitem_label, priceperitem_entry, numberofitems_label,
####numberofitems_entry, totalprice_label, totalprice_entry, calculate_button]
####
####for i in range(len(widgets)):
####    widgets[i].place(x=0, y=i*20)
##
####Grid
##
##priceperitem_label.grid(row=0, column =0)
##priceperitem_entry.grid(row= 0, column=1)
##numberofitems_label.grid(row=1, column=0)
##numberofitems_entry.grid(row=1, column=1)
##totalprice_label.grid(row=2, column=0)
##totalprice_entry.grid(row=2, column=1)
##calculate_button.grid(row=3, column=0,columnspan=2)

##grid responsive

##window.grid_rowconfigure(0, weight=1)
##window.grid_rowconfigure(1, weight=1)
##window.grid_rowconfigure(2, weight=1)
##window.grid_rowconfigure(3, weight=1)
##window.grid_columnconfigure(0, weight=1)
##window.grid_columnconfigure(1, weight=1)


##rows = 4
##columns = 2
##for i in range(rows):
##    window.grid_rowconfigure(i, weight=1)
##for i in range(columns):
##    window.grid_columnconfigure(i, weight=1)

   
##window.mainloop()

#######frame
####grid w ith frame
##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.insert(0, string=str(totalprice))
##    
##window = tkinter. Tk()
##frame = tkinter.Frame(window)
##priceperitem_label = tkinter.Label(frame, text="Price per item")
##priceperitem_entry = tkinter.Entry(frame)
##numberofitems_label = tkinter.Label(frame, text="Numebr of items")
##numberofitems_entry = tkinter. Entry(frame)
##totalprice_label = tkinter.Label(frame, text="Total price:")
##totalprice_entry = tkinter. Entry(frame)
##calculate_button = tkinter. Button(frame, text="Calculate total", command=computePrice)
##
##priceperitem_label.grid(row=0, column =0)
##priceperitem_entry.grid(row= 0, column=1)
##numberofitems_label.grid(row=1, column=0)
##numberofitems_entry.grid(row=1, column=1)
##totalprice_label.grid(row=2, column=0)
##totalprice_entry.grid(row=2, column=1)
##calculate_button.grid(row=3, column=0, columnspan=2)
##
##frame. pack()
##window.mainloop()

####use padding and center
##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.delete(0, tkinter.END)  # Clear the entry before inserting the new value
##    totalprice_entry.insert(0, str(totalprice))
##    
##window = tkinter.Tk()
##window.title("Price Calculator")
##
##frame = tkinter.Frame(window)
##frame.pack(pady=20, padx=20)
#####frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)##center
##
##priceperitem_label = tkinter.Label(frame, text="Price per item")
##priceperitem_label.grid(row=0, column=0, pady=5, padx=5)
##priceperitem_entry = tkinter.Entry(frame)
##priceperitem_entry.grid(row=0, column=1, pady=5, padx=5)
##
##numberofitems_label = tkinter.Label(frame, text="Number of items")
##numberofitems_label.grid(row=1, column=0, pady=5, padx=5)
##numberofitems_entry = tkinter.Entry(frame)
##numberofitems_entry.grid(row=1, column=1, pady=5, padx=5)
##
##totalprice_label = tkinter.Label(frame, text="Total price:")
##totalprice_label.grid(row=2, column=0, pady=5, padx=5)
##totalprice_entry = tkinter.Entry(frame)
##totalprice_entry.grid(row=2, column=1, pady=5, padx=5)
##
##calculate_button = tkinter.Button(frame, text="Calculate total", command=computePrice)
##calculate_button.grid(row=3, column=0, columnspan=2, pady=5, padx=5)
##
##window.mainloop()
##

##Spinbox, Checkbox, Radiobutton

##Spinbox

##
##window = tkinter.Tk()
##window.title("Tkinter tutorial")
####spin = tkinter.Spinbox(window, from_=0, to=10)
####spin = tkinter.Spinbox(window, from_=0, to=10, values=["hello", "hi", "yes", "no"])
####spin = tkinter.Spinbox(window, values=["hello", "hi", "yes", "no"])
##spin.pack()
##window.mainloop()

##def spinPressed():
##    print(spinvar.get())
##    
##window=tkinter. Tk()
##window.title("Tkinter tutorial")
##
##spinvar = tkinter.StringVar()
##spin = tkinter.Spinbox(window, values=["hello", "hi", "yes", "no"], textvariable=spinvar, command=spinPressed)
##spin.pack()
##
##window.mainloop()

##Checkbox
##def checkPressed():
##    print(checkvar.get())
##    
##window=tkinter. Tk()
##window.title("Tkinter tutorial")
##
##checkvar = tkinter. StringVar()
##check = tkinter.Checkbutton(window, text="Check me!", variable=checkvar, onvalue="Yes", offvalue="No", command=checkPressed)
##check.pack()
##                            
##window.mainloop()


#####radio
##window = tkinter. Tk()
##window. title("Tkinter tutorial")
##
##def radioPressed():
##    print(radiovar.get())
##
##radiovar = tkinter.StringVar()
##radio = tkinter.Radiobutton(window, variable=radiovar, text="June", value="June month",command=radioPressed)
##radio1 = tkinter.Radiobutton(window, variable=radiovar, text="July", value= "July month",command=radioPressed)
##radio2 = tkinter.Radiobutton(window, variable=radiovar, text="August", value="August month",command=radioPressed)
##radio3 = tkinter.Radiobutton(window, variable=radiovar, text="September", value="Sept month",command=radioPressed)
##
##radio.pack()
##radio1. pack()
##radio2.pack()
##radio3.pack()
##
##window.mainloop()


####Combobox, Listbox
##Combobox

##import tkinter
##from tkinter import ttk
##
##window = tkinter.Tk()
##window.title("Tkinter tutorial")
##
##combo = ttk.Combobox(window, values=["Monday", "Tuesday", "Wednesday", "Thursday"])
##combo.pack()
##
##window.mainloop()



##from tkinter import ttk
##
##def comboFunction(event):
##    print(combo.get())
######    combo.set("Selection Changed")
##
##window = tkinter.Tk()
##window.title("Tkinter tutorial")
##
##combo = ttk.Combobox(window, values=["Monday", "Tuesday", "Wednesday", "Thursday"])
##combo.pack()
##
##combo.set("Selection day")
##combo.bind('<<ComboboxSelected>>', comboFunction)
##combo["state"]='readonly'
######combo["values"]=['july','August','september']
##window.mainloop()
##


##import tkinter
##
##def listSelected(event):
##    print(listbox.get(listbox.curselection()))
######    print(listbox.curselection())
##
##window = tkinter.Tk()
##window.title("Tkinter tutorial")
##
##listvar = tkinter.StringVar(value=["Monday", "Tuesday", "Wednesday", "Thursday","Sunday"])
##listbox = tkinter.Listbox(window, listvariable=listvar, height=2, selectmode='extended')
##listbox.pack()
##listbox.bind("<<ListboxSelect>>", listSelected)
##
##window.mainloop()



####Text Widget


##window = tkinter.Tk()
##
### Creating the text
##text = tkinter.Text(window, width=40, height=10, font=("Arial", 14))
##text.pack()
##
##def gettext():
##    print(text.get("1.0", "1.2"))
####    print(text.get("1.0", "end"))
##
##get_button = tkinter.Button(window, text="Get text", command=gettext)
##get_button.pack()
##
##def inserttext():
##    text.insert('1.0', 'just inserted text')
##    
##insert_button = tkinter.Button(window, text="Insert text", command=inserttext)
##insert_button.pack()
##
##def deletetext():
##    text.delete("0.0","end")
##    
##delete_button = tkinter.Button(window, text="Delete text", command=deletetext)
##delete_button.pack()
##
##window.mainloop()



#### Messagebox and Popups 
##import tkinter
##from tkinter import messagebox
##
##def openMessageBox():
##    messagebox.showinfo("Message", "Button was pressed")
##    messagebox.showinfo(title="Message", message="Button was pressed")
##    messagebox.showerror(title="Message", message="Button was pressed")
##    # messagebox.showwarning(title="Message", message="Button was pressed")
##    messagebox.askquestion("Mess", "Button was pressed")
##    # messagebox.showwarning(title="Warning!", message="Do not close this window!")
##
##    result_question = messagebox.askquestion(title="Question", message="Do you wish to proceed?")
##    if result_question=='yes':
##      print("user chose yes")
##    else:
##        print("user chose no")
##    print(result_question)
######    
##window = tkinter.Tk()
##button = tkinter.Button(window, text="Press Me", command=openMessageBox)
##button.pack()
####
##window.mainloop()



##'''BACKGROUND IMAGE & ICON'''
##
##
##from tkinter import *
##from PIL import ImageTk
##
##win = Tk()
##
##win.title('master')
##win.iconbitmap('smiley-1635449_1280.ico')
##win.maxsize(width = 1000,height = 500)
##win.minsize(width = 600,height =500)
##
##file = ImageTk.PhotoImage(file = 'wp3409937-hd-background-pattern.jpg')
##
##label = Label(win,image = file)
##label.pack()
##
##win.mainloop()


