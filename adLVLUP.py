#This is for getting coins by watching ads, it can be modified to function for multiple accounts at the same time.........


import pyautogui
import keyboard
import time

# Define the coordinates
coord1 = (582, 607)
coord2 = (379, 662)
coord3 = (1372, 609)
coord4 = (1180, 665)

# Maximum number of loops
max_loops = 50
stop_flag = False  # Global flag to stop the loop

def click_coordinates():
    global stop_flag
    
    # Delay before starting the clicks
    print("Waiting 10 seconds before starting...")
    time.sleep(10)  # 10-second delay

    for i in range(max_loops):
        if stop_flag:  # Check if stop_flag is set to True
            print("ESC pressed, exiting program.")
            break
        
        # Click on the first coordinate
        pyautogui.click(coord1)
        time.sleep(3)
        
        # Click on the second coordinate
        pyautogui.click(coord2)
        time.sleep(3)
        
        # Click on the 3rd coordinate
        pyautogui.click(coord3)
        time.sleep(3)
        
        # Click on the 4th coordinate
        pyautogui.click(coord4)
        time.sleep(11)
        
        print(f"Loop {i+1} completed")

def stop_program():
    global stop_flag
    print("Hotkey pressed, stopping the loop.")
    stop_flag = True  # Set the flag to True to stop the loop

if __name__ == "__main__":
    # Set up a hotkey to stop the program
    keyboard.add_hotkey('esc', stop_program)
    
    print("Press ESC to stop the program.")
    click_coordinates()
