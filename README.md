
# Image Processing App

This project is a GUI-based Python application that allows users to perform various image processing operations on uploaded images. The app is built using libraries such as `numpy`, `Pillow`, `matplotlib`, and `tkinter`.

## Features
- **Upload Image**: Allows users to upload images in formats like `.jpg`, `.png`, `.jpeg`, `.bmp`.
- **Image Processing Options**:
  - Negative Image
  - Translate Image
  - Histogram Equalization
  - Denoise Image
  - Edge Detection
  - Sharpen Image
- **Display Results**: Original and processed images are displayed side by side.

## Requirements
Ensure the following Python libraries are installed:
- `numpy`
- `Pillow`
- `matplotlib`
- `scipy`

Install them using pip:
```bash
pip install numpy pillow matplotlib scipy
```

## How to Use
1. Run the application:
   ```bash
   python app.py
   ```
2. Click on the **Upload Image** button and select an image file.
3. Choose one of the processing options provided.
4. Click **Continue** to apply the selected image processing technique.
5. The original and altered images will be displayed in a new window.

## File Structure
- **`app.py`**: Contains the main code for the application.

## Functions
### `upload_image()`
Handles image upload and conversion to grayscale.

### `display_images(original_image, altered_image)`
Displays the original and processed images side by side in a new window.

### `apply_processing(option, image)`
Applies the selected image processing technique.

### Image Processing Techniques
- **Negative Image**: Converts the image to its negative.
- **Translate Image**: Shifts the image by a specified distance.
- **Histogram Equalization**: Enhances image contrast.
- **Denoise Image**: Reduces noise using a Gaussian filter.
- **Edge Detection**: Detects edges using Sobel operators.
- **Sharpen Image**: Sharpens the image using a custom kernel.

## Notes
- The application is designed for demonstration and learning purposes.
- Ensure input images are in supported formats.

## License
This project is open-source and available for modification.

## Contributing
Feel free to fork the repository and submit pull requests with improvements or additional features.
