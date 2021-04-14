from User import User


def create_users():
    user1 = User("Daniel", "password1")
    user2 = User("Won", "password2")
    return user1, user2

def run_app(user1, user2):
    chat_active = True
    sender = user1
    receiver = user2
    while chat_active:
        message = input(f"Hi {sender.get_name()}, please enter your message to {receiver.get_name()}: ")
        if message == "exit":
            chat_active = False
            print("Good bye!")
            user1.display_messages()
            user2.display_messages()
            break
        elif message == "switch":
            tmp = sender
            sender = receiver
            receiver = tmp
        else:
            sender.send_message(receiver, message)

if __name__ == '__main__':
    user1, user2 = create_users()
    run_app(user1, user2)