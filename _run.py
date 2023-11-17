import _main as ml
from tkinker_ import *
from tkinter import *

class display_:
    def __init__(self,value) -> None:
        self.dls_score = value
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.title("DLS Score")
        self.root.configure(background="#c9ffe5")
        self.root.geometry("300x250")
        lab = Label(self.root,text=f"DLS SCORE : ",font="Carrabian", bg="#20b2aa", fg="black", width=15, height=2)
        lab.place(anchor="center",rely=0.3,relx=0.5)

    def _final(self):
        label2 = Label(self.root,text = f"{self.dls_score}",font=("Carrabian 35"), bg="#c9ffe5", fg="#800080", width=15,height=2)
        label2.place(anchor="center",rely=0.6,relx=0.5)
        self.root.mainloop()

if __name__ == "__main__":
    Tkin_obj=Tkinter_()
    ml_obj = ml.main_fit()
    Tkin_obj._setvalues()
    ml_obj.test_train()
    ml_obj.regressor()
    dls_score = ml_obj.predict(Tkin_obj._score(),Tkin_obj._return())
    final_obj = display_(int(dls_score))
    final_obj._final()
