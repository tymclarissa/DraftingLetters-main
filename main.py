PLACEHOLDER = "[name]"

with open("Contacts/names.txt", "r") as file:
    names = file.readlines()


with open("./Email/draft.txt", "r") as draft:
    draft_letter = draft.read()
    for name in names:
        name = name.strip()
        letter = draft_letter.replace(PLACEHOLDER, name)


with open("./Email/draft.txt", "r") as draft: 
    draft_letter = draft.read()
    for name in names:
        name = name.strip()
        letter = draft_letter.replace(PLACEHOLDER, name)
        with open(f"./Send/Letter_for_{name}.txt", "w") as new_file:
            new_file.write(letter)

                
                                                