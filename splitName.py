# Take user input for full name
full_name = input("Enter your full name: ")

# Split the full name into first name and last name
name_parts = full_name.split()

# Check if at least two parts (first name and last name) are provided
if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = ' '.join(name_parts[1:])  # Handling multiple-word last names
    print("First Name:", first_name)
    print("Last Name:", last_name)
else:
    print("Invalid input. Please enter both first name and last name.")
