import random
import string
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def code_message():
    alphabets = string.ascii_lowercase
    sentence = entry_sentence.get()
    if sentence:
        words = sentence.split()
        secret_words = []
        for word in words:
            if len(word) > 3:
                modified_word = word[1:] + word[0]
                start_letters = ''.join(random.sample(alphabets, 3))
                end_letters = ''.join(random.sample(alphabets, 3))
                secret_words.append(start_letters + modified_word + end_letters)
            else:
                secret_words.append(word[::-1])
        secret_sentence = ' '.join(secret_words)
        messagebox.showinfo("Secret code language", secret_sentence)
        with open("coded message.txt", 'w') as coded:
            coded.write(secret_sentence)
    else:
        messagebox.showwarning("Warning", "Please enter a sentence.")

def decode_message():
    sentence = entry_sentence.get()
    if sentence:
        words = sentence.split()
        decoded_words = []
        for word in words:
            if len(word) > 6:
                start_letters = word[:3]
                end_letters = word[-3:]
                modified_word = word[3:-3]
                original_word = modified_word[-1] + modified_word[:-1]
                decoded_words.append(original_word)
            else:
                decoded_words.append(word[::-1])
        decoded_sentence = ' '.join(decoded_words)
        messagebox.showinfo("Decoded sentence", decoded_sentence)
        with open("decoded message.txt", 'w') as decoded:
            decoded.write(decoded_sentence)
    else:
        messagebox.showwarning("Warning", "Please enter a sentence.")

# Create the main window
root = tk.Tk()
root.config(bg="#f5f5f5")
root.title("Message Coder/Decoder")
root.geometry("800x500")

image = Image.open("secret folder.png")  # Replace with your PNG file path
resized_image = image.resize((300, 300))  # Resize the image (width, height)

photo = ImageTk.PhotoImage(resized_image)

# Create a label widget for the image
label = tk.Label(root, image=photo, bg="#f5f5f5")

# Adjust the position of the image using the 'place' method
label.place(x=615, y=20)  # x and y set the position

# Create and pack the entry widget
entry_sentence = tk.Entry(root, bg="#eaeaea", width=80)
entry_sentence.place(x=535, y=360)

# Create and pack the code and decode buttons
button_code = tk.Button(root, text="Code Message",width=30, height=3, fg="#ffffff", bg="#2c3e50", command=code_message)
button_code.place(x=500, y=550)

button_decode = tk.Button(root, text="Decode Message",width=30, height=3, fg="#ffffff", bg="#2c3e50", command=decode_message)
button_decode.place(x=830, y=550)

# Run the main event loop
root.mainloop()