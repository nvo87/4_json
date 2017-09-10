import json
import io
import shutil
import sys


def load_data_with_utf8(filepath):
    with io.open(filepath, encoding='utf-8') as f_obj:
        return json.load(f_obj)


def get_json_in_pretty_format(json_raw_string):
    return json.dumps(json_raw_string, sort_keys=True, indent=4, ensure_ascii=False)


def pretty_print_json_to_file(json_raw_string, output_filepath):
    with io.open(output_filepath, 'w', encoding='utf-8') as f_obj:
        json.dump(json_raw_string, f_obj, sort_keys=True,
                  indent=4, ensure_ascii=False)


def get_arguments_from_command_line(arg_number):
    if len(sys.argv) > arg_number:
        return sys.argv[arg_number]

if __name__ == '__main__':
    filepath = get_arguments_from_command_line(1)
    if filepath is None:
        print("You have to type json source filepath")
        sys.exit()

    try:
        json_without_format = load_data_with_utf8(filepath)
    except FileNotFoundError:
        print("This filepath doesn't exist!")
        sys.exit()

    json_in_pretty_format = get_json_in_pretty_format(json_without_format)
    print(json_in_pretty_format)

    write_to_file_flag = get_arguments_from_command_line(2)
    if write_to_file_flag == '-f':
        pretty_print_json_to_file(json_without_format, 'output.json')
    else:
        print("Unknown flag. If you want to output result to file, use -f key.")
