from fan_class_program_functionality import Fan

def TestFan():
    fan1 = Fan(speed=Fan.FAST, radius = 10, color = 'yellow', on = True)
    fan2 = Fan(speed=Fan.MEDIUM, radius = 5, color = 'blue', on = False)

    print("--- Fan 1 Properties ---")
    print(f"speed: {fan1.get_speed()}")
    print(f"radius: {fan1.get_radius()}")
    print(f"color: {fan1.get_color()}")
    print(f"on: {fan1.get_on()}")

    print("\n--- Fan 2 Properties ---")
    print(f"speed: {fan2.get_speed()}")
    print(f"radius: {fan2.get_radius()}")
    print(f"color: {fan2.get_color()}")
    print(f"on: {fan2.get_on()}")

    print("\n--- Running Sync Feature (Test) ---")

    workout_sync = Fan()

    user_minutes = int(input("Enter minutes: "))
    user_seconds = int(input("Enter seconds: "))

    workout_sync.runners_pace(minutes = user_minutes, seconds = user_seconds)
    print(f"Fan Speed Set To: {workout_sync.get_speed()}")

if __name__ == "__main__":
    TestFan()