import sys

def process_files(topic, help_string, py_file):
    with open('./SUBTITLES.template.html') as inputf:
        with open('./SUBTITLES.html', 'w') as outputf:
            for line in inputf:
                new_line = line.replace("#TOPIC_STRING#", topic).replace("#CHAT_HELP_STRING#", help_string).replace("#FILE_NAME#", py_file)
                outputf.write(new_line)

if __name__ == "__main__":
    substitution_elements = [
        ("Hello World", "!help_hello_world", "hello_world.py"),
        ("Variables", "!help_variables", "variables.py"),
        ("Collections", "!help_collections", "collections.py"),
        ("Strings","!help_strings", "strings.py"),
        ("Datetime","!help_sates", "dates.py"),
        ("Boolean Logic", "!help_boolean_logic", "boolean_logic.py"),
        ("Conditionals", "!help_conditionals", "conditionals.py"),
        ("Loops", "!help_loops", "loops.py"),
        ("Functions", "!help_functions", "functions.py"),
        ("Modules", "!help_modules", "modules.py"),
        ("Testing/TDD", "!help_testing", "TESTING readme"),
        ("Class", "!help_class", "classes.py"),
        ("Dataclass", "!help_dataclass", "dataclass.py"),
    ]

    if len(sys.argv) == 1:
        print("Available Subtitles:")
        for i, vals in enumerate(substitution_elements):
            print(f"{i}) {vals[0]}")
    else:
        index = int(sys.argv[1])
        process_files(*substitution_elements[index])