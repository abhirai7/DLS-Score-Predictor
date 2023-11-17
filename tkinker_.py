from tkinter import *


class Tkinter_:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("DLS Calculator")
        self.root.geometry("300x250")
        self.root.resizable(width=False, height=False)
        self.root.configure(background='#ffc38f')
        label = Label(self.root, text ="DLS Calculator", font="Arial 14", bg="#c4a9fb", fg="black", width=15, height=2)
        label.pack(anchor="center", pady=20)
    
    def _setvalues(self):
        self.score = Label(self.root, text ="Score : ", font="Arial 11", bg="#ffc38f", fg="black")
        self.score.place(anchor="w",relx=0.1,rely=0.4)
        self.score_input = Entry(self.root, width=20)
        wicket_text = Label(self.root, text ="Wickets : ", font="Arial 11", bg="#ffc38f", fg="black")
        wicket_text.place(anchor="w",relx=0.1,rely=0.5)
        self.wicket_input = Entry(self.root, width=20)
        over_left = label = Label(self.root, text ="Overs Left: ", font="Arial 11", bg="#ffc38f", fg="black")
        over_left.place(anchor="w",relx=0.1,rely=0.6)
        self.over_input = Entry(self.root, width=20)
        self.submit= Button(self.root, text="Submit", command=self.sub,width=10, height=1, bg="white", fg="black").place(anchor="center",relx=0.5,rely=0.8)
        self.wicket_input.place(anchor="e",relx=0.8,rely=0.5)
        self.over_input.place(anchor="e",relx=0.8,rely=0.6)
        self.score_input.place(anchor="e",relx=0.8,rely=0.4)
        self.root.mainloop()


    def sub(self):
        overs=self.over_input.get()
        wickets=self.wicket_input.get()
        self.sc = self.score_input.get()
        
        self.overs=int(overs)
        self.wickets=int(wickets)

    def display(self,value):
        self.label = Label(self.root, text =value)
        self.label.pack(anchor="center", pady=20)


    def _return(self):
        return [[self.overs,self.wickets]]
    
    
    def _score(self):
        return int(self.sc)
