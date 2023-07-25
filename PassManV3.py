import tkinter as tk
import json
from tkinter import ttk
from tkinter import messagebox
import os

def login():
    username = username_entry.get()
    password = password_entry.get()

    # TODO: Add your authentication logic here
    if username == "admin" and password == "password":
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def open_create_account():
    global email_entry, username_entry, password_entry


    create_account_window = tk.Toplevel(root)
    create_account_window.title("Create Account")

    # Create a frame for the create account section
    create_account_frame = ttk.Frame(create_account_window, padding=10)
    create_account_frame.pack()

    email_label = ttk.Label(create_account_frame, text="Email:")
    email_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    email_entry = ttk.Entry(create_account_frame)
    email_entry.grid(row=0, column=1, padx=5, pady=5)

    email_confirm_label = ttk.Label(create_account_frame, text="Confirm Email:")
    email_confirm_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    email_confirm_entry = ttk.Entry(create_account_frame)
    email_confirm_entry.grid(row=1, column=1, padx=5, pady=5)

    username_label = ttk.Label(create_account_frame, text="Username:")
    username_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    username_entry = ttk.Entry(create_account_frame)
    username_entry.grid(row=2, column=1, padx=5, pady=5)

    password_label = ttk.Label(create_account_frame, text="Password:")
    password_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    password_entry = ttk.Entry(create_account_frame, show="*")
    password_entry.grid(row=3, column=1, padx=5, pady=5)

    password_confirm_label = ttk.Label(create_account_frame, text="Confirm Password:")
    password_confirm_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
    password_confirm_entry = ttk.Entry(create_account_frame, show="*")
    password_confirm_entry.grid(row=4, column=1, padx=5, pady=5)

    submit_button = ttk.Button(create_account_frame, text="Create Account", command=create_account)
    submit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

def create_account():

    global email_entry, username_entry, password_entry

    program_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(program_directory, "passwords.json")

    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    data = {
        "Email":email,
        "Username":username,
        "Password": password
    }

    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                pass  # Create an empty file

        with open(file_path, "a") as file:
            json.dump(data, file)

        messagebox.showinfo("Success", "Account created successfully.")
    except IOError:
        messagebox.showerror("Error", "Failed to save account credentials.")

def create_login_screen():
    global root
    global username_entry
    global password_entry

    root = tk.Tk()
    root.title("Password Manager Login")

    # Create a frame for the login section
    login_frame = ttk.Frame(root, padding=10)
    login_frame.pack()

    username_label = ttk.Label(login_frame, text="Username:")
    username_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    username_entry = ttk.Entry(login_frame)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = ttk.Label(login_frame, text="Password:")
    password_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    password_entry = ttk.Entry(login_frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    submit_button = ttk.Button(login_frame, text="Login", command=login)
    submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    create_account_button = ttk.Button(login_frame, text="Create Account", command=open_create_account)
    create_account_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    root.mainloop()

# Run the login screen
if __name__ == "__main__":
    create_login_screen()