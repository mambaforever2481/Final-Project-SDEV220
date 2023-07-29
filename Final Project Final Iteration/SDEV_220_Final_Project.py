from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog


window1 = Tk()
window1.geometry("1150x400")     
window1.config(bg="white")      
window1.resizable(width=True,height=True)       
window1.title('NBA Stats: Enter your name to continue...')


window2 = Tk()
window2.geometry("1150x400")     
window2.config(bg="white")      
window2.resizable(width=True,height=True)       
window2.title('NBA Stats: Select a spreadsheet or file to continue...')

class Introduction:
    def __init__(self,master):
          my_label = Label(master, text = "Welcome to the NBA Stats Application!", bg= 'white')
          my_label.pack()


class User:
    def __init__(self, window1):
        self.l1 = Label(window1,text="NBA Stats",font=("Arial", 25),fg="black",bg="white")      #initializes the header label for the main window
        self.l2= Label(window1,text="Enter your name: ",font=("Arial", 10,"bold"),bg="white")        #Initializes the extry box label for the main window

        self.name = Entry(window1)       #initializes the entry box for which the users name will be entered

        self.btn1 = Button(window1,text="Submit",font=("Arial", 10),command=self.get_name)        #initializes the submit button
        self.btn2 = Button(window1,text="Exit application",font=("Arial", 10),command=exit)      #initializes the exit button

        self.l1.pack()   #packs the label in the main window
        self.l2.pack()  #packs the label in the main window
        self.name.pack()  #packs the label in the main window
        self.btn1.pack()  #packs the button in the main window
        self.btn2.pack()  #packs the button in the main window
    
    def get_name(self):
        self.name1 = self.name.get()      #Assigns the user's name to the variable name1
        if self.name1.isalpha() and len(self.name1) > 0:      #Checks to see if the user entered a valid name
            window1.destroy()
            main = MainWindow(window2)    #If the user entered a valid name, open the NBA player name choice page
        else:       #If the user did not enter a valid name, prompt them to enter a valid name, and return to the main menu
            window3 = Toplevel(window1)     #creates a new toplevel child window with the master window window1 as the parent
            window3.geometry("1150x400")     #configures the window to be 500x500
            window3.config(bg="white")      #configures the window to be white
            window3.resizable(width=False,height=False)     #configures the window to not be resizable
            window3.title('Error')      #configures the window to have a title
            self.l1 = Label(window3,text="You must enter your name to continue",font=("Arial", 20),fg="black",bg="white")        #creates a label with the text "You must enter your name to continue"
            self.l1.pack()       #packs the label onto the window
            self.btn1 = Button(window3,text="OK",font=("Arial", 10), command=window3.destroy)        #creates a button with the text "OK"
            self.btn1.pack()
            self.btn4 = Button(window3,text="Exit application",font=("Arial", 10),command=exit)        #creates an exit button with the text "Exit application"
            self.btn4.pack()     #packs the button onto the frame_two
    
         

class MainWindow:
    def __init__(self, master):


        self.my_frame = Frame(master)
        self.my_frame.pack(pady=20)

        self.my_tree = ttk.Treeview(self.my_frame)
        
        self.my_menu = Menu(master)
        master.config(menu = self.my_menu)

        self.file_menu = Menu(self.my_menu, tearoff= False)
        self.my_menu.add_cascade(label= "Spreadsheets", menu= self.file_menu)
        self.file_menu.add_command(label = "Open", command= self.file_open)
        
        self.my_label = Label(master, text= '', bg = 'white')
        self.my_label2 = Label(master, text = "Please open a file or spreadsheet to continue...", bg= 'white')
        self.my_entry = Entry(self.my_frame, width = 25, bg = "white")
        self.my_button = Button(self.my_frame, width = 15, bg = "white", text= "Search for a player...", command= self.player_search)
        self.my_button2 = Button(self.my_frame, width = 15, bg ="white", text= "Search by team...", command= self.team_search)
        self.my_button3 = Button(self.my_frame, width = 15, bg ="white", text= "Search by position...", command= self.position_search)


        self.my_entry.pack_forget()
        self.my_button.pack_forget()
        self.my_button2.pack_forget()

        self.my_label2.pack()
        self.my_label.pack(pady= 20)
    
    def file_open(self):
        filename = filedialog.askopenfilename(
            initialdir= "C:",
            title = "Open a file",
            filetypes = (("All files", "*.*"),("xlsx files", "*.xlsx")) 
        )
        if filename:
            try:
                filename = r"{}".format(filename)
                global df
                df = pd.read_csv(filename)
            except ValueError:
                self.my_label.config(text="File could not be opened, try again.")
            except FileNotFoundError:
                self.my_label.config(text="File could not be found, try again.")

        self.clear_tree()
        self.my_label2.destroy()
        
        self.my_tree["column"] = list(df.columns)
        self.my_tree["show"] = "headings"
    
        for column in self.my_tree["column"]:
            self.my_tree.heading(column, text= column)
    
        self.df_rows = df.to_numpy().tolist()
    
        for row in self.df_rows:
            self.my_tree.insert("", "end", values = row)
            self.my_tree.pack()
            self.my_entry.pack(pady= 20)
            self.my_button.pack()
            self.my_button2.pack()
            self.my_button3.pack()
    
    def clear_tree(self):
                self.my_tree.delete(*self.my_tree.get_children())

    def player_search(self):
        name = self.my_entry.get()
        global newDf
        newDf = (df[df["NAME"] == name])
        
        self.clear_tree()

    #Set new treeview
        self.my_tree["column"] = list(newDf.columns)
        self.my_tree["show"] = "headings"

    #loop through coulumn list for headers
        for column in self.my_tree["column"]:
            self.my_tree.heading(column, text= column)

    #put data in treeview
        newDf_rows = newDf.to_numpy().tolist()
        
        for row in newDf_rows:
            self.my_tree.insert("", "end", values = row)
    
    #pack the treeview
        self.my_tree.pack()

    def team_search(self):
            team = self.my_entry.get()
            newDf = (df[df["TEAM"]== team])
        
            self.clear_tree()

    #Set new treeview
            self.my_tree["column"] = list(newDf.columns)
            self.my_tree["show"] = "headings"

    #loop through coulumn list for headers
            for column in self.my_tree["column"]:
                self.my_tree.heading(column, text= column)

    #put data in treeview
            newDf_rows = newDf.to_numpy().tolist()
        
            for row in newDf_rows:
                self.my_tree.insert("", "end", values = row)
    
    #pack the treeview
            self.my_tree.pack()
    
    def position_search(self):
            position = self.my_entry.get()
            newDf = (df[df["POS"]== position])
        
            self.clear_tree()

    #Set new treeview
            self.my_tree["column"] = list(newDf.columns)
            self.my_tree["show"] = "headings"

    #loop through coulumn list for headers
            for column in self.my_tree["column"]:
                self.my_tree.heading(column, text= column)

    #put data in treeview
            newDf_rows = newDf.to_numpy().tolist()
        
            for row in newDf_rows:
                self.my_tree.insert("", "end", values = row)
    
    #pack the treeview
            self.my_tree.pack()
    #add to the treeview        






Hello = Introduction(window2)
UserSelect = User(window1)
window1.mainloop()