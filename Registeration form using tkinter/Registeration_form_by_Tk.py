# import tkinter as tk
# from tkinter import messagebox

# # Create the main window
# root = tk.Tk()
# root.title("Registration Form")
# root.geometry("330x290")  # Adjusted window size

# # First Name
# tk.Label(root, text="First Name:",).grid(row=0, column=0,  padx=5, pady=5)
# first_name_entry = tk.Entry(root).grid(row=0, column=1)


# # Last Name
# tk.Label(root, text="Last Name:").grid(row=1, column=0,  padx=5, pady=5)
# last_name_entry = tk.Entry(root).grid(row=1, column=1)

# # Email
# tk.Label(root, text="Email:").grid(row=2, column=0,  padx=5, pady=5)
# email_entry = tk.Entry(root).grid(row=2, column=1)

# # Password
# tk.Label(root, text="Password:").grid(row=3, column=0,  padx=5, pady=5)
# pass_entry = tk.Entry(root, show='*').grid(row=3, column=1)

# # Confirm Password
# tk.Label(root, text="Confirm Password:").grid(row=4, column=0,  padx=5, pady=5)
# confirm_pass_entry = tk.Entry(root, show='*').grid(row=4, column=1)

# # Gender
# gender_var = tk.Radiobutton()
# tk.Label(root, text="Gender:").grid(row=5, column=0,  padx=5, pady=5)
# tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=5, column=1)
# tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=6, column=1)


# def submit():
#     # Validate the entered data
#     if pass_entry.get() != confirm_pass_entry.get():
#         messagebox.showerror("Error", "Passwords do not match!")
#         return
#     if not (first_name_entry.get() and last_name_entry.get() and email_entry.get() and pass_entry.get() and gender_var.get()):
#         messagebox.showerror("Error", "All fields are required!")
#         return
#     messagebox.showinfo("Submitted", "Registration Submitted Successfully!")

# # Submit Button
# submit_btn = tk.Button(root, text="Submit", command=submit).grid(row=7, column=1,  padx=5, pady=5)


# root.mainloop()



import tkinter as tk
from tkinter import messagebox

def login():
    # Validate the entered data
    if not (email_login_entry.get() and pass_login_entry.get()):
        messagebox.showerror("Error", "Email and Password are required!")
        return
    # You can add your code here to verify the login credentials
    messagebox.showinfo("Login", "Login Successful!")

# Create the login window
login_root = tk.Tk()
login_root.title("Login System")
login_root.geometry("400x150")  # Set the window size for the login system

# Email
tk.Label(login_root, text="Email:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
email_login_entry = tk.Entry(login_root)
email_login_entry.grid(row=0, column=1)

# Password
tk.Label(login_root, text="Password:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
pass_login_entry = tk.Entry(login_root, show='*')
pass_login_entry.grid(row=1, column=1)

# Login Button
login_btn = tk.Button(login_root, text="Login", command=login)
login_btn.grid(row=2, column=1, sticky='e', padx=5, pady=5)

# Run the login application
login_root.mainloop()






