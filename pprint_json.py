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


def pretty_print_json_to_file(data, output_filepath):
    with io.open(output_filepath, 'w', encoding='utf-8') as f_obj:
        json.dump(data, f_obj, sort_keys=True,
                  indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # получаем имя файла из аргумента указанного при вызове в консоли
    filepath = sys.argv[1]
    json_without_format = load_data(filepath)

    if sys.argv[2] == '-f':
        pretty_print_json_to_file(json_without_format, 'output.json')

    json_in_pretty_format = pretty_print_json(json_without_format)
    print(json_in_pretty_format)
