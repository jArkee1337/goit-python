from pathlib import Path
import os
import shutil
import re
import sys

folders_and_formats = {'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
                       'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
                       'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
                       'video': ('AVI', 'MP4', 'MOV', 'MKV'),
                       'archives': ('ZIP', 'GZ', 'TAR')
                       }
images_list = []
documents_list = []
audio_list = []
video_list = []
archives_list = []
unknown_files_list = []
set_of_extensions = set()
unknown_set_of_extensions = set()


def normalize(name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
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

        if way.is_dir() and way.name not in folders_and_formats:

            sort_files(Path(f'{path}/{way.name}'), anchor_path)

        elif way.is_file():
            ext = way.suffix.replace('.', '').upper()
            name_for_normalize = Path(way.name).stem
            normalized_name = f'{normalize(name_for_normalize)}.{ext.lower()}'

            if ext in folders_and_formats['images']:
                set_of_extensions.add(ext)
                images_list.append(way.name)
                os.replace(way, f'{anchor_path}/images/{normalized_name}')
            elif ext in folders_and_formats['video']:
                set_of_extensions.add(ext)
                video_list.append(way.name)
                os.replace(way, f'{anchor_path}/video/{normalized_name}')
            elif ext in folders_and_formats['documents']:
                set_of_extensions.add(ext)
                documents_list.append(way.name)
                os.replace(way, f'{anchor_path}/documents/{normalized_name}')
            elif ext in folders_and_formats['audio']:
                set_of_extensions.add(ext)
                audio_list.append(way.name)
                os.replace(way, f'{anchor_path}/audio/{normalized_name}')
            elif ext in folders_and_formats['archives']:
                set_of_extensions.add(ext)
                archives_list.append(way.name)
                new_path = f'{anchor_path}/archives/{normalized_name}'
                os.replace(way, new_path)
                name_for_moving = Path(new_path).name
                shutil.unpack_archive(new_path, f'{Path(new_path).parent}/{Path(name_for_moving).stem}/')
            else:
                unknown_set_of_extensions.add(ext)
                unknown_files_list.append(way.name)


def main():
    if len(sys.argv) > 1:

        p = Path(sys.argv[1])
    else:
        p = Path(input('Enter the path to the folder which you want to clean: '))

    anchor_path = p
    create_folders(p)
    sort_files(p, anchor_path)
    delete_empty_folders(p)

    # p = Path('/home/vk/Рабочий стол/dump')


if __name__ == '__main__':
    main()
