import os
from tkinter import filedialog
from tkinter import *

def choose_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, END)
    input_folder_entry.insert(0, input_folder)

def choose_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, END)
    output_folder_entry.insert(0, output_folder)


def print_folders():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()

    print("Vstupní složka:", input_folder)
    print("Výstupní složka:", output_folder)

    pass

# def print_folders():
#   input_folder = input_folder_entry.get()
#   output_folder = output_folder_entry.get()
#
#   print("Vstupní složka:", input_folder)
#   print("Výstupní složka:", output_folder)
#
#   pass

# Vytvoření GUI
root = Tk()

# Vytvoření prvků GUI
input_folder_label = Label(root, text="Vstupní složka:")
input_folder_entry = Entry(root, width=50)
input_folder_button = Button(root, text="Vybrat složku", command=choose_input_folder)

output_folder_label = Label(root, text="Výstupní složka:")
output_folder_entry = Entry(root, width=50)
output_folder_button = Button(root, text="Vybrat složku", command=choose_output_folder)

convert_button = Button(root, text="Konvertovat", command=print_folders)

# Umístění prvků GUI
input_folder_label.grid(row=0, column=0)
input_folder_entry.grid(row=0, column=1)
input_folder_button.grid(row=0, column=2)

output_folder_label.grid(row=1, column=0)
output_folder_entry.grid(row=1, column=1)
output_folder_button.grid(row=1, column=2)

convert_button.grid(row=2, column=1)

# Spuštění GUI
root.mainloop()