#First, we create the Email class with the __init__ method and the 2 other methods
#The is_sent attribute is not passed to the function, it is set automatically to False
# The send() method does not accept parameters, since it always sets the is_sent attribute to True
#The get_info() method also does not accept parameters, it just returns a string representation of the object
class Email:
    def __init__(self,sender, receiver,content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent=False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#We read the input until we receive "Stop", we create an Email and add it to the emails list
emails = []
line = input()
while line != "Stop":
    tokens = line.split()
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender,receiver,content)
    emails.append(email)
    line = input()

#We read the indices of the sent emails, loop through them \
# and call the send() method for each of the emails at those indices
send_emails = list(map(lambda x: int(x), input().split(", ")))
for x in send_emails:
    emails[x].send()
#Finally, we print each of the emails
for email in emails:
    print(email.get_info())

