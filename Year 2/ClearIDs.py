import os

markdown_files = []

# Define the path to the python files directory
python_files_dir_path = "/path/to/python/files/directory"

for dirpath, dirnames, filenames in os.walk('C:/uni stuff/Flashcards-uni-aero-astrp/Year 2'):
    for name in filenames: 
        if name.endswith(".md"):
            markdown_files.append(os.path.join(dirpath, name))

searchRegex = "ABFALolmao"

def replace_words(file_location):
    text = ""
    found = False 
    with open(file_location, 'r', encoding="Latin-1") as f:
        text = f.read(  )
        if ( text.find( searchRegex ) != -1 ):
            found = True
            text = text.replace( searchRegex, "lmao")

    if ( found ):
        with open(file_location, 'w', encoding="Latin-1") as f:
            f.write(text)
        print("Replaced at: \t",location)


for location in markdown_files:
    replace_words( location )

input("Done")