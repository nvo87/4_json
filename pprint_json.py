import json
import io
import shutil
import sys


def load_data(filepath):
    # из-за проблем с кодировкой в utf-8 используем ф-ию io.open
    with io.open(filepath, encoding='utf-8') as f_obj:
        return json.load(f_obj)


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)


def save_pretty_json_to_file(json_str, filename):
    with io.open(filename, 'w', encoding='utf-8') as f_obj:
        json.dump(json_str, f_obj, sort_keys=True,
                  indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # получаем имя файла из аргумента указанного при вызове в консоли
    filepath = sys.argv[1]
    json_str = load_data(filepath)
    pretty_json_str = pretty_print_json(json_str)

    if sys.argv[2] == '-f':
        save_pretty_json_to_file(json_str, 'output.json')

    print(pretty_json_str)
