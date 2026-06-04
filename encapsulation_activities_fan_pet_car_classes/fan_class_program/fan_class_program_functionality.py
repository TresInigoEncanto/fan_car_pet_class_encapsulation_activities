class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, on = False, radius = 5.0, color = 'blue'):
        self.__speed = speed
        self.__on = on
        self.__radius = float(radius)
        self.__color = color

    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
    
    def get_speed(self):
        return self.__speed
    
    def set_on(self, on):
        self.__on = on
    
    def get_on(self):
        return self.__on
    
    def set_radius(self, radius):
        self.__radius = float(radius)
    
    def get_radius(self):
        return self.__radius
    
    def set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color

    def runners_pace(self, minutes, seconds):
        """
        Adjusts fan speed based on the runner's pace.
        Faster running pace = stronger fan winds
        """

        total_pace = minutes + (seconds / 60.0)

        self.set_on(True)

        if total_pace <= 5.0:
            self.set_speed(Fan.FAST)
            print(f"[Workout] High Intensity Pace: {minutes}:{seconds:02d}/km")

        elif total_pace <= 6.5:
            self.set_speed(Fan.MEDIUM)
            print(f"[Workout] Moderate Tempo Pace: {minutes}:{seconds:02d}/km")
        
        else:
            self.set_speed(Fan.SLOW)
            print(f"[Workout] Easy Recovery Pace: {minutes}:{seconds:02d}/km")
