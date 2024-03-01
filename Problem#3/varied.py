"""
    Name: Luke Runnels
    Lab Time: 3/1/2024
"""

def process_input(input_string):
    # Split into separate strings

    floatTokens = input_string.split(" ")
    # Convert strings to floats
    
    floatNums = []
    for floatToken in floatTokens:
        floatNums.append(float(floatToken))

    # Get max and average
    max_value = max(floatNums)
    average_value = sum(floatNums) / len(floatNums)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
