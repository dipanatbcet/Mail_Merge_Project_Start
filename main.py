#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.readlines()
#Replace the [name] placeholder with the actual name.
with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()
    final_names = []
    for index in names:
        final_names.append(index.strip())


for each_name in final_names:
    with open("./Output/ReadyToSend/letter_for_" + each_name + ".txt", mode="w") as invitation:
        salutation = letter_contents[0].replace("[name]", each_name)
        invitation.write(salutation)
        for j in range(1, len(letter_contents)):
            letter_body = letter_contents[j]
            invitation.write(letter_body)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp