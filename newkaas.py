import tkinter
import tkinter as tk


window = tkinter.Tk()

CheeseLabel = tkinter.Label(text='Is de kaas geel?')
CheeseLabel.pack(fill=tk.X, padx=5, pady=5)

def KaasVraagTrue():
    yesbutton.toggle()
    yesbutton.config(command=KaasVraagTrue2)
    nobutton.config(command=KaasVraagFalse2)
    CheeseLabel['text'] = "Zitten er gaten in?"

def KaasVraagTrue2():
    yesbutton.toggle()
    yesbutton.config(command=lambda:ShowResult('Emmenthalter'))
    nobutton.config(command=lambda:ShowResult("Leerdammer"))
    CheeseLabel['text'] = "Is de kaas belachelijk duur?"

def KaasVraagFalse2():
    nobutton.toggle()
    yesbutton.config(command=lambda:ShowResult('Pamnigiano Reggiano'))
    nobutton.config(command=lambda:ShowResult("Goudse kaas"))
    CheeseLabel['text'] = "Is de kaas zo hard als steen?"

def KaasVraagFalse():
    nobutton.toggle()
    yesbutton.config(command=KaasVraagTrue3)
    nobutton.config(command=KaasVraagFalse3)
    CheeseLabel['text'] = "Heeft de kaas blauwschimmels?"

def KaasVraagTrue3():
    yesbutton.toggle()
    yesbutton.config(command=lambda:ShowResult('Blue de Rochbaron'))
    nobutton.config(command=lambda:ShowResult("Foumme d'Ambert"))
    CheeseLabel['text'] = "Heef de kaas een korst?"

def KaasVraagFalse3():
    nobutton.toggle()
    yesbutton.config(command=lambda:ShowResult('Camebert'))
    nobutton.config(command=lambda:ShowResult("Mozzarella"))
    CheeseLabel['text'] = "Heef de kaas een korst?"

def ShowResult(GivenCheeseVar):
    yesbutton.destroy()
    nobutton.destroy()
    CheeseLabel['text'] = GivenCheeseVar
    None

yesbutton=tk.Checkbutton(window,text='Yes',command=KaasVraagTrue)
yesbutton.pack()

nobutton=tk.Checkbutton(window,text='No',command=KaasVraagFalse)
nobutton.pack()

window.mainloop()