import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length >= 4:
                return length
            else:
                print("Password length must be at least 4.")
        except ValueError:
            print("Please enter a valid number.")


def get_complexity_choice():
    print("\nSelect password complexity:")
    print("1. Lowercase letters only")
    print("2. Uppercase and lowercase letters")
    print("3. Letters and numbers")
    print("4. Letters, numbers, and special characters")

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in {"1", "2", "3", "4"}:
            return int(choice)
        else:
            print("Invalid choice. Please select between 1 and 4.")


def build_character_pool(choice):
    if choice == 1:
        return string.ascii_lowercase
    elif choice == 2:
        return string.ascii_lowercase + string.ascii_uppercase
    elif choice == 3:
        return string.ascii_lowercase + string.ascii_uppercase + string.digits
    else:
        return (
            string.ascii_lowercase +
            string.ascii_uppercase +
            string.digits +
            string.punctuation
        )


def generate_password(length, characters):
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password


def main():
    print("----- PASSWORD GENERATOR -----")

    length = get_password_length()
    complexity = get_complexity_choice()
    characters = build_character_pool(complexity)

    password = generate_password(length, characters)
    print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()
