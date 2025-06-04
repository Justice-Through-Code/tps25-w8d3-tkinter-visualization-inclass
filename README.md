# tps25-w8d3-tkinter-visualization-inclass

Breakout #1 – Your First Chart
🎯 Goal:
Reinforce fellows' understanding of how to render a basic chart in a Tkinter application using matplotlib. This exercise builds confidence with figure creation, widget layout, and plot customization.

📝 Instructions:
Fellows should:

    Based on the code provided from the original static chart, create a step tracking chart using the following data:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    steps = [4500, 6700, 7200, 5000, 9800, 11000, 7600]

Customize the data:

    Replace X and Y values with something real: temperatures, heart rate, daily steps, grades, etc.


Enhance the chart:

    Add a chart title

    Add X and Y axis labels

Extra Challenges (time permitting):

1) Track two people’s steps or compare two datasets.
    example data:
        friend_steps = [5000, 6000, 8000, 7000, 9000, 10500, 8300]

2) Use a bar chart instead of a line chart

3) Add grid lines to the chart





------------------------------------------------------------------------------------------



Breakout #2 – Interactive Data Entry
🎯 Goal:
Empower fellows to build interactive visualizations that respond to user input. In this case, students will let the user enter a number n, then plot the squares of numbers from 0 to n-1. The plot should be dynamic—updating with each new entry.

📝 Instructions:
Fellows should build a GUI that includes:

    An Entry widget to collect a number from the user.

    A Button that triggers the chart to update.

    A matplotlib plot that displays the squares of numbers from 0 to the entered value.


Bonus features:

    Label the chart axes and title.

    Clear any previous plot lines before redrawing.


Hints:

    Use .get() to read user input from the Entry field.

    Wrap the plotting code in a function connected to the button’s command=.

    Always use plot.clear() before re-plotting to prevent overlap.

    Include .draw() to refresh the canvas with the new chart.

Extra Challenges (time permitting):

1) Dropdown menu to let user choose between squaring and cubing numbers

2) Display error: Show an error Label if a non-numeric number is presented

3) Add tooltips or markers to show values on hover