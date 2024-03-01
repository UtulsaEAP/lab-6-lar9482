"""
    Name: Luke Runnels
    Lab Time: 3/1/2024
"""

def process_and_print(input_string):
    # Split into separate strings
    numTokens = input_string.split(" ")

    # Convert strings to integers and filter out negative values
    negNums = []
    for numToken in numTokens:
        num = int(numToken)
        if (num < 0):
            negNums.append(num)

    # Sort integers in reverse order
    negNums.sort()

    output = ""

    # Print sorted integers
    for i in range(len(negNums)-1, -1, -1):
        output += f'{negNums[i]} '
    
    print(output, end="")
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
