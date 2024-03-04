test = 'Hello World'

encpripted_test = ''
for letter in test:
    encpripted_test += chr(ord(letter)^200)
print(encpripted_test)

decripted_test = ''
for letter in encpripted_test:
    decripted_test += chr(ord(letter)^200)
print(decripted_test)