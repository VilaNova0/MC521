def calcAngle(hour, minute):
    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute

    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)

    return angle

def check_angle(angle) -> bool:
    for hour in range(0, 12):
        for minute in range(0, 60):
            if calcAngle(hour, minute) == angle:
                return True
    return False

while True:
    try:
        angle = int(input())
        if angle % 6:
            print('N')
        else:
            dist = angle // 6
            if check_angle(angle):
                print('Y')
            else:
                print('N')
    except EOFError:
        break