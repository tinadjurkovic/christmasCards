def card_creator(employee, template):
    content = template.replace("NAME", employee)
    return content

def cards_creator(file_path, template_path, output_dir):
    with open(file_path, 'r') as namesFile:
        names = namesFile.read().splitlines()

    with open(template_path, 'r') as templateFile:
        template = templateFile.read()

    for name in names:
        card_content = card_creator(name, template)
        card_filename = f"{output_dir}/{name}.txt"
        with open(card_filename, 'w') as cardFile:
            cardFile.write(card_content)

if __name__ == '__main__':
    employees_file_path = 'employees.txt'
    template_file_path = 'template.txt'
    output_directory = 'christmasCards'

    cards_creator(employees_file_path, template_file_path, output_directory)
