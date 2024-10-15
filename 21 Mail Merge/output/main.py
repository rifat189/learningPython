PLACEHOLDER = "[name]"
with open("../input/namefile/namesforletter.txt") as file:
    names = file.readlines()
    # print(names)

with open("../input/letter/demo letter.txt") as demo:
    demo_letter = demo.read()
    for n in names:
        stripped_name = n.strip()
        new_letter = demo_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./readytosend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
