from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip
import os


def convert_to_mp3(file_path, output_folder, progress_var):
    clip = VideoFileClip(file_path)
    file_name = os.path.basename(file_path).replace(".avi", ".mp3")
    output_path = os.path.join(output_folder, file_name)
    clip.audio.write_audiofile(output_path, progress_bar=progress_var)


def convert_selected_files(output_folder, progress_bar):
    input_files = input_file_list.curselection()
    
    for file_index in input_files:
        file_path = input_file_list.get(file_index)
        convert_to_mp3(file_path, output_folder, progress_bar)


def choose_files():
    # zobrazit dialog pro výběr souborů
    file_types = (("Video soubory", "*.mp4;*.avi;*.mov"), ("Všechny soubory", "*.*"))
    chosen_files = filedialog.askopenfilenames(title="Vyberte soubory", filetypes=file_types)
    
    # vypsat jména vybraných souborů v ListBoxu
    input_file_list.delete(0, END)
    for file_path in chosen_files:
        file_name = os.path.basename(file_path)
        input_file_list.insert(END, file_path)


def choose_folder():
    output_folder = filedialog.askdirectory(title="Vyberte složku pro výstup")
    output_folder_entry.delete(0, END)
    output_folder_entry.insert(END, output_folder)


def start_conversion():
    output_folder = output_folder_entry.get()
    if not output_folder:
        messagebox.showerror("Chyba", "Vyberte výstupní složku.")
        return
    
    if not input_file_list.curselection():
        messagebox.showerror("Chyba", "Vyberte alespoň jeden soubor k převodu.")
        return
    
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
    progress_bar.grid(row=5, column=1, padx=5, pady=5)
    
    progress_bar["maximum"] = len(input_file_list.curselection())
    progress_bar["value"] = 0
    
    for i in range(len(input_file_list.curselection())):
        progress_bar["value"] += 1
        root.update_idletasks()
        convert_selected_files(output_folder, progress_bar)

    progress_bar.destroy()
    messagebox.showinfo("Hotovo", "Převod dokončen.")


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
output_folder_button.grid(row=1,column=2, padx=5, pady=5)

input_file_list = Listbox(root, selectmode="multiple")
input_file_list.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

convert_button = Button(root, text="Převést", command=start_conversion)
convert_button.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()