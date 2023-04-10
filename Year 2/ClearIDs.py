import os
import re

markdown_files = []

# Define the path to the python files directory
python_files_dir_path = "/path/to/python/files/directory"

for dirpath, dirnames, filenames in os.walk('C:/uni stuff/Flashcards-uni-aero-astrp/Year 2'):
    for name in filenames: 
        if name.endswith(".md"):
            markdown_files.append(os.path.join(dirpath, name))


def remove_regex_matches(pattern, string):
    # compile the regex pattern for performance
    regex = re.compile(pattern)
    # use sub() function to replace all matches with empty string
    return regex.sub("", string)

def replace_words(file_location):
    text2 = ""
    found = False 
    with open(file_location, 'r', encoding="Latin-1") as f:
        text = f.read(  )
        text2 = remove_regex_matches( "(\<!--).+?(--\>\n)", text )
        if ( text != text2 ):
            found = True 

    if ( found ):
        with open(file_location, 'w', encoding="Latin-1") as f:
            f.write(text2)
        print("Replaced at: \t",location)


input("Confirm deletion of all ID's in the markdown files")

for location in markdown_files:
    replace_words( location )

input("Done")