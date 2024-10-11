import os
import yaml
import pandas as pd

# Fungsi untuk membaca file DVC
def read_dvc_file(file_path):
    with open(file_path, 'r') as file:
        dvc_content = yaml.safe_load(file)
    return dvc_content

# Fungsi untuk membaca file dalam direktori
def read_files_in_directory(directory_path):
    files_data = {}
    
    # List all files in the specified directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            # Read different file types accordingly
            if filename.endswith('.csv'):
                files_data[filename] = pd.read_csv(file_path)
            elif filename.endswith('.txt'):
                with open(file_path, 'r') as file:
                    files_data[filename] = file.read()
            # Add more file types as needed

    return files_data

# Contoh penggunaan
dvc_file_path = 'Dataset.dvc'  # Path ke file DVC Anda
dvc_data = read_dvc_file(dvc_file_path)

# Ambil path direktori dari konten DVC
output_directory = dvc_data['outs'][0]['path']  # Mengambil path dari output
print(f"Output directory path: {output_directory}")  # Debugging line

# Get absolute path
output_directory = os.path.abspath(output_directory)
print(f"Absolute output directory path: {output_directory}")  # Debugging line

# Baca semua file dalam direktori
if os.path.exists(output_directory):
    data_files = read_files_in_directory(output_directory)

    # Cetak isi file yang telah dibaca
    for file_name, content in data_files.items():
        print(f"Isi dari {file_name}:")
        print(content)
else:
    print(f"Directory '{output_directory}' does not exist.")
