# Import the Tkinter GUI library
import tkinter as tk

# Import Matplotlib components needed for embedding plots into Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Create the main application window
root = tk.Tk()
root.title("Interactive Chart")     # Set the window title
root.geometry("600x500")           # Set the size of the window (width x height)

# Create a Matplotlib figure (5 inches by 4 inches, 100 dots per inch)
fig = Figure(figsize=(5, 4), dpi=100)

# Add a subplot to the figure (1 row, 1 column, first subplot)
plot = fig.add_subplot(111)

# Embed the Matplotlib figure into the Tkinter window using a canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()  # Draw the initial empty chart
canvas.get_tk_widget().pack()  # Add the canvas widget to the window

# Create an Entry widget where the user can type a number
entry = tk.Entry(root)
entry.pack(pady=10)  # Add vertical padding for spacing

# Define a function to update the chart based on user input
def update_chart():
    try:
        num = int(entry.get())  # Get the number entered by the user
        plot.clear()  # Clear the previous plot

        # Create a new list of x and y values where y = x^2
        x_vals = [i for i in range(num)]
        y_vals = [i**2 for i in range(num)]

        plot.plot(x_vals, y_vals, marker='o')  # Plot the new data as a line with dots
        plot.set_title("Square Numbers")       # Set chart title
        plot.set_xlabel("x")                   # Set x-axis label
        plot.set_ylabel("x squared")           # Set y-axis label

        canvas.draw()  # Redraw the updated plot
    except ValueError:
        pass  # Do nothing if the input is not a valid number

# Create a button that calls update_chart() when clicked
tk.Button(root, text="Plot Squares", command=update_chart).pack()

# Start the Tkinter event loop
root.mainloop()