import random
import string
import tkinter as tk
from tkinter import messagebox

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
root.title("Message Coder/Decoder")

# Create and pack the entry widget
entry_sentence = tk.Entry(root, width=50)
entry_sentence.pack(pady=10)

# Create and pack the code and decode buttons
button_code = tk.Button(root, text="Code Message", command=code_message)
button_code.pack(side="left", padx=10)

button_decode = tk.Button(root, text="Decode Message", command=decode_message)
button_decode.pack(side="right", padx=10)

# Run the main event loop
root.mainloop()