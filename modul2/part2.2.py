# string format

# method format

my_str = 'text {}'
print(my_str.format('''example'''))
my_str = 'text {1} {0}'
print(my_str.format('example1' , 'example2'))
my_str = 'text {ex1} {ex2}'
print(my_str.format(ex1 = 'example1' , ex2 = 'example2'))
my_str = 'text {ex1} {ex2}'
print(my_str.format(ex1 = 'example1' , ex2 = 'example2'))

print(80 *"#")

#formated string
ex1 = 'example1'
ex2 = 'example2'
print(f"text2 {ex1}")
print(f"text2 {2}")

#len function

ex1 = 'example1'
print(len(ex1))

# index of string

hello = 'hello world'
        #012345678910
print(hello[3:7]) # last index not included
print(hello[0:11:2]) #not all versions of python 3
print(hello[::2])

#hello = 'h e l l o   w o r l d'
    #    -10-9-8-7-6-5-4-3-2-1
print(hello[::-1])
print(hello[-5::1])
print('negative step')
print(hello[-5:-1:-1])
