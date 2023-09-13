# python script.py path/to/directory_or_file key value
# https://pypi.org/project/mkdocs-i18n/

import os
import re
import sys
import phrase_strings
from pprint import pprint
from pathlib import Path


def replace_key_in_file(file_path):
    """Open file_path and search for keys wrapped in double curly braces.
    If a key is found, replace it with a value from the
    dict returned by the load_locale function. If no value is found, replace the key with an empty string.
    Then output a new file with the modified content. The filename should be the same as the original file, but with the
    .locale as appended to the stem of the filepath.
    """
    p = Path(file_path)

    try:
        with open(file_path, 'r') as file_in:
            content = file_in.read()

        for x in range(2, len(sys.argv)):
            # Set the locale to the next passed parameter
            xlocale = sys.argv[x]
            data_locale = phrase_strings.load_locale(xlocale)

            # Find all keys wrapped in double curly braces
            # Example: {{ key }}
            keys = re.findall(r"\{\{.*?\}\}", content)

            # Loop through keys and replace them with values from the loaded locale
            for key in keys:
                # Remove curly braces from the key
                key_without_curly_braces = key[2:-2].strip()

                # Replace key with value from loaded locale
                if key_without_curly_braces in data_locale:
                    content_out = content.replace(key, data_locale[key_without_curly_braces]['message'])
                else:
                    content_out = content.replace(key, "")

            # Output a new file with the modified content
            new_file_name = f"{p.stem}.{xlocale}{p.suffix}"
            new_file_path = os.path.dirname(file_path) + '/' + new_file_name
            with open(new_file_path, 'w') as file_out:
                file_out.write(content_out)

            print(f"File '{new_file_path}' processed successfully.")

    except Exception as e:
        print(f"An error occurred while processing '{file_path}': {e}")


def process_directories(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_key_in_file(file_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python translate.py <directory_or_filename> <locale> {<locale>...}")
        sys.exit(1)

    target_path = sys.argv[1]

    if os.path.isfile(target_path):
        replace_key_in_file(target_path)
    elif os.path.isdir(target_path):
        process_directories(target_path)
    else:
        pprint("target path:" + target_path)
        print("Invalid input. Please provide a valid directory or filename.")
