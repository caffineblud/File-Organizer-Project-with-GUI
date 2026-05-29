import os
import shutil

from utils.helpers import get_category


def organize_files(folder_path):

    if not os.path.exists(folder_path):
        return "Folder does not exist."

    files = os.listdir(folder_path)

    moved_files = 0

    for file in files:

        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        category = get_category(file)

        category_folder = os.path.join(folder_path, category)

        os.makedirs(category_folder, exist_ok=True)

        destination = os.path.join(category_folder, file)

        shutil.move(file_path, destination)

        moved_files += 1

    return f"{moved_files} files organized successfully!"