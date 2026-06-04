from pet_class_program_functionality import Pet

def main():
    input_name = input("Enter your pet's name: ")
    input_animal_type = input("Enter your pet's animal type: ")
    input_age = input("Enter your pet's age: ")

    my_pet = Pet(input_name, input_animal_type, input_age)

    print("\n--- Your Pet's Information ---")
    print("Your pet's name is", my_pet.get_name())

if __name__ == "__main__":
    main()