import tkinter
import tkinter as tk
from tkinter import Spinbox, ttk

def DestroyTheWidgets():
    label.destroy()
    pizza_cb.destroy()
    button.destroy()

def DestroyWidgets2():
    label.destroy()
    button.destroy()
    spin_box.destroy()

def MakeHowManyPizza():
    global current_value,spin_box,button
    size = selected_pizza.get()
    DestroyTheWidgets()
    label = tkinter.Label(text="Hoeveel pizza's wilt u?")
    label.pack()
    current_value = tk.StringVar(value=0)
    spin_box = ttk.Spinbox(window,from_=0,to=30,textvariable=current_value,wrap=True)
    spin_box.pack()
    button = tkinter.Button(text='Next',command=lambda: ShowPrize(size))
    button.pack()
    None
def ShowPrize(size):
    amount = current_value.get()
    DestroyWidgets2()
    if size == 'Small':
        amountsize = 6.99
    elif size == 'Medium':
        amountsize = 9.99
    elif size == 'Large':
        amountsize = 14.99
    price = int(amount) * amountsize
    label = tk.Label(text=f"Je hebt {amount} {size} pizza's besteld \nPrijs: {amount} x {amountsize} = {round(price,2)}  \nDe bestelling is onderweg!")
    label.pack()

window= tkinter.Tk()
textprizesandsizes = """--------------------------------------------------- 
  Kies welke afmeting pizza u wilt:\n
Small:€6.99\n
Medium:€9.99\n
Large:€14.99\n                   
---------------------------------------------------"""
label = tkinter.Label(text=textprizesandsizes)
label.pack()

sizes = ['Small','Medium','Large']
selected_pizza = tk.StringVar()
pizza_cb = ttk.Combobox(window, textvariable=selected_pizza)
pizza_cb['values'] = sizes
pizza_cb['state'] = 'readonly'
pizza_cb.pack(fill=tk.X, padx=5, pady=5)

button = tk.Button(text='Next',command=MakeHowManyPizza)
button.pack()


window.mainloop()