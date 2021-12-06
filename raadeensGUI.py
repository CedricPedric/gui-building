import tkinter
import tkinter as tk
import random
from tkinter.messagebox import showinfo, showerror
currentround = 1
won = 0
lost = 0

def Guess(randomnumber):
    global lives
    numbers = [1,2,3,4,5,6,7,8,9,0]
    print(randomnumber)
    numberguessed = entry.get()
    for z in range(len(list(numberguessed))):
        if list(numberguessed)[z] not in str(numbers):
            showerror(title='Warning!',message='Please enter a number.')
            return
    if int(numberguessed) == randomnumber:
        showinfo(title='You Won',message='You guessed the word!')
        BackToMenu(True)
    else:
        Calculate(numberguessed,randomnumber)
        lives -= 1
        liveslabel['text'] = f'Lives: {lives}'
        

def Calculate(numberguessed,randomnumber):
    howclose = int(numberguessed) - randomnumber
    text = ""
    if int(numberguessed) < randomnumber:
        text += 'Hoger'
    elif int(numberguessed) > randomnumber:
        text += 'Lager'

    if howclose >= -20 and howclose <= 20:
        text += ' Je bent heel warm!'
    elif howclose >= -50 and howclose<= 50:
        text += ' Je bent warm'
    howcloselabel['text'] = text

def MakeMainMenu():
    global mainmenulabel,button,button2,won,lost
    mainmenutext = f"""{'-'*30}
Guess a number game!
Als u start is het ronde {currentround}/20.
U heeft {won} gewonnen.
U heeft {lost} veloren.
{'-'*30}
"""
    mainmenulabel = tk.Label(text=mainmenutext)
    mainmenulabel.pack()

    button = tk.Button(text='Start Game',command=ButtonCommand)
    button.pack()
    button2 = tk.Button(text='End Game',command=lambda: GameEnd(won,lost))
    button2.pack()

def ButtonCommand():
    global entry, howcloselabel,lives,liveslabel,label,guessbutton
    lives = 10
    randomnumber = random.randint(0,1000)
    mainmenulabel.destroy()
    button.destroy()
    button2.destroy()

    liveslabel = tk.Label(text=f'Lives: {lives}')
    liveslabel.pack()
    label = tk.Label(text='Raad een getal:')
    label.pack()
    entry = tk.Entry()
    entry.pack()
    howcloselabel = tk.Label(text='Hoger/Lager')
    howcloselabel.pack()
    guessbutton = tk.Button(text='Guess',command=lambda: [Guess(randomnumber),CheckLives()])
    guessbutton.pack()

def CheckLives():
    if lives <= 0:
        BackToMenu(False)

def GameEnd(won,lost):
    showinfo(
        title='The End', message=f'The Game Has Ended \nYou Won: {won} \nYou Lost: {lost} '
    )
    window.destroy()

def BackToMenu(boolean):
    global won,lost,currentround
    if boolean:
        won += 1
    else:
        lost += 1
    currentround += 1
    if currentround >= 20:
        GameEnd(won,lost)
        None
    liveslabel.destroy()
    label.destroy()
    entry.destroy()
    howcloselabel.destroy()
    guessbutton.destroy()

    MakeMainMenu()

window = tkinter.Tk()
MakeMainMenu()
window.mainloop()