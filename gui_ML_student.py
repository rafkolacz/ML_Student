import ML_Student_Model as model
from tkinter import *

root = Tk()
root.title("G3 Calculator")
root.resizable(False, False)
root.geometry("300x200+900+400")

def calc():
    temp = []
    temp.append(int(G1.get()))
    temp.append(int(G2.get()))
    temp.append(int(study.get()))
    temp.append(int(fails.get()))
    temp.append(int(ab.get()))

    G3 = model.calculator(temp)
    myLabel3 = Label(root, text="Your score:")
    myLabel3.grid(row=9, column=1)
    myLabel4 = Label(root, text=G3)
    myLabel4.grid(row=9, column=2)


myLabel1 = Label(root, text=" Hello, welcome in G3 calculator!")
myLabel1.grid(row=1, column=2)
myLabel2 = Label(root,text = "Please input data:")
myLabel2.grid(row=2, column=1)

g1Label = Label(root,text = "G1")
g1Label.grid(row=3, column=1)
g2Label = Label(root,text = "G2")
g2Label.grid(row=4, column=1)
studyLabel = Label(root,text = "Study time")
studyLabel.grid(row=5, column=1)
failLabel = Label(root,text = "Failures")
failLabel.grid(row=6, column=1)
abLabel = Label(root,text = "Absences")
abLabel.grid(row=7, column=1)

G1 = Entry(root)
G1.grid(row=3, column=2)
G1.insert(0, 0)

G2 = Entry(root)
G2.grid(row=4, column=2)
G2.insert(0, 0)

study = Entry(root)
study.grid(row=5, column=2)
study.insert(0, 0)

fails = Entry(root)
fails.grid(row=6, column=2)
fails.insert(0, 0)

ab = Entry(root)
ab.grid(row=7, column=2)
ab.insert(0, 0)


myButton = Button(root, text="Calculate", command=calc)
myButton.grid(row=8, column=2)
root.mainloop()



