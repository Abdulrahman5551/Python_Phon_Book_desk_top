from tkinter import *
from tkinter import ttk
from tkinter import messagebox

"""
This is a [ phone book ] application
Deals in storing data with a [ dictionary ]

"""

class Phone_book:

    def __init__(self, window_phone):
        self.names = {
            "Graham": 9661111111,
            "Hayden": 9662222222,
            "Joel": 9663333333,
            "Easton": 9664444444,
            "Carson": 9665555555,
            "Carter": 9666666666,
            "John": 9667777777,
            "Jack": 9668888888,
            "Leo": 9669999999,
            "Charles ": 9661212121,
        }
        self.window = window_phone

        # Main Window
        self.window.geometry('467x567+410+70')
        self.window.title('Phone Book: 1.0')
        self.window.resizable(False, False)
        self.window.config(bg='#20378D')

        # All Variables
        self.search_var = StringVar()
        self.insert_name_var = StringVar()
        self.insert_number_var = StringVar()

        # Table

        self.tree_frame = Frame(self.window, bg="orange")
        self.tree_frame.place(x=3, y=3, width=251, height=390)

        self.table_tree = ttk.Treeview(self.tree_frame, columns=("1", "2"), height=60,)

        self.table_tree.heading("1", text="Name")
        self.table_tree.column("1", width=140, anchor="center")

        self.table_tree.heading("2", text="Number")
        self.table_tree.column("2", width=120, anchor="center")

        self.table_tree['show'] = 'headings'
        self.table_tree.place(x=1, y=1, height=390)

        self.countor_contact = Label(self.window, text=f"Contact : ", bg="#20378D", fg="white", font=('Calibre', 13))
        self.countor_contact.place(x=5, y=395)

        #Search Box
        self.label_search = Label(self.window, text='Find Name :', bg="#20378D", fg="white", font=('Calibre', 13))
        self.label_search.place(x=268, y=15)

        self.entry_search = Entry(self.window, width=20, font=('Calibre', 13),
         justify='center', textvariable=self.search_var)
        self.entry_search.place(x=268, y=40)
        self.entry_search.focus()

        self.button_search = Button(self.window, text='Search', bd=1, relief=SOLID, command=self.search_data, width=25)
        self.button_search.place(x=268, y=70)

        self.button_return = Button(self.window, text='Re-List', bd=1, relief=SOLID, command=self.reList, width=25)
        self.button_return.place(x=268, y=102)

        # Insert New Data Area
        self.frame_insert = Frame(self.window, bg="#20378D", bd=3, relief=SOLID)
        self.frame_insert.place(x=257, y=170, width=208, height=222)

        self.label_name = Label(self.window, text='Name :', bg="#20378D", fg="white", font=('Calibre', 13))
        self.label_name.place(x=268, y=180)

        self.name = Entry(self.window, width=20, font=('Calibre', 13),
         justify='center', textvariable=self.insert_name_var)
        self.name.place(x=268, y=205)

        self.label_number = Label(self.window, text="Number :", bg="#20378D", fg="white", font=('Calibre', 13))
        self.label_number.place(x=268, y=238)

        self.number = Entry(self.window, width=20, font=('Calibre', 13),
         justify='center', textvariable=self.insert_number_var)
        self.number.place(x=268, y=268)

        self.button_add = Button(self.window, text="Add", bd=1, relief=SOLID, width=25, command=self.add_data)
        self.button_add.place(x=268, y=300)

        self.button_update = Button(self.window, text="Update", bd=1, relief=SOLID, width=25, command=self.update_data)
        self.button_update.place(x=268, y=329)

        self.button_delete = Button(self.window, text="Delete", bd=1, relief=SOLID, width=25, bg="red", command=self.delete_data)
        self.button_delete.place(x=268, y=359)

        self.show_data()
        self.table_tree.bind("<ButtonRelease-1>", self.set_cursor)
        
        
    def show_data(self):

        for key, value in self.names.items():
            d = (key, value)
            self.table_tree.insert("", END, values=d)
    
    def search_data(self):
        getSearch = self.entry_search.get()

        if len(getSearch) > 0:
            if getSearch in self.names:

                for items in self.table_tree.get_children():
                    self.table_tree.delete(items)
                
                key = (getSearch, self.names[getSearch])
                self.table_tree.insert("", END, values=key)
            else:
                for items in self.table_tree.get_children():
                    self.table_tree.delete(items)

                nofoun = ("No Found!", "No Found!")
                self.table_tree.insert("", END, values=nofoun)
        else:
            pass
    
    def reList(self):
        for items in self.table_tree.get_children():
                    self.table_tree.delete(items)
        self.show_data()

        self.search_var.set('')
        self.insert_name_var.set('')
        self.insert_number_var.set('')
        self.count = len(self.names)

        self.countor_contact = Label(self.window, text=f"{self.count}  ", bg="#20378D", fg="white", font=('Calibre', 13))
        self.countor_contact.place(x=75, y=395)
    
    def set_cursor(self, event):
        cursor_row = self.table_tree.focus()
        contents = self.table_tree.item(cursor_row)
        getData = contents['values']

        try:

            self.insert_name_var.set(getData[0])
            self.insert_number_var.set(getData[1])
        
        except IndexError:
            print("Nooo")
    
    def add_data(self):
        keyName = self.insert_name_var.get()
        valueNumber = self.insert_number_var.get()

        if len(keyName) > 0 and len(valueNumber) > 4:
            self.names.update({keyName : valueNumber})
            self.reList()
            messagebox.showinfo('Add', 'Done Add ..')
        else:
            pass
    
    def update_data(self):

        getName = self.insert_name_var.get()
        getNumber = self.insert_number_var.get()
        if len(getName) > 0 or len(getNumber) > 0:

             self.names[getName] = getNumber
             self.reList()
        else:
            pass
    
    def delete_data(self):
        getName = self.insert_name_var.get()
        getNumber = self.insert_number_var.get()

        if len(getName) > 0 and len(getNumber):
            self.names.pop(getName)
            self.reList()
        
        else:
            pass
        
root = Tk()
Phone_book(root)

root.mainloop()