WIDTH = 500
HEIGHT = 500
PACMAN_HEIGHT = 100
PACMAN_WIDTH = 100
SPEED = 3
MAX_ANGLE = 45
MIN_ANGLE = 0
MOUTH_RIGHT_BEGIN_ANGLE = 0
MOUTH_RIGHT_END_ANGLE = 360
MOUTH_DOWN_BEGIN_ANGLE = 90
MOUTH_DOWN_END_ANGLE = 450
MOUTH_LEFT_BEGIN_ANGLE = 180
MOUTH_LEFT_END_ANGLE = 540
MOUTH_UP_BEGIN_ANGLE = -90
MOUTH_UP_END_ANGLE = 270
x = WIDTH/2
y = HEIGHT/2
speed_angle = -2
x_add = 0
y_add = 0
angle_add = 0



def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    fill(1.0, 1.0, 0.0)
    noStroke()

def draw():
    global x, y, speed_angle, angle_add  # Must be declared as global
    background(0)

    x = x + x_add
    y = y + y_add
    
    # The following cases seal with mouse open
    # with differnt direction
    if (angle_add >= MAX_ANGLE or angle_add <= MIN_ANGLE):
        speed_angle = -speed_angle
    angle_add = angle_add + speed_angle

    # The following cases deal with when PacMan
    # is near the edge of the screen
    
    # If PacMan moves completely behond the right edge 
    if (x > WIDTH + (PACMAN_WIDTH/2)): 
        # Reset the x value to the left side
        x = PACMAN_WIDTH/2
    # If PacMan is overlapping the right edge
    elif (x > WIDTH - (PACMAN_WIDTH/2)):
        # draw a second PacMan on the left side, also
        # overlapping
        pacman(x - WIDTH, y)
    
    # If PacMan moves past the bottom edge, 
    # redraw at the top
    if (y > HEIGHT + (PACMAN_HEIGHT/2)):
        y = PACMAN_HEIGHT/2
    elif (y > HEIGHT - (PACMAN_HEIGHT/2)):
        pacman(x, y - HEIGHT)
        
    # If PacMan moves past the left edge, 
    # redraw at the right   
    if (x < -(PACMAN_WIDTH/2)): 
        x = WIDTH - (PACMAN_WIDTH/2)
    elif (x < PACMAN_WIDTH/2):
        pacman(x + WIDTH, y)
    
    # If PacMan moves past the top, redraw at bottom
    if (y < -(PACMAN_HEIGHT/2)):
        y = HEIGHT - (PACMAN_HEIGHT/2)
    elif (y < PACMAN_HEIGHT/2):
        pacman(x, y + HEIGHT)
    
    # Always draw PacMan at his real current location.
    pacman(x, y)

def pacman(x, y):
    """Draw PacMan to the screen"""
    # Use global variables as necessary
    if (x_add < 0):
        start_angle = MOUTH_LEFT_BEGIN_ANGLE
        end_angle = MOUTH_LEFT_END_ANGLE
    elif (y_add > 0):
        start_angle = MOUTH_DOWN_BEGIN_ANGLE
        end_angle = MOUTH_DOWN_END_ANGLE
    elif (y_add < 0):
        start_angle = MOUTH_UP_BEGIN_ANGLE
        end_angle = MOUTH_UP_END_ANGLE
    else:
        start_angle = MOUTH_RIGHT_BEGIN_ANGLE
        end_angle = MOUTH_RIGHT_END_ANGLE

    start_angle = start_angle + angle_add
    end_angle = end_angle - angle_add
    arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, 
        radians(start_angle), 
        radians(end_angle))
    
def keyPressed():
    global x_add, y_add  # Must be declared as global
    if (key == CODED):
        if (keyCode == DOWN):
            x_add = 0
            y_add = SPEED
        elif (keyCode == UP):
            x_add = 0
            y_add = -(SPEED)
        elif (keyCode == LEFT):
            x_add = -(SPEED)
            y_add = 0
        elif (keyCode == RIGHT):
            x_add = SPEED
            y_add = 0
