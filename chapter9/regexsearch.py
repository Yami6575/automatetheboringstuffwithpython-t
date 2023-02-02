
import os
import re


word = input('Word to search: ')
regex = re.compile(f"{word}")


def find_regex(directory):
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            
            with open(directory+'/'+file) as text_file:
                text = text_file.read()
                text_file.close()   
            found_words = regex.findall(text)
            
            if not found_words:
                continue
            else:
                for i in found_words:
                    print(file + ":\n" + i, end='\n\n')


find_regex(input('Enter Directory: '))