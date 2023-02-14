import random
import tkinter as tk

def get_integer_input(firstString, errorString="Error, please enter an integer: "):
    validatedInput = 0
    tryLoop = True

    try:
        validatedInput = int(input(firstString))
    except ValueError:
        while tryLoop:
            tryLoop = False
            try:
                validatedInput = int(input(errorString))
            except ValueError:
                tryLoop = True
    return validatedInput

def generate_password(password_length, include_numbers, include_special_characters, root):
    letters_list = list("abcdefghijklmnopqrstuvwxyz")
    numbers_list = list("0123456789")
    special_characters_list = list("!@#$%^&*()_+-=")

    password_list = []

    # Add characters to the password list
    for i in range(password_length):
        if include_numbers and include_special_characters:
            password_list.append(random.choice(letters_list + numbers_list + special_characters_list))
        elif include_numbers:
            password_list.append(random.choice(letters_list + numbers_list))
        elif include_special_characters:
            password_list.append(random.choice(letters_list + special_characters_list))
        else:
            password_list.append(random.choice(letters_list))
            
    my_pass = "".join(password_list)
    
    pass_label = tk.Label(root, text=my_pass, anchor="w")
    
    pass_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="s")
    
    # Make a button that copies the password to the clipboard
    root.clipboard_clear()
    copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: root.clipboard_append(my_pass))
    copy_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


def create_gui():
    root = tk.Tk()
    root.title("Password Generator")
    
    password_length_label = tk.Label(root, text="Password Length")
    password_length_scale = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL, length=150)
    
    include_numbers_var = tk.BooleanVar()
    include_numbers_var.set(True)
    
    include_numbers_label = tk.Label(root, text="Include numbers: ", anchor="w")
    include_numbers_checkbox = tk.Checkbutton(root, variable=include_numbers_var)

    include_special_characters_var = tk.BooleanVar()
    include_special_characters_var.set(True)
    
    include_special_characters_label = tk.Label(root, text="Include special characters: ", anchor="w")
    include_special_characters_checkbox = tk.Checkbutton(root,variable=include_special_characters_var)
    
    generate_button = tk.Button(root, text="Generate Password",command=lambda: 
        generate_password(int(password_length_scale.get()), 
                          include_numbers_var.get(), 
                          include_special_characters_var.get(), root))
    
    
    password_length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    password_length_scale.grid(row=0, column=0, padx=150, sticky="w")
    
    include_numbers_label.grid(row=1, column=0, sticky="w")
    include_numbers_checkbox.grid(row=1, column=0, padx=150, sticky="w")
    
    include_special_characters_label.grid(row=2, column=0, sticky="w")
    include_special_characters_checkbox.grid(row=2, column=0, padx=150, sticky="w")

    generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
    

    root.mainloop()


   
    
if __name__ == "__main__":
    create_gui()