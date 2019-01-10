# -----------------------------------------------------------------------------
# Application Name: Level 10 Life
# By:               Zachery Hysong
#
# Project Started:  2019-01-03
# Last Update:      2019-01-03
#
# Description:      This application is a programming test to learn how to draw
#                   `Level 10` charts using pygame
#
# Todo:             Add Labels
#                   Find a way to fill in the shapes
#                   Create Readme
#                   Create and push Repo to GitHub
# -----------------------------------------------------------------------------

# ------------------------------------------------- # Import Packages ---------
import pygame                                       # Import 'pygame'
import math                                         # Import 'math'

# ------------------------------------------------- # Initialize Constants ----
BLACK = (0, 0, 0)                                   # Define BLACK
WHITE = (255, 255, 255)                             # Define WHITE
DARKGRAY = (20, 20, 20)                             # Define DARKGRAY
LIGHTGRAY = (60, 60, 60)                            # Define LIGHTGRAY
RED = (255, 0, 0)                                   # Define RED
ORANGE = (255, 128, 0)                              # Define ORANGE
YELLOW = (255, 255, 0)                              # Define YELLOW
LIGHTGREEN = (128, 255, 0)                          # Define LIGHTGREEN
GREEN = (0, 255, 0)                                 # Define GREEN
CYAN = (0, 255, 255)                                # Define CYAN
LIGHTBLUE = (0, 128, 255)                           # Define LIGHTBLUE
BLUE = (0, 0, 255)                                  # Define BLUE
PURPLE = (128, 0, 255)                              # Define PURPLE
MAGENTA = (255, 0, 128)                             # Define MAGENTA

# ------------------------------------------------- # Set pygame defaults -----
size = (500, 500)                                   # Define Screen Size
screen = pygame.display.set_mode((size))            # Set Screen Size

# ------------------------------------------------- # Create Background -------
background = pygame.Surface(screen.get_size())      # Set BG Surface
background = background.convert()                   # Optimise for performance
background.fill(DARKGRAY)                           # Fill Screen w/ White


# ------------------------------------------------- # Define degreesToRadians -
def degreesToRadians(deg):
    return deg/180.0 * math.pi                      # Return Angle as Degrees


# ------------------------------------------------- # Define drawCircleArc ----
def drawCircleArc(screen, color, center, radius,
                  startDeg, endDeg, thickness):
    (x, y) = center                                 # Define Center
    rect = (x-radius, y-radius,                     # Define start X and Y
            radius*2, radius*2)                     # Define End X and Y
    startRad = degreesToRadians(startDeg)           # Start Angle
    endRad = degreesToRadians(endDeg)               # End Angle
    pygame.draw.arc(screen, color, rect, startRad,  # Draw to Screen
                    endRad, thickness)


# ------------------------------------------------- # Define drawPieChart -----
def drawPieChart(color, x, y, radius, startDeg, endDeg, thickness):

    # --------------------------------------------- # Set Circle Variables ----
    circleCenterX = x                               # Set Center X
    circleCenterY = y                               # Set Center Y
    circleCenter = (circleCenterX, circleCenterY)   # Set Center Tuple
    circleRadius = radius                           # Set Radius
    circleStartDeg = startDeg                       # Set Starting Angle
    circleEndDeg = endDeg                           # Set Ending Angle
    circleThickness = thickness                     # Set Thickness

    # --------------------------------------------- # Set startLine Variables -
    startLineAngleAsRads = degreesToRadians(        # Get Angle as Rads
                           circleStartDeg)

    startLineX2 = (circleCenterX                    # Calculate End X
                   + math.cos(startLineAngleAsRads)
                   * circleRadius)
    startLineY2 = (circleCenterY                    # Calculate End Y
                   + math.sin(startLineAngleAsRads)
                   * -circleRadius)

    # --------------------------------------------- # Set endLine Variables ---
    endLineAngleAsRads = degreesToRadians(        # Get Angle as Rads
                           circleEndDeg)
    endLineX2 = (circleCenterX                      # Calculate End X
                 + math.cos(endLineAngleAsRads)
                 * circleRadius)
    endLineY2 = (circleCenterY                      # Calculate End Y
                 + math.sin(endLineAngleAsRads)
                 * -circleRadius)

    # --------------------------------------------- # Draw new Arc ------------
    drawCircleArc(background,                       # Set Background
                  color,                            # Set Color
                  circleCenter,                     # Set Center
                  circleRadius,                     # Set Radius
                  circleStartDeg,                   # Set Start Degrees
                  circleEndDeg,                     # Set End Degrees
                  circleThickness)                  # Set Thickness

    # --------------------------------------------- # Draw Starting Line ------
    pygame.draw.line(background,                    # Set Background
                     color,                         # Set Color
                     (circleCenterX,                # Set Start X
                      circleCenterY),               # Set Start Y
                     (startLineX2,                  # Set End X
                      startLineY2),                 # Set End Y
                     thickness)                     # Set Thickness

    # --------------------------------------------- # Draw Ending Line --------
    pygame.draw.line(background,                    # Set Background
                     color,                         # Set Color
                     (circleCenterX,                # Set Start X
                      circleCenterY),               # Set Start Y
                     (endLineX2,                    # Set End X
                      endLineY2),                   # Set End Y
                     thickness)                     # Set Thickness


for x in range(0, 10):
    # --------------------------------------------- # Draw the Base Circles ---
    loop1 = 1 * (x + 1)                             # Loop Incrementer
    pygame.draw.circle(background,                  # Set Surface
                       LIGHTGRAY,                   # Set Color
                       (250, 250),                  # Set Start X and Y
                       loop1 * 20,                  # Set Radius
                       1)                           # Set Thickness

    # --------------------------------------------- # Draw Division Line ------
    angle = 36 * (x + 1)                            # Set Angle
    angleRadians = degreesToRadians(angle)          # Convert to Radians
    X2 = 250 + (math.cos(angleRadians) * 200)       # Get X2
    Y2 = 250 + (math.sin(angleRadians) * 200)       # Get Y2
    pygame.draw.line(background,                    # Set Background
                     LIGHTGRAY,                     # Set Color
                     (250, 250),                    # Set Start X and Y
                     (X2, Y2),                      # Set End X and Y
                     1)                             # Set Thickness

drawPieChart(RED,                                   # Family & Friends
             250, 250, 60,  0,   36, 2)
drawPieChart(ORANGE,                                # Personal Development
             250, 250, 100, 36,  72, 2)
drawPieChart(YELLOW,                                # Spirituality
             250, 250, 20,  72,  108, 2)
drawPieChart(LIGHTGREEN,                            # Finances
             250, 250, 40,  108, 144, 2)
drawPieChart(GREEN,                                 # Career / School
             250, 250, 80,  144, 180, 2)
drawPieChart(CYAN,                                  # Relationships
             250, 250, 100, 180, 216, 2)
drawPieChart(LIGHTBLUE,                             # Fun / Recreation
             250, 250, 120, 216, 252, 2)
drawPieChart(BLUE,                                  # Giving and Contribution
             250, 250, 20,  252, 288, 2)
drawPieChart(PURPLE,                                # Home and Entertainment
             250, 250, 160, 288, 324, 2)
drawPieChart(MAGENTA,                               # Health and Fitness
             250, 250, 100, 324, 360, 2)

screen.blit(background, (0, 0))                     # Blit the background

pygame.display.set_caption("Level 10 Life")         # Set Screen Title
done = False                                        # Initialize Loop
clock = pygame.time.Clock()                         # Define Clock

# ------------------------------------------------- # Start Main Game Loop ----
while not done:                                     # Loop named Done
    for event in pygame.event.get():                # User did something
        if event.type == pygame.QUIT:               # If user clicked close
            done = True                             # Exit Loop
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect Mouse Down
            done = True                             # Exit Loop
    pygame.display.flip()                           # Update Display
    clock.tick(60)                                  # Limit to 60 FPS

# ------------------------------------------------- # Exit Main Game Loop -----

pygame.quit()                                       # Exit Game
