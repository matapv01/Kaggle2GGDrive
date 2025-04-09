# -*- coding: utf-8 -*-
# Kaggle Dataset Downloader and Extractor

# Step 1: Upload your kaggle.json credentials (Skip if dataset is public)
from google.colab import files

# Upload kaggle.json
files.upload()

# Step 2: Move kaggle.json to the appropriate directory and set permissions
import os
import shutil

# Create the .kaggle directory if it does not exist
os.makedirs("/root/.kaggle", exist_ok=True)

# Move kaggle.json to the .kaggle folder
shutil.move("kaggle.json", "/root/.kaggle/kaggle.json")

# Set permissions for the kaggle.json file
os.chmod("/root/.kaggle/kaggle.json", 600)

# Step 3: Download the Dataset
# Replace 'username/dataset-name' with the actual Kaggle dataset identifier
dataset_path = "username/dataset-name"  # Example: 'zynicide/wine-reviews'
!kaggle datasets download -d {dataset_path}

# Step 4: Unzip the downloaded Dataset
import zipfile

# Replace 'dataset-name.zip' with your actual downloaded zip filename
zip_filename = "dataset-name.zip"  # Example: 'wine-reviews.zip'
extract_dir = "dataset"  # Destination directory for extracted files

# Unzip
with zipfile.ZipFile(zip_filename, "r") as zip_ref:
    zip_ref.extractall(extract_dir)

# Remove the original zip file to save space
os.remove(zip_filename)

# Step 5: List files in the dataset directory
print("Contents of dataset folder:")
print(os.listdir(extract_dir))

# Step 6: Load a CSV file for verification (if available)
import pandas as pd

csv_file = "filename.csv"  # Example: 'winemag-data-130k-v2.csv'
csv_path = os.path.join(extract_dir, csv_file)

# Check if file exists before loading
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    display(df.head())
else:
    print(f"CSV file '{csv_file}' not found in {extract_dir}")
