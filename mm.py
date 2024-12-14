import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os
import threading

def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            threading.Thread(target=generate_and_play_tts, args=(text,)).start()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def generate_and_play_tts(text):
    tts = gTTS(text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3" if os.name == "nt" else "open output.mp3")

def clear_text():
    text_entry.delete("1.0", tk.END)

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("400x300")

# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_entry.pack(pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create buttons and align them side by side
play_button = tk.Button(button_frame, text="Play", command=play_text, bg="black", fg="white")
play_button.grid(row=0, column=0, padx=5)

set_button = tk.Button(button_frame, text="Set", command=clear_text, bg="black", fg="white")
set_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="red", fg="white")
exit_button.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()
