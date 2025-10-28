"""
Palindrome Permutation: Given a string, 
write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words

"""

def Palindrome_Permutation(string):
    string = string.lower()
    seen = {}
    
    for chr in string:
        if chr != " ":
            seen[chr] = seen.get(chr,0) + 1

    print(seen)

    odd_count = 0
    for count in seen.values():

        if count % 2 != 0:
            odd_count += 1 

        if odd_count > 1:

            return False
        
    return True

string = "aat"
print(Palindrome_Permutation(string))