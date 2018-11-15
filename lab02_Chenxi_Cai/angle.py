import math
#  Input an angle in degrees
#  prints out the sine and cosine values for the angle
def main():
    angle_deg = float(input(' Enter an angle: '))
    angle_rad = math.radians(angle_deg)

    angle_sin = math.sin(angle_rad)
    angle_cos = math.cos(angle_rad)

    print('The cosine of', angle_deg, 'is', angle_cos)
    print('The sine of', angle_deg,'is',angle_sin)

main()