class Party:
    def __init__(self):
        self.people = []

party = Party()  # Create a new instance of the class
line = input()  #Read input and add it to the party people until you receive "End"
while line != "End":
    party.people.append(line)
    line = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")


