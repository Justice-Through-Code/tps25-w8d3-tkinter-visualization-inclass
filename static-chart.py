# Import the tkinter module for creating the GUI
import tkinter as tk

# Import the necessary classes to embed a matplotlib figure in a Tkinter window
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Create the main application window
root = tk.Tk()
root.title("Static Chart in GUI")     # Set the title of the window
root.geometry("500x400")              # Set the window size to 500x400 pixels


# Create a Matplotlib Figure

# Create a figure object with a specified size (5x4 inches) and resolution (100 dots per inch)
fig = Figure(figsize=(5, 4), dpi=100)

# Add a subplot (a single plot area) to the figure
# 111 means: 1 row, 1 column, 1st subplot (i.e., just one plot area in the figure)
plot = fig.add_subplot(111)

# Plot some sample data on the subplot
# X values: [1, 2, 3, 4]; Y values: [10, 20, 25, 30]
plot.plot([1, 2, 3, 4], [10, 20, 25, 30])


# Embed the Figure in Tkinter


# Create a canvas widget that can display the Matplotlib figure inside the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)  # 'master=root' attaches it to the main window

# Draw the canvas (renders the plot)
canvas.draw()

# Get the Tkinter widget from the canvas and pack it so it appears in the window
canvas.get_tk_widget().pack()

# This keeps the window open and waits for user interaction (like closing the window)
root.mainloop()
