import zipfile
import os
import shutil

def zip_folder(folder_path, output_path):
    if not os.path.exists("./purge"):
        os.makedirs("./purge")
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, os.path.dirname(folder_path))
                zipf.write(abs_path, rel_path)
    shutil.rmtree(folder_to_archive)

# Example usage
folder_to_archive = './messagelogs'
output_zip_file = './purge/message-log-archive.zip'
zip_folder(folder_to_archive, output_zip_file)
