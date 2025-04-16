command = input()
notes = []  # Initialize an empty list to store notes

while command != "End":
    tokens = command.split("-")  # Split the input into importance and value
    importance = int(tokens[0])  # Convert importance to integer
    value = tokens[1]  # The value is the second part

    # Find the correct position to insert the note based on importance
    inserted = False  # to track whether the note has been inserted into the correct position in the list
    for i in range(len(notes)):  #The for loop iterates over all the existing notes in the notes list to find the correct position for the new note
        note_importance = int(notes[i].split("-")[0])  # Get the importance of the current note
        if note_importance > importance:
            notes.insert(i, command)  # Insert the new note before the current note
            inserted = True
            break

    # If the note has not been inserted, it means it has the lowest importance
    if not inserted:  #If the inserted flag is still False, it means the new note has the lowest importance (i.e., it’s smaller than all other notes in the list), so it gets appended to the end of the notes list
        notes.append(command)  # Append the note at the end of the list

    command = input()  # Read the next command

# Create a list of the values only, and print the result as a list
result = [note.split("-")[1] for note in notes]
print(result)
