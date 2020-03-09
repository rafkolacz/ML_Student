# import ML_Student_Model as model
import tkinter as tk

x = [11,11,2,0,3]
#value = model.calculator(elo)
#print(value)
'''
win = tk.Tk()
win.geometry("324x100")
win.resizable(0, 0)
win.title("Will U pass your final exam?")

frame = tk.Frame(win)
frame.pack()

tk.Label(frame, text = "sdds").pack()


def btn_calc(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)

'''


class MainWindow(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.nazwa_label = tk.Label(self, text="Input G1, G2 points, hours of studytime, number of failures and hours of absence:")
        self.nazwa_label.pack(fill=tk.X)

        self.add_btn = tk.Button(self, text="Input data", command=self.input_data())
        self.add_btn.pack(fill=tk.X)

    def input_data(self):
            t = tk.Toplevel(self)
            t.wm_title("Adding item #%s")

            nazwa_label = tk.Label(t, text="Nazwa:")
            nazwa_txt = tk.Entry(t, width=10)
            nazwa_label.grid(column=0, row=0, sticky=tk.W)
            nazwa_txt.grid(column=1, row=0)



root = tk.Tk()
window = MainWindow(root)
window.pack(side="top", fill="both", expand=True)
root.title("Will U pass your final exam?")
root.mainloop()

