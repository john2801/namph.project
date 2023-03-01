from tkinter import *


def transfer():
    if listbox.get(ACTIVE) == "Cat":
        age = int(input_age_animal.get())
        age_in_human = (age - 2) * 4 + 24
        result.config(text=f"{age_in_human}")
    else:
        age = int(input_age_animal.get())
        age_in_human = age * 7
        result.config(text=f"{age_in_human}")


FONT = ("Arial", 10, "normal")
screen = Tk()
screen.title("Transfer age from pets to human")
screen.minsize(500, 500)
screen.config(padx=20, pady=20)
title = Label(text="What is your pet's 'human age'?", font=FONT)
title.grid(column=4, row=1)
title.config(padx=10, pady=10)

animal_age = Label(text="Pet age", font=FONT)
animal_age.grid(column=2, row=3)
to_human = Label(text="To Human")
to_human.grid(column=2, row=4)
result = Label(text=0)
result.grid(column=3, row=4)


input_age_animal = Entry(width=10)
input_age_animal.grid(column=3, row=3)
listbox = Listbox(height=2)
animals = ["Dog", "Cat"]
for item in animals:
    listbox.insert(animals.index(item), item)

listbox.grid(column=5, row=4)
chose_animal = Label(text="Choose your animal")
chose_animal.grid(column=5, row=3)

transfer = Button(text="Transfer", font=FONT, command=transfer)
transfer.grid(column=3, row=5)

screen.mainloop()
