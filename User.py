class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.messages_received = []
        self.messages_sent = []

    def describe(self):
        print("Hello, my name is " + self.name + ", and my password is " + self.password)

    def change_password(self, new_password):
        self.password = new_password

    def send_message(self, user, message):
        self.messages_sent.append(message)
        user.messages_received.append(message)

    def display_messages(self):
        print(self.name + " - sent: " + str(self.messages_sent))
        print(self.name + " - received: " + str(self.messages_received))

    def get_name(self):
        return self.name