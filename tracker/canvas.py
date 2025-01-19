import tkinter as tk

import customtkinter

from covid_data import get_covid_data
import customtkinter as ctk
from PIL import Image, ImageTk

canvas = ctk.CTk()
canvas.geometry("400x500")
canvas.title("COVID-19 Tracker")
customtkinter.set_appearance_mode("dark")
# Set the new icon
icon_image = Image.open(r"D:\Python_Projects\COVID-19_Tracker\resources\icon_covid.png")
icon = ImageTk.PhotoImage(icon_image)
canvas.iconphoto(False, icon)
ctk_icon = ctk.CTkImage(light_image=icon_image, size=(32, 32))


f = ("poppins", 15, "bold")

button = ctk.CTkButton(master=canvas, font=f, text="Load", command=get_covid_data)
button.pack(pady=20)

label = tk.Label(canvas, font=f)
label.config(fg="white")
label.config(bg="#282424")
label.pack(pady=20)

label2 = tk.Label(canvas, font=8)
label2.config(fg="white")
label2.config(bg="#282424")
label2.pack()