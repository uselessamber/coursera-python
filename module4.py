# Question 1
#
# The format_address function separates out parts of the address string into new strings: 
# house_number and street_name, and returns: 
# "house number X on street named Y". 
# The format of the input string is: numeric house number, 
# followed by the street name which may contain numbers, 
# but never by themselves, and could be several words long. 
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 
# Fill in the gaps to complete this function.

def format_address(address_string):
    # Declare variables

    # Separate the address string into parts

    # Traverse through the address parts
    args = []
    cw = ""
    for c in address_string:
        if c != " ":
            cw += c
        else:
            args.append(cw)
            cw = ""
        pass
    if cw != "":
        args.append(cw)
        cw = ""

    # Determine if the address part is the
    # house number or part of the street name
    
    house_number = args[0]
    street_name = ""
    for i in range(1, len(args)):
        street_name += args[i] + " "
    street_name = street_name[:-1]
        

    # Does anything else need to be done 
    # before returning the result?
  
    # Return the formatted string  
    return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

# Problem 2
# The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Can you write this function in just one line?

def highlight_word(sentence, word):
	return 

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
