import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import ImageTk

# Prompt user to upload image
def upload_image():

# Diplay before and after images
def display_images(original_image, altered_image):

# Apply chosen processing method to image
def apply_processing(option, image):

# Image Processing method functions here
def negative_image(image):

def translate_image(image, distX, distY):

def denoise_image(image, sigma=2):

def sharpen_image(image, kernel):

def edge_detection(image):

# Prompt user to select processing option
def on_continue(option, image, img, file_path):

# Prompt user to upload image
def create_gui():

# Diplay options when Image is uploaded
def handle_upload(root):

if __name__ == '__main__':
    create_gui()
