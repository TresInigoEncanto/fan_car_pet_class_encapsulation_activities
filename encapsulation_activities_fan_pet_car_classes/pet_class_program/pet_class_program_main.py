from pet_class_program_functionality import Pet

def main():
    input_name = input("Enter your pet's name: ")
    input_animal_type = input("Enter your pet's animal type: ")
    input_age = input("Enter your pet's age (Ex: 1 year): ")

    my_pet = Pet(input_name, input_animal_type, input_age)

    print("\n--- Your Pet's Information ---")
    print("Your pet's name is", my_pet.get_name())
    print("Your pet is a", my_pet.get_animal_type())
    print("Your pet is", my_pet.get_age(), "old")

    print("\n--- Outdoor Stroll With Your Pets Feature ---")

    run_minutes = int(input("How many minutes did you run with your pet? "))

    pet_type = my_pet.get_animal_type().lower()

    if "dog" in pet_type:
        multiplier = 0.15

    elif "cat" in pet_type:
        multiplier = 0.5
    
    else:
        multiplier = 0.10

    distance_covered = run_minutes * multiplier

    print(f"\nWorkout Complete")
    print(f"Because {my_pet.get_name()} is a {my_pet.get_animal_type()}, your walk/run had a great pace!")
    print(f"Approximate distance covered of your run/walk: {distance_covered:.2f} km, good job!")

if __name__ == "__main__":
    main()