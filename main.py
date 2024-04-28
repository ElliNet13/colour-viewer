import ctypes
from sys import exit
from PIL import Image, ImageTk
import tkinter as tk

def view(photo):
  root = tk.Tk()
  root.title("Colour Viewer")

# Create a label for displaying the image
  label = tk.Label(root)
  label.pack()
  photo = ImageTk.PhotoImage(image)
  label.config(image=photo)
  label.image = photo
  return root

def hti(hex_color, size=(100, 100)):
    """Convert hexadecimal color to a solid color image."""
    image = Image.new("RGB", size, hex_color)
    return image
def rth(r, g, b):
    """Convert RGB to hexadecimal."""
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

try:
  R = ctypes.c_ubyte(int(input("R")))
  B = ctypes.c_ubyte(int(input("B")))
  G = ctypes.c_ubyte(int(input("G")))
except ValueError:
  print("Invalid input.")
  exit(1)

hex = rth(R.value, G.value, B.value)
print(f"""
R: {R.value}
B: {B.value}
G: {G.value}
Hex: {hex}""")
image = hti(hex, size=(400, 400))
tk = view(image)
tk.mainloop()