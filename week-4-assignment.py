
# Function to modify a file by converting its content to uppercase
def modify_file():
    while True:
        # Prompting a user for the input filename
        input_file = input("Enter the input filename: ")
        
        try:
            # Open the input file for reading
            with open(input_file, 'r') as infile:
                # Read the file content
                content = infile.read()
            
            # Modify the content (e.g., convert to uppercase)
            modified_content = content.upper()
            
            # Prompt the user for the output filename
            output_file = input("Enter the output filename: ")
            
            # Open the output file for writing
            with open(output_file, 'w') as outfile:
                # Write the modified content
                outfile.write(modified_content)
            
            print(f"File '{input_file}' has been modified and saved as '{output_file}'.")
            break  # Exit the loop after successful processing
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' does not exist. Please try again.")
        except IOError as e:
            print(f"An I/O error occurred: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# Run the program
modify_file()
