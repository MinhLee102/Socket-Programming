import tkinter as tk
from client import requestServer

#Create main screen
screen = tk.Tk()
screen.title("Conversion")
screen.geometry('800x400')

clientInput = tk.StringVar()
outputLabel = tk.Label(screen, text="Output: ", font=('arial',15, 'normal'))
outputLabel.grid(column=0, row=3)

def enter():
    input = clientInput.get()
    result = requestServer(input)
    print(input)
    outputLabel.config(text="Output: " + result)
    


label = tk.Label(screen, text="Server", font=('arial',30, 'bold'))
label.grid(column= 0, row= 0)

entry = tk.Entry(screen, textvariable=clientInput, font=('arial',15, 'normal'))
entry.grid(column=0, row= 1)

enter_button = tk.Button(screen, text= "Enter", command= enter)
enter_button.grid(column=0, row=2)

screen.mainloop()