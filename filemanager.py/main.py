import os
import shutil


direktori_awal = "C:\\Users\\Adrian\\Downloads"
direktori_target = "E:\\File manager Python (Target)"

def organize_file(source_dir, dest_dir):
    # Membuat daftar semua file dalam direktori sumber
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    for file in files:
        # Mendapatkan ekstensi file
        file_extension = file.split('.')[-1]
        
        # Membuat folder berdasarkan ekstensi file di direktori tujuan
        folder_path = os.path.join(dest_dir, file_extension.upper())  # Folder dengan nama ekstensi
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Memindahkan file ke folder yang sesuai
        shutil.move(os.path.join(source_dir, file), os.path.join(folder_path, file))
        print(f"Memindahkan {file} ke {folder_path}")

# Memanggil fungsi
organize_file(direktori_awal, direktori_target)
