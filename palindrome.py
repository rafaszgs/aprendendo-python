palavra = input ("palavra: ")
palindrome = palavra == palavra[::-1]
print (f"{palavra} e palindromo?")
print (palindrome)