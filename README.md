# Kaggle2GGDrive

aggle2GGDrive is a simple automation tool to download datasets from Kaggle and save them directly into Google Drive. This tool helps streamline dataset collection, especially for training machine learning models in a Colab environment or for long-term storage in the cloud.

> Seamlessly download Kaggle datasets to your Google Drive 🚀

**Kaggle2GGDrive** automates the process of fetching datasets from Kaggle and storing them directly into your Google Drive.  
Perfect for machine learning workflows, data analysis projects, or simply keeping a backup of important datasets.

---

## 🔧 Features

- 🔽 Download datasets from Kaggle via API.
- ☁️ Save datasets directly into a specified Google Drive folder.
- ⚡ Quick setup with minimal configuration.
- 📦 Supports both zipped datasets and individual file downloads.
  
---

## 📦 Requirements

- Python 3.7+
- Kaggle API credentials (`kaggle.json`)
- Google Drive mounted on Colab

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup
  
1. Obtain Kaggle API Credentials
   - Go to Kaggle Account Settings
   - Click "Create New API Token".
   - A kaggle.json file will be downloaded.
  
2. Mount Google Drive (in Colab)

```python
from google.colab import drive
drive.mount('/content/drive')
```

3. Configure Kaggle API

- Set the environment variable pointing to your kaggle.json:
   
```python 
import os
os.environ['KAGGLE_CONFIG_DIR'] = "/path/to/your/kaggle.json"
```

- Example for Colab:
  
```python
os.environ['KAGGLE_CONFIG_DIR'] = "/content/drive/MyDrive/Project/Kaggle2GGDrive/"
```

---

## 🚀 Usage

Download a Kaggle dataset and move it to Google Drive:

```bash
python kaggle2ggdrive.py \
  --dataset <kaggle-dataset-slug> \
  --drive-folder <google-drive-folder-path>
Argument	Description
--dataset	Kaggle dataset slug (e.g., zynicide/wine-reviews)
--drive-folder	Path to your target Google Drive folder
```

---

## 📁 Example

```bash
python kaggle2ggdrive.py \
  --dataset zynicide/wine-reviews \
  --drive-folder /content/drive/MyDrive/Datasets/WineReviews
```

---

## 📌 Notes

- Ensure you have sufficient storage space in your Google Drive.
- Kaggle enforces API download limits — avoid frequent repeated downloads.
- For very large datasets, consider downloading in chunks.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Contributions are welcome! If you'd like to add features or improve the tool, feel free to fork this repository and submit a pull request.

---

🙌 Acknowledgments
- Kaggle API
- Google Drive API
