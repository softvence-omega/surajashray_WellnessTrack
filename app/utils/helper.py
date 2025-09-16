import shutil
import os



def delete_file(file_path):
    if os.path.exists(file_path):
        shutil.rmtree(file_path)