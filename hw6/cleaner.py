from pathlib import Path
import os
import shutil
import re

folders_and_formats = {'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
           'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
          'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
          'video': ('AVI', 'MP4', 'MOV', 'MKV'),
           'archives': ('ZIP', 'GZ', 'TAR')
}



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

def delete_empty_folders(path):

    for way in path.iterdir():
        if way.is_dir() and way.name not in folders_and_formats:
            delete_empty_folders(Path(f'{path}/{way.name}'))
            if not os.listdir(way):
                os.rmdir(way)



def create_folders(path):
    for folder in folders_and_formats.keys():
        if not os.path.exists(f'{path}/{folder}'):
            os.mkdir(f'{path}/{folder}')



def sort_files(path, anchor_path):

    for way in path.iterdir():
        #print(way)
        if way.is_dir() and way.name not in folders_and_formats:

            sort_files(Path(f'{path}/{way.name}'), anchor_path)

        elif way.is_file():
            ext = way.suffix.replace('.', '').upper()
            if ext in folders_and_formats['images']:

                os.replace(way, f'{anchor_path}/images/{way.name}')
            elif ext in folders_and_formats['video']:


                os.replace(way, f'{anchor_path}/video/{way.name}')
            elif ext in folders_and_formats['documents']:

                os.replace(way, f'{anchor_path}/documents/{way.name}')
            elif ext in folders_and_formats['audio']:

                os.replace(way, f'{anchor_path}/audio/{way.name}')
            elif ext in folders_and_formats['archives']:

                new_path = f'{anchor_path}/archives/{way.name}'
                os.replace(way, new_path)
                name_for_moving = Path(new_path).name


                shutil.unpack_archive(new_path, f'{Path(new_path).parent}/{Path(name_for_moving).stem}/')






def main():
    p = Path('/home/vk/Рабочий стол/dump')
    anchor_path = p
    #create_folders(p)
    sort_files(p, anchor_path)
    delete_empty_folders(p)

    #p = Path(input('Enter the path to the folder which you want to clean: '))







if __name__ == '__main__':
    main()