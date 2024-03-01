import pyautogui as pygui
import pyperclip as pyclip

def open_chat(person):

    # Open search bar
    pygui.hotkey('ctrl', 'f')    
    pygui.hotkey('ctrl', 'a')
    pygui.press('delete') 

    # Search person
    pygui.typewrite(person, interval=0.1)
    pygui.press('enter')

def open_first_chat():
    pygui.hotkey('ctrl', '1')

def next_chat():
    pygui.hotkey('ctrl', 'tab')

def close_chat():
    pygui.hotkey('ctrl', 'w')

# -----------------------  

def write_message(message):
    pygui.typewrite(message, interval=0.01)
    pygui.press('enter')

def check_last_message():

    # Check if a message has been send to you
    try:
        start_messagebox_position = pygui.locateOnScreen("assets\L_messagebox.png", confidence=.9)
    except(ImageNotFoundException):
        print("Could not find the messagebox")
        quit()

    x, y = start_messagebox_position[0] + 235, start_messagebox_position[1] - 50

    #print(f"{x}; {y}")

    # If no message than stop function
    if pygui.pixelMatchesColor(int(x) - 10, int(y), (255, 255, 255)) == False:
        return False
    else:
        return True

# -----------------------

def get_number_current_chat():
    try:
        start_profile_position = pygui.locateOnScreen("assets\L_new_chat_button.png", confidence=.6)
    except(ImageNotFoundException):
        print("Could not find the messagebox")
        quit()

    x, y = start_profile_position[0] + 290, start_profile_position[1] + 25
    pygui.moveTo(x, y, duration=0.1)
    pygui.click()
    pygui.moveTo(x, y + 125, duration=0.1)
    pygui.tripleClick()
    pygui.hotkey('ctrl', 'c')
    pygui.press('escape') 
    return pyclip.paste()

def get_last_message():

    # Check if a message has been send to you
    try:
        start_messagebox_position = pygui.locateOnScreen("assets\L_messagebox.png", confidence=.9)
    except(ImageNotFoundException):
        print("Could not find the messagebox")
        quit()

    x, y = start_messagebox_position[0] + 235, start_messagebox_position[1] - 50

    #print(f"{x}; {y}")

    # If no message than stop function
    if pygui.pixelMatchesColor(int(x) - 10, int(y), (255, 255, 255)) == False:
        return None

    pygui.moveTo(x, y, duration=0.35)
    pygui.tripleClick()
    pygui.hotkey('ctrl', 'c')

    # TO CHANGE
    pygui.moveTo(x, y - 50, duration=0.35)
    pygui.click()

    return pyclip.paste()

def get_respond_list():
    
    repondent_list = []
    current_number = None

    pygui.hotkey('ctrl', 'f')    
    pygui.hotkey('ctrl', 'a')
    pygui.press('delete') 

    # Open the first chat
    open_first_chat()

    # Add all number to which to respond to the phone_list variable
    while True:
        last_number_checked = current_number
        
        # Check the number of the current chat
        current_number = get_number_current_chat()

        # If the end of the list has been reached, go back to the start
        if last_number_checked == current_number:
            open_first_chat()
            break

        if check_last_message():
            repondent_list.append(current_number)
        
        next_chat()
    
    return repondent_list
