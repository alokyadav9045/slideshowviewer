from itertools import cycle
from PIL import Image ,ImageTk
import time
import tkinter as tk 

root=tk.Tk()
root.title("Image slide show viewer")

image_paths=[
    r"C:\alok\IMG_20231001_124007_608.jpg",
    r"C:\alok\photo_2024-05-16_22-48-43.jpg",
    r"C:\alok\profile-pic (6).png",
    r"C:\alok\Dp withoutbg.png",
] 
image_size=(720,720)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow= cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root,text='play button', command=start_slideshow)
play_button.pack()

root.mainloop()
