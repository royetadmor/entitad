import tkinter as tk
import model

def on_button_click():
    user_input = entry.get()
    result = model.get_entities(user_input)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", result)


# Create the main window
window = tk.Tk()
window.title("GUI Example")

# Create a label
label = tk.Label(window, text="Enter text:")
label.pack()

# Create a text input box
entry = tk.Entry(window, width=50)
entry.pack()

# Create a button
button = tk.Button(window, text="Go", command=on_button_click)
button.pack()

# Create an output text box
output_text = tk.Text(window, height=40, width=80)
output_text.pack()
# Run the main event loop
window.mainloop()
