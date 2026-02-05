import os
import shutil

downloads_path = os.path.expanduser("~/Downloads")
folders = ["Images", "Documents", "Installers"]

extensions = {
    ".jpg": "Images", ".png": "Images", ".jpeg": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".dmg": "Installers", ".pkg": "Installers", ".zip": "Installers"
}

for filename in os.listdir(downloads_path):
    ext = os.path.splitext(filename)[1].lower()
    if ext in extensions:
        dest_folder = os.path.join(downloads_path, extensions[ext])
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(os.path.join(downloads_path, filename), os.path.join(dest_folder, filename))
