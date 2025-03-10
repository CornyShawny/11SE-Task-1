import tkinter as tk

# title for gui and background
root = tk.Tk() # create main window
root.title("WeatherFetch")
root.configure(background="lightblue")

# size of the window
root.minsize(100, 100)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

# words within gui
tk.Label(root, text="Weather Fetch").pack()

# frame inside gui
frame = tk.Frame(root, width=250, height=250)
frame.pack(padx=5, pady=5)

# frame inside the frame inside gui
nested_frame = tk.Frame(frame, width=200, height=200, bg="lightblue")
nested_frame.pack(padx=10, pady=10)

def submit_location():
    print("Location submitted.")

# submit button to submit the location
submit = tk.Button(root, text="Submit", command=submit_location)
submit.pack()

root.mainloop()