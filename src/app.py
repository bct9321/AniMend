import tkinter as tk
from tkinter import messagebox
from animend import process_directories_batch

def process_directories():
    try:
        process_directories_batch()
        messagebox.showinfo("Success", "Processing completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("AniMend")

# Create a label to display instructions
instruction_label = tk.Label(root, text="Click the button to process anime directories:")
instruction_label.pack(pady=10)

# Create a button to trigger the processing
process_button = tk.Button(root, text="Process Directories", command=process_directories)
process_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
