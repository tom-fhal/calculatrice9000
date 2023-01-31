from tkinter import *
import tkinter as tk
import tkinter as ttk
file = open("historique.txt", "a+")
file.close()
root = tk.Tk()
root.title('Calculator')
root.geometry("400x400")

frame_button = Frame(root)
frame_button.grid(pady=28)
operations = StringVar()
toshow = StringVar()  



oneBouton = ttk.Button(frame_button, text="1", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                      command=lambda: calculation(1))
oneBouton.grid(row=2, column=0, padx=2, pady=3)

twoBouton = ttk.Button(frame_button, text="2", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: calculation(2))
twoBouton.grid(row=2, column=1, padx=2, pady=3)

treeBouton = ttk.Button(frame_button, text="3", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                         command=lambda: calculation(3))
treeBouton.grid(row=2, column=2, padx=2, pady=3)

plusBouton = ttk.Button(frame_button, text="+", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: calculation('+'))
plusBouton.grid(row=2, column=3, padx=2, pady=3)

################################################################################
################################################################################
################################################################################

fourBouton = ttk.Button(frame_button, text="4", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                          command=lambda: calculation(4))

fourBouton.grid(row=3, column=0, padx=2, pady=3)

fiveBouton = ttk.Button(frame_button, text="5", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: calculation(5))
fiveBouton.grid(row=3, column=1, padx=2, pady=3)

sixBouton = ttk.Button(frame_button, text="6", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                       command=lambda: calculation(6))

sixBouton.grid(row=3, column=2, padx=2, pady=3)

lessBouton = ttk.Button(frame_button, text="-", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                         command=lambda: calculation('-'))
lessBouton.grid(row=3, column=3, padx=2, pady=3)
###################################################################################
###################################################################################
##################################################################################

sevenBouton = ttk.Button(frame_button, text="7", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: calculation(7))

sevenBouton.grid(row=4, column=0, padx=2, pady=3)

heightBouton = ttk.Button(frame_button, text="8", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: calculation(8))

heightBouton.grid(row=4, column=1, padx=2, pady=3)

nineBouton = ttk.Button(frame_button, text="9", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: calculation(9))

nineBouton.grid(row=4, column=2, padx=2, pady=3)
###############################################################################################################################
##############################################################################################################################
zeroButton = ttk.Button(frame_button, text="0", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: calculation(0))
zeroButton.grid(row=5, column=0, padx=2, pady=3)
################################################################################################################################
################################################################################################################################
clearButton = ttk.Button(frame_button, text="C", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                         command=lambda: erase())
clearButton.grid(row=5, column=1, padx=2, pady=3)

equalButton = ttk.Button(frame_button, text="=", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                         command=lambda: equal())
equalButton.grid(row=5, column=2, padx=2, pady=3)

multButton = ttk.Button(frame_button, text="x", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: calculation('*'))
multButton.grid(row=4, column=3, padx=2, pady=3)

dotButton = ttk.Button(frame_button, text=".", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                       command=lambda: calculation('.'))
dotButton.grid(row=6, column=3, padx=2, pady=3)

divideButton = ttk.Button(frame_button, text="/", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                          command=lambda: calculation('/'))
divideButton.grid(row=5, column=3, padx=2, pady=3)

powerButton = ttk.Button(frame_button, text="²", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                             command=lambda: calculation('**2'))
powerButton.grid(row=6, column=1, padx=2, pady=3)

squarerootButton = ttk.Button(frame_button, text="√x", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                              command=lambda: calculation('**0.5'))
squarerootButton.grid(row=6, column=2, padx=2, pady=3)

historyButton=ttk.Button(frame_button, text="HIST", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                              command=lambda: openNewWindow())
historyButton.grid(row=7, column=2, padx=2, pady=3)



screenframe = Frame(root, width=100, height=50, bd=0)
screenframe.place(x=0)

screenresult = Entry(screenframe, font='Helvetica 15',width=40 ,textvariable=operations,bg="#eee", fg="black", bd=0,
                    justify=RIGHT)
screenresult.grid(row=0, column=0)


def openNewWindow():
    master = tk.Tk()
    master.title("New Window")
    file = open("historique.txt", "r")
    histo = file.read()
    file.close()
    n = 1
    for a in histo:
        if a == "\n":
            n += 1
    
    master.geometry("300x"+str(50 + 25*n))
    canvas= Canvas(master, width= 1000, height= 750, bg="SpringGreen2")
    canvas.create_text(100, 12*n, text=str(histo), fill="black", font=('Helvetica 15 bold'))
    canvas.grid(row = 1, column = 1)
    
    erasebutton = ttk.Button(master, text="erase", pady=10, padx=20, font="Helvetica 15", bg="white", fg="black",
                        command=lambda: eraseButton())
    erasebutton.grid(row=0,column=0)

def calculation(item):
    global expression
    expression = expression + str(item)
    operations.set(expression)
    toshow.set(operations)
    
def eraseButton():
    file = open("historique.txt","w")
    file.write("")
    file.close()



def erase():
    global expression
    expression = ""
    operations.set("")



def equal():
    global expression
    result = str(eval(expression))  
    operations.set(result)
    file = open("historique.txt","a")
    file.write(expression+" = "+str(eval(expression))+"\n")
    file.close()
    expression = ""
    



expression = ""

root.mainloop()
