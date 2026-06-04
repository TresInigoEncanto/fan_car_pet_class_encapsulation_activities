from car_class_program_functionality import Car

def main():
    my_car = Car(2026, "Toyota Corolla")

    print("--- Acceleration ---")

    for i in range(5):
        my_car.accelerate()
        print(f"Current speed after accelerate call {i+1}: {my_car.get_speed()}")
    
    print("\n--- Brake ---")
    
    for i in range(5):
        my_car.brake()
        print(f"Current speed after brake call {i+1}: {my_car.get_speed()}")

    print("\n--- Pace Car Cruise Control ---")

    run_minutes = int(input("Enter target pace minutes per kilometer = ")) 
    
    run_seconds = int(input("Enter target pace seconds per kilometer = "))

    total_pace = run_minutes + (run_seconds / 60.0)

    print(f"Runner's Target Pace: {run_minutes}:{run_seconds:02d}/km")

    if total_pace <= 5.0:
        print("High Intensity Pace")
        target_speed = 25

    elif total_pace <= 6.5:
        print("Moderate Tempo Pace")
        target_speed = 15
    
    else:
        print("Easy Recovery Pace")
        target_speed = 5
    
    print(f"Pace car cruising to match runner's pace. Target speed; {target_speed} km/h")

    while my_car.get_speed() != target_speed:
        current = my_car.get_speed()

        if current < target_speed:
            my_car.accelerate()
        
        elif current > target_speed:
            my_car.brake()

    

if __name__ == "__main__":
    main()
