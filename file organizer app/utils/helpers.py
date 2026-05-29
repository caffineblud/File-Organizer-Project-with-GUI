import os


FILE_CATEGORIES = {

    "Images": [".png", ".jpg", ".jpeg", ".gif"],

    "Documents": [".pdf", ".docx", ".txt"],

    "Videos": [".mp4", ".mkv", ".mov"],

    "Music": [".mp3", ".wav"],

    "Programs": [".py", ".java", ".cpp"],

    "Archives": [".zip", ".rar"]
}


def get_category(filename):

    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:
            return category

    return "Others"