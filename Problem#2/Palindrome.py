"""
    Name: Luke Runnels
    Lab Time: 3/1/2024
"""

def check_palindrome(user_input):
    start = 0
    end = len(user_input) - 1

    while (start < end):
        if (user_input[start] != user_input[end]):
            print(f'not a palindrome: {user_input}')
            return

        start += 1

        end -= 1
    
    print(f'palindrome: {user_input}')

if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
