import re
import os
from pathlib import Path
import shutil

# Make a dictionary with files which we want to search
type_of_files = { "images" : [],
                  "documents" : [],
                  "audio" : [],
                  "video" : [],
                  "archives" : []
                  }
# Make lists with different extensions of files
img = ['.jpeg', '.png', '.jpg', '.svg']
vid = ['.avi', '.mp4', '.mov', '.mkv']
doc = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
aud = ['.mp3', '.ogg', '.wav', '.amr']
arch = ['.zip', '.gz', '.tar']

# Function which create folderr in accordance with dictionary: type_of_files
def create_folders_from_list(folder_path, folder_names):

    for folder in folder_names:

        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')

# The main function which normalize and sort folders and files
def folder_check(p):

    for item in p.iterdir():        
        if item.is_dir():

            if item.name !='images'and item.name !='video'and item.name !='documents'and item.name !='audio'and item.name !='archives':

                new_folder_name = normalize(item.name)
                updated_folder_path = Path(f'{item.parent}/{new_folder_name}')
                os.rename(item, updated_folder_path)
                folder_check(updated_folder_path)

        elif item.is_file():
            sorter_of_files(item)

def sorter_of_files(p):

    ext = p.suffix
    name = p.stem
    normalized_name = normalize(name)
    updated_path = p.rename(Path(p.parent, normalized_name + ext))

    if ext.casefold() in img:
        type_of_files['images'].append(normalized_name + ext)        
        shutil.move(f'{p.parent}/{normalized_name}{ext}', f'{SORTING_FOLDER}/images/{normalized_name}{ext}')

    elif ext.casefold() in vid:
        type_of_files['video'].append(normalized_name + ext)        
        shutil.move(f'{p.parent}/{normalized_name}{ext}', f'{SORTING_FOLDER}/video/{normalized_name}{ext}')

    elif ext.casefold() in doc:
        type_of_files['documents'].append(normalized_name + ext)        
        shutil.move(f'{p.parent}/{normalized_name}{ext}', f'{SORTING_FOLDER}/documents/{normalized_name}{ext}')

    elif ext.casefold() in aud:
        type_of_files['audio'].append(normalized_name + ext)       
        shutil.move(f'{p.parent}/{normalized_name}{ext}', f'{SORTING_FOLDER}/audio/{normalized_name}{ext}')

    elif ext.casefold() in arch:
        type_of_files['archives'].append(normalized_name + ext)
        
        if not os.path.exists(f'{SORTING_FOLDER}/archives/{normalized_name}'):

            os.mkdir(f'{SORTING_FOLDER}/archives/{normalized_name}')
        shutil.unpack_archive(updated_path, f'{SORTING_FOLDER}/archives/{normalized_name}')
        
#Function delete empty folders
def remove_empty_folders(p):

    for item in os.listdir(p):
        a = os.path.join(p, item)
        if os.path.isdir(a) and item !='images'and item !='video'and item !='documents'and item !='audio'and item !='archives':
            remove_empty_folders(a)
            if not os.listdir(a):
                os.rmdir(a)
                

#Function makes transliteration from cyryllic
def normalize(name):

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):

      TRANS[ord(c)] = l
      TRANS[ord(c.upper())] = l.upper()

    result = name.translate(TRANS)    
    result = re.sub("[^0-9a-zA-Z]+", "_", result)
    return result

p = Path(input("Enter the directory path: "))
SORTING_FOLDER = p

create_folders_from_list(p, type_of_files)
folder_check(p)
remove_empty_folders(p)


        

    
