import cv2
import os
import glob

# Ask for the folder path from the user
folder_path = input("Please enter the path to your images folder: ")
# Assume the output video path to be in the same folder, but with .mp4 extension
output_video_path = os.path.join(folder_path, 'output_video.mp4')

# Ask if the user wants to limit to the first N files in the folder
limit_input = input("Limit to the first N files? Leave blank for no limit: ")
limit = int(limit_input) if limit_input.isdigit() else None

# Retrieve a list of image paths
image_paths = glob.glob(os.path.join(folder_path, '*.jpg')) + glob.glob(os.path.join(folder_path, '*.png'))
image_paths.sort()  # Sort the images by name

# Apply limit if specified
if limit is not None:
    image_paths = image_paths[:limit]

# Read the first image to determine the width and height for the video
frame = cv2.imread(image_paths[0])
height, width, layers = frame.shape

# Define the codec and create a VideoWriter object using H.264 ('mp4v')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Note: Some systems might require 'avc1' instead of 'mp4v'
video = cv2.VideoWriter(output_video_path, fourcc, 25.0, (width, height))

# Loop through all images and add them to the video
for image_path in image_paths:
    image = cv2.imread(image_path)
    video.write(image)

# Release the VideoWriter object
video.release()
cv2.destroyAllWindows()

print(f"Video has been created and saved to {output_video_path}")
