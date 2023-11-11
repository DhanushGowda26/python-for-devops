text="hello@123.com"
text1="madam"
text2="triangle"
text3="intgeral"

def reverse_string(text):
    return text[::-1]

def check_palindrome(text1):
    return text1==text1[::-1]

def check_anagram(text2,text3):
    return sorted(text2)==sorted(text3)

def only_alpha(text):
    new_text=''.join(char for char in text if char.isaplha())
    return new_text

def only_digit(text):
    new_text=''.join(char for char in text if char.isdigit())
    return new_text

def only_alph_num(text):
    new_text=''.join(char for char in text if char.isalnum())
    return new_text

def only_symbols(text):
    new_text=''.join(char for char in text if not char.isalnum())
    return new_text

