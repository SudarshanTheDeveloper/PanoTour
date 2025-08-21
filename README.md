# PanoTour
PanoTour is a Python-based tool for creating 360-degree panoramic images by merging six cube map photos using OpenCV. The final output is a high-resolution 4K equirectangular panorama image ideal for virtual tours, VR environments, or immersive media.

# Features
Converts six images representing cube map faces (front, back, left, right, top, bottom) into a seamless 360-degree panorama.

Uses OpenCV for image processing and stitching.

Blends seams between cube faces for a smooth final image.

Outputs a 4K resolution (16384 x 8192) equirectangular panorama.

Optional real-time display of the result.

# Getting Started
Prerequisites
Python 3.x

OpenCV library for Python

Install OpenCV using pip:

# bash
pip install opencv-python
# Usage
Prepare six images for the cube map faces named as follows (with .jpg extension):

File_0.jpg (Bottom)

File_1.jpg (Top)

File_2.jpg (Right)

File_3.jpg (Left)

File_4.jpg (Back)

File_5.jpg (Front)

Place these images in the same directory as the script or update the paths accordingly.

Run the Python script:

# bash
python 360pano.py
The script will generate a 360_image_4k_seam_blended.jpg file in the directory.

(Optional) The script displays the resulting panorama image in a window.

# How It Works
The script loads the six cube map images.

Applies necessary rotations and flips to align the images correctly.

Blends the seams between adjacent images for smooth transitions.

Converts the cube map into a 360-degree equirectangular panorama using spherical coordinates mapping.

Saves and displays the final panoramic image.

# Future Improvements
Add a web interface to upload images and generate panoramas online.

Implement error handling and input validation.

Allow adjustable output resolutions.

Optimize performance with multiprocessing or C++ backends.
