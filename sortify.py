import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Mapping of folder names to file extensions
file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    "Music": ['.mp3', '.wav', '.aac'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz'],
    "Executables": ['.exe', '.msi', '.apk'],
    "Code": ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css'],
    "Others": []  # Files that don't match any of the above
}

def organize_folder(path):
    if not os.path.exists(path):
        messagebox.showerror("Error", "Invalid folder path!")
        return

    files_moved = 0

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            moved = False
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            for folder, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    files_moved += 1
                    moved = True
                    break

            if not moved:
                dest_folder = os.path.join(path, "Others")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                files_moved += 1

    messagebox.showinfo("Done", f"Organized {files_moved} files successfully!")

def select_folder_and_organize():
    folder_path = filedialog.askdirectory(title="Select a Folder to Organize")
    if folder_path:
        organize_folder(folder_path)

# GUI
def main():
    root = tk.Tk()
    root.title("Sortify - File Organizer")
    root.geometry("800x400")
    root.configure(bg="#fdf6f0")

    title = tk.Label(root, text="Sortify", font=("Helvetica", 36, "bold"), bg="#fdf6f0", fg="#d63384")
    title.pack(pady=20)

    organize_btn = tk.Button(
        root,
        text="Select Folder to Organize",
        command=select_folder_and_organize,
        font=("Helvetica", 18),
        bg="#d63384",
        fg="black",
        padx=10,
        pady=10
    )
    organize_btn.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
