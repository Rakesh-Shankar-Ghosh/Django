import random

def generate_password(password_length):
  """Generates a random password."""
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{[]}\|;:'\",./<>?"
  length = int(password_length)
  password = ""
  for _ in range(length):
    password += random.choice(characters)
  return password

def main():
  """Generates and prints a random password."""
  print("Input Length of Password")
  length = input()
  password = generate_password(length)
  print("your Password is:=>>",password)

if __name__ == "__main__":
  print("Welcome to Passsword Generator__TASK_02")
  main()
