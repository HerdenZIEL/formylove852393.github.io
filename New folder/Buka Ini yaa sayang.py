import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import pygame
import threading
import math
from turtle import *

# Fungsi untuk memutar musik
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("2.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

# Fungsi untuk animasi GIF
def animate_gif(label, frames, delay, index=0):
    frame = frames[index]
    label.configure(image=frame)
    root.after(delay, animate_gif, label, frames, delay, (index+1) % len(frames))

# Fungsi untuk berkedipkan titik
def blink_dot():
    current_text = label_text.cget("text")
    if current_text.endswith("."):
        label_text.config(text="I love you in every universe")
    else:
        label_text.config(text="I love you in every universe.")
    root.after(500, blink_dot)

# Mulai thread untuk musik
threading.Thread(target=play_music, daemon=True).start()

# Buat jendela utama
root = tk.Tk()
root.title("Happy Birthday")
root.geometry("600x600")
root.configure(bg="black")

# Tampilkan GIF
canvas = tk.Canvas(root, width=500, height=400, bg="black", highlightthickness=0)
canvas.pack(pady=20)

gif = Image.open("1.gif")  # Ganti dengan nama file gif kamu
frames = [ImageTk.PhotoImage(frame.copy().resize((500, 400))) for frame in ImageSequence.Iterator(gif)]
label_gif = tk.Label(canvas, bg="black")
label_gif.pack()
animate_gif(label_gif, frames, delay=100)

# Tampilkan teks berkedip
label_text = tk.Label(root, text="I love you in every universe.", font=("Courier", 20, "bold"), fg="pink", bg="black")
label_text.pack(pady=10)
blink_dot()

def heart(k):
    return 15*math.sin(k)**3

def heart1(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)

speed(1000)
bgcolor('black')
for i in range(6000):
    goto(heart(i)*20,heart1(i)*20)
    for j in range(5):
        color('pink')

done()

# Jalankan aplikasi
root.mainloop()
