from tkinter import *

top = Tk()
playlist = []


    
def printList():
    print(playlist)
    
def exportList ():
    with open('tst.txt', 'w') as f:
        for item in list:
         f.write("is/n" item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()
        
def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "week 1", bg= "white", command = week1)
    B1Main.grid(column= 0, row = 2)
    B2Main = Button(text = "Week2", bg = "white")
    B2Main.grid(column= 0, row = 3)
    B3Main = Button(text = "week3", bg = "white")
    B3Main.grid(column= 0, row= 4)

def week1():
    clearWindow[]
    def results():
        result = E1.get()
        playlist.append(result)
        E1.delete(0, END)
    
    #This is a label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row= 1)

    #This is an Entry widget 
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row= 2)

    #This is a Button widget
    B1 = Button(text= "   Playlist Generator  ", bg="pink", command= results )
    B1.grid(column= 1, row= 2)

    B2 = Button(text= " print ", bg = "Light blue" command= results)
    B2.grid(column= 2, row= 2)

    B3 = Button(text= "Export List", bg = "purple", command = exportList)
    B3.grid(column = 0, row = 3)

    Bexit = Button(text= "Main Menu", bg = "sunshine yellow", command = mainMenu)
    Bexit.grid(column = 1, row = 3)

def week2():
    clearWindow()
    B1week2 = Button()
    L1Week2 = Label()
    L2Week2 = Label()
    L3Week3 = Label()
    E1Week2 = Entry()
    E1Week2 = Entry()



if __name__ == "__main__":
    mainMenu()
top.mainloop()
 
