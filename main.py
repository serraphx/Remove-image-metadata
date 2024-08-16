import os
from PIL import Image
from PIL.ExifTags import TAGS


# Removes metadata from an image file
#image_path: The full path of the image file.
def remove_metadata(image_path):

    try:
        image = Image.open(image_path)

        # Create a new image without EXIF data
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        # Save the new image, replacing the old one
        image_without_exif.save(image_path)

        print(f"Metadata removed from {image_path}")

    except Exception as e:
        print(f"Failed to remove metadata from {image_path}: {e}")


# Processes all image files in a directory, removing their metadata.
def process_directory(directory_path):

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            file_path = os.path.join(directory_path, filename)
            remove_metadata(file_path)


directory_path = input("Enter the full directory path: ")
process_directory(directory_path)
