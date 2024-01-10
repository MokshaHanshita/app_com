import tkinter as tk
from tkinter import ttk, messagebox
import requests
import tkinter as tk
import requests
import customtkinter as ctk
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip
login_status=False

class screen_1():
    def __init__(self, app):
        self.app = app

        self.screen1_frame = ctk.CTkFrame(master=app, border_width=2, corner_radius=10, width=650, height=550)
        self.screen1_frame.place(x=30, y=30)
        result_text = tk.Label(master=self.screen_1, text="", wraplength=400)
        result_text.pack(pady=10)