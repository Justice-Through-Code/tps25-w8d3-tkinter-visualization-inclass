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
