# Topics Covered-> Getting started with Matplotlib
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
plt.plot(x,y)
plt.show()

# Draw a line in a diagram from position (1, 3) to position (8, 10):
x = np.array([1, 8])
y = np.array([3, 10])
plt.plot(x, y)
plt.show()

# Draw two points in the diagram, one at position (1, 3), (3,6), (5,8) and one in position (8, 10):
x = np.array([1, 3, 5, 8])
y = np.array([3, 6, 8, 10])
plt.plot(x, y, 'o')
plt.show()

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])
plt.plot(x, y)
plt.show()

# Plotting without x-points:
y = np.array([3, 8, 1, 10, 5, 7])
plt.plot(y)
plt.show()

# Markers:-> The keyword argument marker to emphasize each point with a specified marker
# Mark each point with a circle:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
# Mark each point with a star
plt.plot(ypoints, marker = '*')
plt.show()

# Format Strings fmt
# This parameter is also called fmt, and is written with this syntax:
# marker|line|color
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o-g')
plt.show()

# Marker Size
# You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
# Set the size of the markers to 20:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = "o", ms=20)
plt.show()

# Marker Color
# Set the EDGE color to red:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# Set the FACE color to red:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

# Line Width
# You can use the keyword argument linewidth or the shorter lw to change the width of the line.
# The value is a floating number, in points:
# Plot with a 20.5pt wide line:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '20.5')
plt.show()

# Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:
# Draw two lines by specifying a plt.plot() function for each line:
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()

# Add labels to the x- and y-axis:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

# Add a plot title and labels for the x- and y-axis:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

# Set Font Properties for Title and Labels
# You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.show()

# Position the Title You can use the loc parameter in title() to position the title.
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
# Position the title to the left:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data", loc = 'right')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.show()

# Add grid lines to the plot:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid()
# plt.grid(axis = 'x')
# plt.grid(axis = 'y')
plt.show()

# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

# Draw 2 plots:
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.show()

# Draw 6 plots:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()

# Create random arrays with 100 values for x-points, y-points, colors and sizes:
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()

# Draw 4 "hot pink" bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

# pie chart
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 