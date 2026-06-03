from car_class_program_functionality import Car

def main():
    my_car = Car(2026, "Toyota Corolla")

    print("--- Acceleration ---")

    for i in range(5):
        my_car.accelerate()
        print(f"Current speed after call {i+1}: {my_car.get_speed()}")

if __name__ == "__main__":
    main()
