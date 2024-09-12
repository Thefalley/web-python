
# 📸 Flask Image Upload App

This is a simple web application built with Flask that allows users to upload images to a local folder via a web interface. It provides a basic understanding of how to implement a file upload system using Python (Flask) for the backend and HTML/CSS for the frontend.

## ✨ Features

- 🖼️ Simple web interface to upload images from your device.
- 💾 Images are stored locally in the `static/uploads` folder.
- 🎉 Displays the uploaded image after a successful upload.
- 🖌️ Supports popular image formats: `.png`, `.jpg`, `.jpeg`, `.gif`.

## 📁 Project Structure

The project is organized into the following directories and files:



### File and Folder Descriptions:

- **`app.py`**: The core of the application, managing routes and logic for handling file uploads.
- **`templates/index.html`**: The main webpage that provides a form for users to upload images.
- **`templates/upload_success.html`**: A confirmation page that displays the uploaded image.
- **`static/style.css`**: Stylesheet for the HTML pages, defining the look and feel of the interface.
- **`static/uploads/`**: The folder where the images are saved once they are uploaded.

## ⚙️ How It Works

1. **Form Submission**: On the homepage (`/`), users can select an image file from their device and submit the form to upload it.
2. **File Upload Handling**: The backend (`app.py`) receives the file, verifies the file type, and stores it in the `static/uploads/` directory.
3. **Upload Success**: After a successful upload, the app redirects to a page that displays the uploaded image.

## 🚀 Setup Instructions

To run this project on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-image-upload-app.git
cd flask-image-upload-app

pip install Flask
```

# Set you ip 
```
ipconfig 
``` 

# Run the program 
````
python app.py
````

# run navegator
````
http://<your-local-ip>:5000/
````