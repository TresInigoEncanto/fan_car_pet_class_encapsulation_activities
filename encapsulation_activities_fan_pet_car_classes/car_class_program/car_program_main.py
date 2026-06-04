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

if __name__ == "__main__":
    main()
