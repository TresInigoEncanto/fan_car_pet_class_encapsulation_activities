class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, on = False, radius = 5.0, color = 'blue'):
        self.__speed = speed
        self.__on = on
        self.__radius = float(radius)
        self.__color = color