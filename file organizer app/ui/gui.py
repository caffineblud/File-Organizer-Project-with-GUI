import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from core.organizer import organize_files

# ---------- COLORS ----------

BG_COLOR = "#0f0f0f"
CARD_COLOR = "#1a1a1a"
TEXT_COLOR = "#d7ffd9"
ACCENT_COLOR = "#2ecc71"
BUTTON_TEXT = "#000000"


def browse_folder():

    folder_selected = filedialog.askdirectory()

    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_selected)


def start_organizing():

    folder_path = folder_path_entry.get()

    if folder_path.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please select a folder."
        )
        return

    result = organize_files(folder_path)

    messagebox.showinfo(
        "Result",
        result
    )


def run_gui():

    global folder_path_entry

    root = tk.Tk()

    root.title("File Organizer")
    root.geometry("550x320")
    root.resizable(False, False)

    root.configure(bg=BG_COLOR)

    # ---------- TITLE ----------

    title_label = tk.Label(
        root,
        text="FILE ORGANIZER",
        font=("Arial", 24, "bold"),
        bg=BG_COLOR,
        fg=ACCENT_COLOR
    )

    title_label.pack(pady=25)

    # ---------- FRAME ----------

    main_frame = tk.Frame(
        root,
        bg=CARD_COLOR,
        padx=20,
        pady=20
    )

    main_frame.pack(pady=10)

    # ---------- ENTRY ----------

    folder_path_entry = tk.Entry(
        main_frame,
        font=("Arial", 12),
        width=42,
        bg="#262626",
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief="flat"
    )

    folder_path_entry.pack(pady=10, ipady=8)

    # ---------- BROWSE BUTTON ----------

    browse_button = tk.Button(
        main_frame,
        text="Browse Folder",
        font=("Arial", 11, "bold"),
        width=18,
        bg=ACCENT_COLOR,
        fg=BUTTON_TEXT,
        relief="flat",
        cursor="hand2",
        command=browse_folder
    )

    browse_button.pack(pady=8)

    # ---------- ORGANIZE BUTTON ----------

    organize_button = tk.Button(
        main_frame,
        text="Organize Files",
        font=("Arial", 11, "bold"),
        width=18,
        bg=ACCENT_COLOR,
        fg=BUTTON_TEXT,
        relief="flat",
        cursor="hand2",
        command=start_organizing
    )

    organize_button.pack(pady=8)

    # ---------- INFO ----------

    info_label = tk.Label(
        root,
        text="Automatically sorts files into folders",
        font=("Arial", 10),
        bg=BG_COLOR,
        fg="#8bcf9b"
    )

    info_label.pack(pady=15)

    root.mainloop()