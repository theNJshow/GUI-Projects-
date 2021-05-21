from tkinter import *
import random

top = Tk()
playlist = []
myRolls = []
dieType = []
    
def printList():
    print(playlist)

def exportList():
    with open('playlist.txt', 'w') as f:
        for item in playlist:
            f.write( "%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column = 0, row = 2)
    B2Main = Button(text = "Week 2", bg = "white", command = week2)
    B2Main.grid(column = 0, row = 3)
    B3Main = Button(text = "Week 3", bg = "white")
    B3Main.grid(column = 0, row = 4)

def week1():
    clearWindow()
    def results():
        result = E1.get()
        playlist.append(result)
        E1.delete(0, END)
    
    # This is a Label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row= 1)

    #This is an Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row= 2)

    #This is a Button widget
    B1 = Button(text = " + ", bg = "white", command = results)
    B1.grid(column = 1, row= 2)

    B2 = Button(text = " Print ", bg = "light blue", command = printList)
    B2.grid(column = 2, row = 2)

    B3 = Button(text= "Export List", bg = "#B4FFCD", command = exportList)
    B3.grid(column = 0, row = 3)

    Bexit = Button(text= "Main Menu", bg = "light grey", command = mainMenu)
    Bexit.grid(column = 1, row = 3)

def week2():
    def rollDice():
        #update variable data
        dieType = E2Week2.get()
        rollTimes = E1Week2.get()
        #clear window AFTER updating variables
        clearWindow()
        #roll the dice
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        #build the results window
        L4Week2 = Label(top, text= "Here's your rolls!")
        L4Week2.grid(column = 0, row = 1)
        
        L5Week2 = Label(top, text= "{}".format(myRolls))
        L5Week2.grid(column = 0, row = 2)
        
        B2Week2 = Button(text= "Main Menu", bg="yellow", command= mainMenu)
        B2Week2.grid(column = 0, row = 3)
    
    clearWindow()
    B1Week2 = Button(text= "Roll em!", bg="yellow")
    B1Week2.grid(column= 2, row=4)
    
    L1Week2 = Label(top, text= "Dice Roller App")
    L1Week2.grid(column= 2, row=1)
    
    L2Week2 = Label(top, text= "# of Rolls")
    L2Week2.grid(column= 0, row=2)
    
    L3Week2 = Label(top, text= "# of sides")
    L3Week2.grid(column= 3, row=2)
    
    E1Week2 = Entry(top, bd = 5)
    E1Week2.grid(column= 0, row=3)
    
    E2Week2 = Entry(top, bd = 5)
    E2Week2.grid(column= 3, row=3)




def week3():

B3 = linearlist(text= "hello lets make a list")


        #the new code
        import linearlist
        print("hello! lets make a list!")
        print("""1. Add some words,
2. Return some words
3. print contents of list  """) 
        
if __name__ == "__main__":
    mainMenu()
    top.mainloop()
    
