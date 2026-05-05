from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image Path
image_paths = [
    r"C:\Users\Sonu\Desktop\Image Side Show\-\Image side show\IMG_0946.JPG",
    r"C:\Users\Sonu\Desktop\Image Side Show\-\Image side show\IMG_0947.JPG",
    r"C:\Users\Sonu\Desktop\Image Side Show\-\Image side show\IMG_0949.JPG",
    r"C:\Users\Sonu\Desktop\Image Side Show\-\Image side show\IMG_0950.JPG",
    r"C:\Users\Sonu\Desktop\Image Side Show\-\Image side show\IMG_0952.JPG"
]

# Resize images
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(img) for img in images]

# Label to display images
label = tk.Label(root)
label.pack()

# Cycle through images
slideshow = cycle(photo_images)

def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo  # prevent garbage collection
    root.after(3000, update_image)  # call again after 3 seconds

def start_slideshow():
    update_image()

play_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()