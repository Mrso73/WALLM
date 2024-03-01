#import inference as llm
import whatsapp_interface as wf
from time import sleep

session_count = 5
sleep(3)


# Main program loop
while True:

    # Get list of all the chats/people that have unanswerd messages
    people_list = wf.get_respond_list() 

    number_list = [number for number in people_list if number.startswith('+')] # Keep only the phone numbers

    print(people_list)
    print(number_list)
    print("----------")

    # Send message to everyone is the list
    for x in range(session_count):
        for person in number_list:
            wf.open_chat(person)

            message = wf.get_last_message()

            if message == "/clear/":
                print("clearing chat")
                llm.message = []

            elif message == "/stop/":
                print("Stopping program")
                quit()

            elif message != None:
                #response = llm.generate(message)
                #wf.write_message(response)
                wf.write_message("Message read")
