import tkinter
from tkinter import *
import tkinter.messagebox as m
from operator import itemgetter

class AdressBook():
    def __init__(self):
        self.person = []
        self.top = tkinter.Tk()       
        
        self.top.title("AdressBook Window")
        self.frame = Frame(self.top)      

    def start_function(self):        
        var = StringVar()
        label = Label(self.top, textvariable = var, relief = RAISED)
        var.set("Address Book")
        label.pack()

        self.frame.pack()
        bottomframe = Frame(self.top)
        bottomframe.pack(side = BOTTOM)      

        b = tkinter.Button(self.frame, text = "Add", command = self.add)
        b.pack(side = LEFT)

        middleframe = Frame(self.top)
        middleframe.pack( side = LEFT)

        b1 = tkinter.Button(self.frame, text = "Edit", command = self.edit)
        b1.pack( side = LEFT)

        middle2frame = Frame(self.top)
        middle2frame.pack( side = LEFT)

        b2 = tkinter.Button(self.frame, text = "Delete", command = self.delete_entry)
        b2.pack(side = LEFT)

        b3 = tkinter.Button(self.frame, text = "Display", command = self.display_data)
        b3.pack(side = RIGHT)

        b4 = tkinter.Button(self.frame, text = "Sort", command = self.sort_list)
        b4.pack(side = BOTTOM)

        b4 = tkinter.Button(bottomframe, text = "Quit", command = self.top.destroy)     #bottomframe.quit
        b4.pack(side = BOTTOM)
        
        self.top.mainloop()

    def add(self):
        top1 = tkinter.Tk()
        top1.title("Add window")
        inframe = Frame(top1)
        inframe.pack(side = LEFT)
    
        Label(inframe, text="First Name").grid(row=0)
        Label(inframe, text="Last Name").grid(row=1)
        Label(inframe, text="Adress").grid(row=2)
        Label(inframe, text="City").grid(row=3)
        Label(inframe, text="zip_code").grid(row=4)
        Label(inframe, text="State").grid(row=5)
        Label(inframe, text="Mo. No.").grid(row=6)

        self.e1 = Entry(inframe)
        self.e2 = Entry(inframe)
        self.e3 = Entry(inframe)
        self.e4 = Entry(inframe)
        self.e5 = Entry(inframe)
        self.e6 = Entry(inframe)
        self.e7 = Entry(inframe)       

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)

        Button(inframe, text='Close_window', command=top1.destroy).grid(row=8, column=0, sticky=W, pady=4)
        Button(inframe, text='Add', command=self.get_data).grid(row=8, column=1, sticky=W, pady=4)

       
    def get_data(self):
        person_data = {}
        first_name  = self.e1.get()
        last_name   = self.e2.get()
        address     = self.e3.get()
        person_data['f_name'] = first_name
        person_data['l_name'] = last_name
        person_data['address'] = address
        person_data['city'] = self.e4.get()
        person_data['zipcode'] = self.e5.get()
        person_data['state'] = self.e6.get()
        person_data['mo.no'] = self.e7.get()
        self.person.append(person_data)
        
        var1 = StringVar()
        var1.set(person_data)
        e1 = Entry(self.top, textvariable = var1)
        e1.pack()


    def edit(self):
        top2 = tkinter.Tk()
        top2.title("Edit Window")
        editframe = Frame(top2)
        editframe.pack(side = LEFT)
    
        Label(editframe, text="Enter first name ").grid(row=0)
        
        self.e1 = Entry(editframe)
        
        self.e1.grid(row=0, column=1)
        
        Button(editframe, text='Quit', command=top2.destroy).grid(row=3, column=0, sticky=W, pady=4)
        Button(editframe, text='Edit', command=self.edit_data).grid(row=3, column=1, sticky=W, pady=4)

   
    def edit_data(self):
        first_name = self.e1.get()
        for i in range(len(self.person)):
            
            if self.person[i]['f_name'] == first_name:
                del(self.person[i])
                self.add()
        else:
            print("There is no such name available..")

    
    def delete_entry(self):
        top2 = tkinter.Tk()
        editframe = Frame(top2)
        editframe.pack(side = LEFT)
    
        Label(editframe, text="Enter first name To delete ").grid(row=0)
        
        self.e1 = Entry(editframe)
        
        self.e1.grid(row=0, column=1)
        
        Button(editframe, text='Quit', command=top2.destroy).grid(row=3, column=0, sticky=W, pady=4)
        Button(editframe, text='Delete', command=self.delete_data).grid(row=3, column=1, sticky=W, pady=4)

    def delete_data(self):
        first_name = self.e1.get()
        for i in range(len(self.person)):
            if self.person[i]['f_name'] == first_name:
                del(self.person[i])

    def create_widget(self, dict_data):       
        var2 = StringVar()      
        var2.set(dict_data)
        e1 = Label(self.pframe, textvariable = var2)
        e1.pack()

    def display_data(self):
        self.pframe = Frame(self.top)
        self.pframe.pack(side = LEFT)
        
        for i in self.person:
            self.create_widget(i)
            
    def sort_list(self):
        new_list = sorted(self.person, key = itemgetter('l_name'))
        print("sorted list = ",new_list)

a = AdressBook()
a.start_function()
