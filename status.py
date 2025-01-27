import customtkinter as ctk
from tkinter import messagebox
import requests
import json
import threading
import time

STATUS_LIST = []
CURRENT_STATUS_INDEX = 0
TOKEN_FILE = "token.json"
INTERVAL = 60
IS_ROTATING = False

DISCORD_BG = "#36393F"
DISCORD_FG = "#FFFFFF"
DISCORD_BUTTON_BG = "#7289DA"
DISCORD_BUTTON_FG = "#FFFFFF"
DISCORD_ENTRY_BG = "#40444B"
DISCORD_ENTRY_FG = "#FFFFFF"
DISCORD_LISTBOX_BG = "#2F3136"
DISCORD_LISTBOX_FG = "#FFFFFF"

def load_token():
    try:
        with open(TOKEN_FILE, "r") as file:
            data = json.load(file)
            return data.get("token", "")
    except FileNotFoundError:
        return ""

def save_token(token):
    with open(TOKEN_FILE, "w") as file:
        json.dump({"token": token}, file)

def change_status(status):
    try:
        payload = {
            "custom_status": {
                "text": status
            }
        }
        headers = {
            "Authorization": TOKEN,
            "Content-Type": "application/json"
        }
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Changed Status to: {status}")
        else:
            print(f"Error Changing status contact easylogs for help: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"There is an Error: {e}")

def status_rotation():
    global CURRENT_STATUS_INDEX, IS_ROTATING
    while IS_ROTATING:
        if STATUS_LIST:
            change_status(STATUS_LIST[CURRENT_STATUS_INDEX])
            CURRENT_STATUS_INDEX = (CURRENT_STATUS_INDEX + 1) % len(STATUS_LIST)
        time.sleep(INTERVAL)

def add_status():
    status = status_entry.get()
    if status:
        STATUS_LIST.append(status)
        status_listbox.insert(ctk.END, status)
        status_entry.delete(0, ctk.END)
    else:
        messagebox.showwarning("Warning", "Please insert a Status")

def set_interval():
    global INTERVAL
    try:
        new_interval = int(interval_entry.get())
        if new_interval > 0:
            INTERVAL = new_interval
            messagebox.showinfo("Success", f"Intervall is now on {INTERVAL} Seconds")
        else:
            messagebox.showwarning("Warning", "The Intervall must be greater than 0")
    except ValueError:
        messagebox.showerror("Fehler", "Please Insert a Valid Number!")

def update_token():
    new_token = token_entry.get()
    if new_token:
        save_token(new_token)
        global TOKEN
        TOKEN = new_token
        messagebox.showinfo("Success", "Token got updated!")
    else:
        messagebox.showwarning("Warning", "Please enter a Token!")

def toggle_rotation():
    global IS_ROTATING
    if not IS_ROTATING:
        if not STATUS_LIST:
            messagebox.showwarning("Warning", "Add atleast 1 Status")
            return
        if not TOKEN:
            messagebox.showwarning("Warning", "Use a Valid User-Token!")
            return
        IS_ROTATING = True
        rotation_thread = threading.Thread(target=status_rotation, daemon=True)
        rotation_thread.start()
        start_button.configure(text="Stop Rotation", fg_color="#E74C3C")
        messagebox.showinfo("Info", "Status-Rotation started!")
    else:
        IS_ROTATING = False
        start_button.configure(text="Start Rotation", fg_color=DISCORD_BUTTON_BG)
        messagebox.showinfo("Info", "Status-Rotation stopped!")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Discord Status Changer by easylogs")
root.geometry("500x600")
root.configure(bg=DISCORD_BG)

TOKEN = load_token()

token_label = ctk.CTkLabel(root, text="Discord User-Token:", text_color=DISCORD_FG)
token_label.pack(pady=5)
token_entry = ctk.CTkEntry(root, width=400, fg_color=DISCORD_ENTRY_BG, text_color=DISCORD_ENTRY_FG)
token_entry.insert(0, TOKEN)
token_entry.pack(pady=5)
update_token_button = ctk.CTkButton(root, text="Update Token", command=update_token, fg_color=DISCORD_BUTTON_BG, text_color=DISCORD_BUTTON_FG)
update_token_button.pack(pady=5)

status_label = ctk.CTkLabel(root, text="New status:", text_color=DISCORD_FG)
status_label.pack(pady=5)
status_entry = ctk.CTkEntry(root, width=400, fg_color=DISCORD_ENTRY_BG, text_color=DISCORD_ENTRY_FG)
status_entry.pack(pady=5)
add_status_button = ctk.CTkButton(root, text="Add status", command=add_status, fg_color=DISCORD_BUTTON_BG, text_color=DISCORD_BUTTON_FG)
add_status_button.pack(pady=5)

status_listbox = ctk.CTkTextbox(root, width=400, height=150, fg_color=DISCORD_LISTBOX_BG, text_color=DISCORD_LISTBOX_FG)
status_listbox.pack(pady=10)

interval_label = ctk.CTkLabel(root, text="Intervall (in Seconds):", text_color=DISCORD_FG)
interval_label.pack(pady=5)
interval_entry = ctk.CTkEntry(root, width=400, fg_color=DISCORD_ENTRY_BG, text_color=DISCORD_ENTRY_FG)
interval_entry.insert(0, str(INTERVAL))
interval_entry.pack(pady=5)
set_interval_button = ctk.CTkButton(root, text="Set Interval", command=set_interval, fg_color=DISCORD_BUTTON_BG, text_color=DISCORD_BUTTON_FG)
set_interval_button.pack(pady=5)

start_button = ctk.CTkButton(root, text="Start Rotation", command=toggle_rotation, fg_color=DISCORD_BUTTON_BG, text_color=DISCORD_BUTTON_FG)
start_button.pack(pady=10)

root.mainloop()