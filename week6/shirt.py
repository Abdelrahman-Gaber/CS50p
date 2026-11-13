from PIL import Image, ImageOps
import sys
import os

file_formats = [".jpeg", ".jpg", ".png"]

try:
    file1_extension = os.path.splitext(sys.argv[1])[1].lower()
    file2_extension = os.path.splitext(sys.argv[2])[1].lower()

    if len(sys.argv) > 3:
        sys.exit("Too many commend-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif (file1_extension not in file_formats or file2_extension not in file_formats):
        sys.exit("Files has to be in .jpeg or .jpg or .png extensions")
    elif file1_extension != file2_extension:
        sys.exit("File extensions don't match")
    else:
        shirt = Image.open("shirt.png")
        size = shirt.size
        with Image.open(sys.argv[1], "r") as before:
            before_resized = ImageOps.fit(before, size)
            before_resized.paste(shirt, shirt)
            before_resized.save(sys.argv[2])



except FileNotFoundError:
    sys.exit(f"couldn't read {sys.argv[1]}")
except IndexError:
    sys.exit("Too few command-line arguments")