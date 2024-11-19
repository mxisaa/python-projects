import customtkinter as ctk
from tkinter import messagebox

# Function to check password strength
def check_password_strength():
    password = password_entry.get()
    length_error = len(password) < 8
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    digit_error = not any(char.isdigit() for char in password)
    special_char_error = not any(char in "!@#$%^&*()-_+=<>?/{}[]~" for char in password)

    common_password_error = password.lower() in ["password", "123456", "12345678"]

    errors = [length_error, uppercase_error, lowercase_error, digit_error, special_char_error, common_password_error]

    if sum(errors) == 0:
        strength = "Strong"
        color = "green"
    elif sum(errors) <= 2:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    result_label.configure(text=f"Password Strength: {strength}", text_color=color)

# Set appearance mode and theme
ctk.set_appearance_mode("Dark")  # Set to "Light" or "Dark"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create the GUI
root = ctk.CTk()
root.geometry("500x400")
root.title("Mai's Password Strength Checker")

title_label = ctk.CTkLabel(
    root, 
    text="Type in a password below:", 
    font=("Helvetica", 18, "bold"),
    text_color=("white", "white")
)
title_label.pack(pady=20)

password_entry = ctk.CTkEntry(root, placeholder_text="Enter your password", show="*")
password_entry.pack(pady=10)

check_button = ctk.CTkButton(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=20)

result_label = ctk.CTkLabel(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=20)

root.mainloop()
