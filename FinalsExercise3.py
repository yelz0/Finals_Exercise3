def main():
    filename = "users.txt"

    try:
        username = input("Enter your Username: ")
        age = int(input("Enter your age: "))
        
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")
            
    except ValueError:
        print("Error: Please enter a valid numerical age.")
           
    else:
        print("\nDetails saved successfully!:)")
    
        
    finally:
        print("\nDisplaying content:")
        
        try:
            with open(filename, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("The file is empty or does not exist.")
            
main()
