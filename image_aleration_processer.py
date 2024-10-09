import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import ImageTk

def upload_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
    if file_path:
        img = Image.open(file_path).convert('L')  # Convert to grayscale
        image_array = np.array(img)
        return image_array, img, file_path
    else:
        messagebox.showerror("Error", "No image selected.")
        return None, None, None

def display_images(original_image, altered_image):
    display_window = tk.Toplevel()
    display_window.title("Original and Altered Image")

    # Convert numpy arrays to PIL Images
    original_img = Image.fromarray(original_image)
    altered_img = Image.fromarray(altered_image)

    # Convert to PhotoImage to display in Tkinter
    original_img_tk = ImageTk.PhotoImage(original_img)
    altered_img_tk = ImageTk.PhotoImage(altered_img)

    # Create labels to display both images side by side
    label_original = tk.Label(display_window, image=original_img_tk)
    label_altered = tk.Label(display_window, image=altered_img_tk)

    label_original.grid(row=0, column=0)
    label_altered.grid(row=0, column=1)

    # Keep a reference to avoid garbage collection
    label_original.image = original_img_tk
    label_altered.image = altered_img_tk

def apply_processing(option, image):
    if option == "Negative Image":
        return negative_image(image)
    elif option == "Translate Image":
        return translate_image(image, 5, 5)
    elif option == "Histogram Equalization":
        return np.array(ImageOps.equalize(Image.fromarray(image)))
    elif option == "Denoise Image":
        return denoise_image(image)
    elif option == "Edge Detection":
        return edge_detection(image)
    elif option == "Sharpen Image":
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        return sharpen_image(image, kernel)
    else:
        return image

# Image Processing methods
def negative_image(image):
    return 255 - image

def translate_image(image, distX, distY):
    translated_image = np.zeros_like(image)
    height, width = image.shape
    for i in range(height):
        for j in range(width):
            newX, newY = j + distX, i + distY
            if 0 <= newX < width and 0 <= newY < height:
                translated_image[newY, newX] = image[i, j]
    return translated_image

def denoise_image(image, sigma=2):
    from scipy.ndimage import gaussian_filter
    return gaussian_filter(image, sigma)

def sharpen_image(image, kernel):
    from scipy.ndimage import convolve
    return convolve(image, kernel)

def edge_detection(image):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    from scipy.ndimage import convolve
    grad_x = convolve(image, sobel_x)
    grad_y = convolve(image, sobel_y)
    return np.hypot(grad_x, grad_y).astype(np.uint8)

def on_continue(option, image, img, file_path):
    if option.get() == "":
        messagebox.showerror("Error", "Please select an option before continuing.")
        return

    altered_image = apply_processing(option.get(), image)
    display_images(np.array(img), altered_image)

def create_gui():
    root = tk.Tk()
    root.title("Image Processing App")

    # Upload button
    upload_btn = tk.Button(root, text="Upload Image", command=lambda: handle_upload(root))
    upload_btn.pack(pady=10)

    root.mainloop()

def handle_upload(root):
    image_array, img, file_path = upload_image()

    if image_array is not None:
        # Option Selector
        options_frame = tk.Frame(root)
        options_frame.pack(pady=10)

        tk.Label(options_frame, text="Select an option:").pack()

        option = tk.StringVar()
        option.set("")  # Default value

        options = ["Negative Image", "Translate Image", "Histogram Equalization", "Denoise Image", "Edge Detection", "Sharpen Image"]

        for opt in options:
            radio_btn = tk.Radiobutton(options_frame, text=opt, variable=option, value=opt)
            radio_btn.pack(anchor=tk.W)

        # Continue button
        continue_btn = tk.Button(root, text="Continue", command=lambda: on_continue(option, image_array, img, file_path))
        continue_btn.pack(pady=10)

if __name__ == '__main__':
    create_gui()
