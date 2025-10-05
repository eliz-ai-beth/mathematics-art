#ripples.py


import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------
# PARAMETERS (change these to customize)
# ------------------------------------------------------
N = 2000                  # number of steps
k = np.linspace(-10000, 10000, N)  # range for horizontal spread
circle_points = 200       # resolution of each circle (more points = smoother)
line_color = "black"      # color of circle outlines
line_width = 0.1          # thickness of the lines
save = False              # set True to save output as PNG
outfile = "ripples.png"   # filename if saving
dpi = 600                 # resolution of saved image



# ------------------------------------------------------
# EQUATIONS
# ------------------------------------------------------
# A(k): horizontal displacement of circles (creates arches left/right)
A = 0.6 * np.sin(2*np.pi*k/2500) * np.exp(-np.abs(k)/6000)

# B(k): vertical displacement (the "spine" stacking circles up/down)
B = k / 5000

# R(k): radius of each circle (controls ripple thickness and taper)
R = (0.05
     + 0.1 * np.cos(2*np.pi*k/369)**21
     * (1 - np.abs(k)/1000))



# ------------------------------------------------------
# PLOTTING
# ------------------------------------------------------
fig, ax = plt.subplots(figsize=(4,6), dpi=120)
theta = np.linspace(0, 2*np.pi, circle_points)

# Loop through all steps to draw circles one by one
for i in range(len(k)):
    x = A[i] + R[i]*np.cos(theta)   # x-coordinates of circle
    y = B[i] + R[i]*np.sin(theta)   # y-coordinates of circle
    ax.plot(x, y, color=line_color, linewidth=line_width)



# ------------------------------------------------------
# FORMATTING 
# ------------------------------------------------------
ax.set_aspect("equal", adjustable="box")  # keep circles round
ax.axis("off")                            # hide axes and ticks
plt.tight_layout(pad=0)



# ------------------------------------------------------
# SAVE OR SHOW
# ------------------------------------------------------
if save:
    plt.savefig(outfile, dpi=dpi, bbox_inches="tight", pad_inches=0)
plt.show()
