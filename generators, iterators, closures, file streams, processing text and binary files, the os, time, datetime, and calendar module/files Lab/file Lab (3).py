import string

def letter_count(file_name):
    # Open the file and read its contents
    with open(file_name, 'r') as file:
        text = file.read()

    # Initialize a dictionary to store the letter counts
    letter_counts = {letter: 0 for letter in string.ascii_letters}

    # Iterate through each character in the text and update the letter counts
    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_counts[char] += 1

    # Sort the letter counts based on frequency
    letter_counts = {k: v for k, v in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)}

    # Create the output file with the '.hist' suffix
    output_file = file_name.split(".")[0] + ".hist"

    # Open the output file and write the histogram
    with open(output_file, 'w') as file:
        for letter in letter_counts:
            if letter_counts[letter] > 0:
                file.write(letter + '--> ' + str(letter_counts[letter]) + "\n")

# Ask the user for the input file's name
file_name = input("Enter the input file's name: ")

# Call the letter_count function
letter_count(file_name)
