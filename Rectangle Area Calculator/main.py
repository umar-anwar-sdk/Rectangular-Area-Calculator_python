import tkinter as tk

def calculate_area(length, width):
    area = length * width
    return area

def on_calculate_button_click():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        result = calculate_area(length, width)
        result_label.config(text=f"Area: {result} square units")
    except ValueError:
        result_label.config(text="Please enter valid numerical values for length and width.")

# Create the main window
window = tk.Tk()
window.title("Rectangle Area Calculator")

# Create and place a frame for the form-like layout
form_frame = tk.Frame(window)
form_frame.pack(padx=10, pady=10)

length_label = tk.Label(form_frame, text="Length:")
length_label.grid(row=0, column=0, padx=5, pady=5,)

length_entry = tk.Entry(form_frame,width=20)
length_entry.grid(row=0, column=1, padx=5, pady=5)

width_label = tk.Label(form_frame, text="Width:")
width_label.grid(row=1, column=0, padx=5, pady=5)

width_entry = tk.Entry(form_frame,width=20)
width_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(form_frame, text="Calculate Area", command=on_calculate_button_click)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="Area: ",width=20)
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
