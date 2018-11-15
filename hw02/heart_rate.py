def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    #compute the maximum heart rate and the heart rate reserve
    heart_rate_max  = 208 - 0.7 * age
    reserve =  heart_rate_max - restHR

    print("Your heart rate reserve is:", reserve, "bpm")

    #Different zones
    #Zone 1: 50% -60%, Zone 2: 60%-70%, Zone 3: 70%-80%, Zone 4: 80%-93%, Zone 5: 93%-100%
    
    rate_zone1_low = restHR + reserve * 0.5
    rate_zone1_high = restHR + reserve * 0.6
    rate_zone2_high = restHR + reserve * 0.7
    rate_zone3_high = restHR + reserve * 0.8
    rate_zone4_high = restHR + reserve * 0.93
    rate_zone5_high = restHR + reserve

    print("Here is a breakdown of your training zones:")
    print("Zone 1:", round(rate_zone1_low,2),"to",round(rate_zone1_high,2),"bpm\n"
          "Zone 2:", round(rate_zone1_high,2),"to",round(rate_zone2_high,2),"bpm\n"
          "Zone 3:",round(rate_zone2_high,2),"to",round(rate_zone3_high,2),"bpm\n"
          "Zone 4:",round(rate_zone3_high,2),"to",round(rate_zone4_high,2),"bpm\n"
          "Zone 5:",round(rate_zone4_high,2),"to",round(rate_zone5_high,2),"bpm" )


    print("=======================================")

main()