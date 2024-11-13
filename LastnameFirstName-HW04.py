"""Homework 4 

Name: Izail Chamberlain
Lab Section: 11
Submission Date: 11.13.24
Sources, help given to/received from: ChatGPT to clarify command descriptions

You will be reading from and writing to a file.
You will read from prompt.txt Download prompt.txt.c
You will write to a file called "out.txt".

Look at prompt.txt to understand its structure.

It contains key-value pairs on each line of the file.
The keys are 'w' and '*'.
'w' stands for white space, and '*' is an asterisk (*).
The numeric value shows how many of each of those characters there are for each line in your output file.
Each line in prompt.txt corresponds to one line in out.txt.

For example, the line:
"w:101    *:020    w:026    *:004    w:017    *:030"
You will output a line with 101 white spaces, 20 asterisks, 26 white spaces, 4 asterisks, 17 white spaces, and 30 asterisks.
All of that will be on ONE line of your output file.

Each of the key-value pairs is separated by a tab '\t' character.
The key values are separated by a ':' character.

You can use the .split() function on strings to create a list. For example, pairs = line.split("\t") will give you a list of all the pairs in a line.

You can multiply strings by an integer, x, to create a string repeated x times. So, string_val = "*" * 10 would create a string with 10 asterisks: "**********".

You will be outputting a VERY recognizable ASCII art with this. If you are looking at the output file and you aren't sure what it is, you are likely doing it incorrectly. It can help if you zoom out on your output file.

Submit your file named as: LastnameFirstName-HW04.py

Your python file must include the standard required comments at the top of your file.

Name

Lab Section

Submission Date

Sources, help given to/received from"""

from pathlib import Path

input_path = Path('data/prompt.txt')
output_path = Path('data/out.txt')

# Reads the contents of the input file
contents = input_path.read_text()

# Initializes a list to hold each formatted line for output
output_lines = []

# Processes each line in the input file
for line in contents.splitlines():
    # Splits by tab to get key-value pairs
    pairs = line.split('\t')
    formatted_line = ''
    
    for pair in pairs:
        # Check if ':' exists in pair to avoid errors
        if ':' in pair:
            # Splits by ':' to get the key and the number of characters
            key, count = pair.split(':')
            count = int(count)
            
            # Appends spaces or asterisks based on the key
            if key == 'w':
                formatted_line += ' ' * count
            elif key == '*':
                formatted_line += '*' * count
    
    # Adds the formatted line to the output list
    output_lines.append(formatted_line)

# Writes all lines to the output file
output_path.write_text('\n'.join(output_lines))
#Confirms generation from file
print("ASCII art generated and saved to out.txt") 




