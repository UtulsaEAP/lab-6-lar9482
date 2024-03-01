"""
    Name: Luke Runnels
    Lab Time: 3/1/2024
"""

def process_user_contacts(user_input):

    nameAndPhoneTokens = user_input.split(" ")
    nameAndPhoneDict = {}
    
    for nameAndPhoneToken in nameAndPhoneTokens:
        nameToken = nameAndPhoneToken.split(",")[0]
        phoneToken = nameAndPhoneToken.split(",")[1]

        nameAndPhoneDict[nameToken] = phoneToken
         
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    if (nameAndPhoneDict.get(contact_name) is None):
        print("Contact not found.")
    else:
        print(nameAndPhoneDict[contact_name])
        
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
