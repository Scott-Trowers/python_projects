with open('Input/Letters/starting_letter.txt') as template_file:
    template = template_file.read()

invitees = []
with open('Input/Names/invited_names.txt') as invite_list:
    for name in invite_list:
        clean_name = name.replace('\n', '')
        invitees.append(clean_name)

for person in invitees:
    addressed_letter = template.replace('[name]', person)

    person_no_space = person.replace(' ', '')
    letter_path = f"Output/ReadyToSend/{person_no_space}_invite.txt"

    with open(letter_path, "x", encoding="utf-8") as f:
        f.write(addressed_letter)
