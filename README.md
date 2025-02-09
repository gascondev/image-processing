# Image Processing with OpenCV

This is a simple image processing project using OpenCV. The script loads an image, converts it to grayscale, creates a negative version, and displays the results side by side.

## 📌 Features

- Load an image from a file
- Convert the image to grayscale
- Generate a negative of the original image
- Display all three images side by side

## 🚀 Installation

### 1️⃣ Prerequisites

Make sure you have **Python 3** installed on your system. You also need to install OpenCV and NumPy:

```bash
pip install opencv-python numpy
```

### 2️⃣ Clone the repository

```bash
git clone https://github.com/gascondev/image-processing.git
cd image-processing
```

## ▶️ Usage

1. Place an image named `image1.jpg` in the project folder.
2. Run the script:
   ```bash
   python main.py
   ```
3. The processed images will be displayed in a new window.

## 📝 Notes

- If the image is not found, the script will display an error message.
- You can modify the script to use a different image by changing the filename in the `cv2.imread()` function.

## 📸 Example Output

The script generates a side-by-side display of:

1. The original image
2. The grayscale version
3. The negative version

---

**Author:** [Álvaro Gascón](https://github.com/gascondev)\
🔗 **GitHub Repository:** [Image Processing](https://github.com/gascondev/image-processing)


