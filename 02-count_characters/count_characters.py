'''
Create a program that prompts for an input string 
and dis- plays output that shows the input string 
and the number of characters the string contains.
'''
input_string = ''
while input_string == '':
    input_string = input('Please enter a string > ').strip()
    
output_string = '{} has {} letters.'.format(input_string, len(input_string))
print(output_string)
