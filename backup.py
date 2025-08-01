import os
import shutil
import zipfile
import time
from datetime import datetime

def create_timestamped_folder(base_name, version):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{base_name}_{timestamp}_v{version}"

def copy_folder(source, destination):
    try:
        shutil.copytree(source, destination)
        return True, None
    except Exception as e:
        return False, str(e)

def zip_folder(source, destination):
    try:
        shutil.make_archive(destination, 'zip', source)
        return True, None
    except Exception as e:
        return False, str(e)

def count_files(folder):
    return sum(len(files) for _, _, files in os.walk(folder))

def log_backup(log_path, entry):
    with open(log_path, 'a') as f:
        f.write(entry + '\n')

def perform_backup(source, destination, version, use_zip=True):
    base_name = os.path.join(destination, "backup")
    backup_folder_name = create_timestamped_folder(base_name, version)
    start_time = time.time()

    if use_zip:
        success, error = zip_folder(source, backup_folder_name)
        backup_folder_name += ".zip"
    else:
        success, error = copy_folder(source, backup_folder_name)

    duration = time.time() - start_time
    num_files = count_files(source)
    status = "Success" if success else f"Failed: {error}"

    log_entry = (
        f"[{datetime.now()}] Backup: {source} -> {backup_folder_name} | "
        f"Status: {status} | Files: {num_files} | Duration: {duration:.2f}s"
    )

    log_backup("backup.log", log_entry)
    print(log_entry)
