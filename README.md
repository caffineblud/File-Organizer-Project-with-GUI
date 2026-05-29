# File Organizer GUI

*A modern dark-themed File Organizer built using Python and Tkinter.*
*This application automatically sorts files into folders based on their file type, helping keep directories clean and organized.*

## Features

- Modern dark mode GUI
- Black and sea green theme
- Automatically organizes files into folders
- Browse folders using file explorer
- Categorizes files by type
- Clean and modular project structure

## File Categories:

**The app automatically sorts files into folders such as:**

- Images
- Documents
- Videos
- Music
- Programs
- Archives
- Others

---

## Technologies Used:

- *Python*
- *Tkinter*
- *os module*
- *shutil module*

---

## Project Structure:
```bash
file-organizer/
│
├── main.py
├── README.md
├── requirements.txt
│
├── core/
│   ├── __init__.py
│   └── organizer.py
│
├── ui/
│   ├── __init__.py
│   └── gui.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
└── test_folder/
```
---

## How It Works:

**Before organizing:**
```bash
Downloads/
├── image.jpg
├── notes.pdf
├── song.mp3
├── movie.mp4
```
**After organizing:**
```bash
Downloads/
├── Images/
│   └── image.jpg
│
├── Documents/
│   └── notes.pdf
│
├── Music/
│   └── song.mp3
│
└── Videos/
    └── movie.mp4
```
---

## Run the Project:
```python
python main.py
```
---

## Installation:

**Clone the repository:**
```bash
git clone <your-repository-link>
```
**Move into the project folder:**
```bash
cd file-organizer
```
## Run the application:
```python

python main.py
```
---

## Future Improvements:

- Drag and drop support
- Duplicate file detection
- File size filters
- Automatic scheduling
- Custom file categories
- Desktop executable version

---

## Author:

***Yash Kr Singh***
