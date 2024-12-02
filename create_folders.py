import os
import shutil

def copy_and_rename_template(template_folder, dest_folder_prefix, start, end):
    for i in range(start, end + 1):
        folder_name = f"{dest_folder_prefix}{i:02d}_"
        dest_folder = os.path.join(os.path.dirname(template_folder), folder_name)

        if not os.path.exists(dest_folder):
            shutil.copytree(template_folder, dest_folder)
            rename_files_in_folder(dest_folder, 'XX', f"{i:02d}")

def rename_files_in_folder(folder, old_pattern, new_pattern):
    for root, _, files in os.walk(folder):
        for file_name in files:
            if old_pattern in file_name:
                new_file_name = file_name.replace(old_pattern, new_pattern)
                os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))

if __name__ == "__main__":
    template_folder = "Day_XX_"  # Path to the template folder
    dest_folder_prefix = "Day_"
    start_index = 3
    end_index = 25

    copy_and_rename_template(template_folder, dest_folder_prefix, start_index, end_index)
