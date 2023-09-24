import random
import string
import argparse

def generate_password(length, num_special_chars, num_capital_letters):
    if length < num_special_chars + num_capital_letters:
        print("Error: The sum of special characters and capital letters exceeds the password length.")
        return

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    special_chars = string.punctuation

    pool = lowercase_letters + uppercase_letters + special_chars


    password = [random.choice(lowercase_letters) for _ in range(length)]

    for _ in range(num_capital_letters):
        index = random.randint(0, length - 1)
        password[index] = random.choice(uppercase_letters)


    for _ in range(num_special_chars):
        index = random.randint(0, length - 1)
        password[index] = random.choice(special_chars)

    random.shuffle(password)

    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("-l", "--length", type=int, help="Length of the password", required=True)
    parser.add_argument("-s", "--special", type=int, help="Number of special characters", required=True)
    parser.add_argument("-c", "--capital", type=int, help="Number of capital letters", required=True)
    args = parser.parse_args()

    password = generate_password(args.length, args.special, args.capital)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
