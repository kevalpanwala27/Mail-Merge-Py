PLACEHOLDER = "[name]"

with open("Day24/Mail Merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Day24/Mail Merge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Day24/Mail Merge/Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)

