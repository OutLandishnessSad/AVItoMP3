from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
import os


def convert_to_mp3(file_path, output_folder):
    clip = VideoFileClip(file_path)
    file_name = os.path.basename(file_path).replace(".avi", ".mp3")
    output_path = os.path.join(output_folder, file_name)
    clip.audio.write_audiofile(output_path)


def convert_selected_files(output_folder):
    input_files = input_file_list.curselection()
    
    for file_index in input_files:
        file_path = input_file_list.get(file_index)
        print(file_path)
        convert_to_mp3(file_path, output_folder)


def choose_files():
    # zobrazit dialog pro výběr souborů
    file_types = (("Video soubory", "*.mp4;*.avi;*.mov"), ("Všechny soubory", "*.*"))
    chosen_files = filedialog.askopenfilenames(title="Vyberte soubory", filetypes=file_types)
    
    # vypsat jména vybraných souborů v ListBoxu
    input_file_list.delete(0, END)
    for file_path in chosen_files:
        file_name = os.path.basename(file_path)
        input_file_list.insert(END, file_path)

def convert_selected_files(output_folder):
    input_files = input_file_list.curselection()
    
    # nastavit indeterminantní mód načítacího pruhu
    progressbar.start()

    for file_index in input_files:
        file_path = input_file_list.get(file_index)
        convert_to_mp3(file_path, output_folder)
        
    # ukončit načítací pruh
    progressbar.stop()


def choose_folder():
    output_folder = filedialog.askdirectory(title="Vyberte složku pro výstup")
    output_folder_entry.delete(0, END)
    output_folder_entry.insert(END, output_folder)


root = Tk()
root.title("Konvertor AVI do MP3")

input_folder_label = Label(root, text="Vstupní složka:")
input_folder_label.grid(row=0, column=0, padx=5, pady=5)

input_folder_entry = Entry(root)
input_folder_entry.grid(row=0, column=1, padx=5, pady=5)

input_folder_button = Button(root, text="Browse", command=choose_files)
input_folder_button.grid(row=0, column=2, padx=5, pady=5)

output_folder_label = Label(root, text="Výstupní složka:")
output_folder_label.grid(row=1, column=0, padx=5, pady=5)

output_folder_entry = Entry(root)
output_folder_entry.grid(row=1, column=1, padx=5, pady=5)

output_folder_button = Button(root, text="Browse", command=choose_folder)
output_folder_button.grid(row=1, column=2, padx=5, pady=5)

input_file_label = Label(root, text="Vyberte soubory k převodu:")
input_file_label.grid(row=2, column=0, padx=5, pady=5)

input_file_list = Listbox(root, selectmode=MULTIPLE)
input_file_list.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

convert_button = Button(root, text="Převést", command=lambda: convert_selected_files(output_folder_entry.get()))
convert_button.grid(row=4, column=0, padx=5, pady=5)

progressbar = ttk.Progressbar(root, orient='horizontal', mode='indeterminate')
progressbar.grid(row=5, column=0, columnspan=3, padx=5, pady=5)




root.mainloop()
