#this is for torn poster level up method on yoworld


import pyautogui
import keyboard
import time

# Define the coordinates
coord1 = (286, 485)
coord2 = (377, 699)
coord3 = (380, 614)
c4 = (399,663)

# Maximum number of loops
max_loops = 5000
stop_flag = False  # Global flag to stop the loop

def click_coordinates():
    global stop_flag
    
    # Delay before starting the clicks
    print("Waiting 5 seconds before starting...")
    time.sleep(5)  # 5-second delay

    for i in range(max_loops):
        if stop_flag:  # Check if stop_flag is set to True
            print("ESC pressed, exiting program.")
            break
        
        # Click on the first coordinate
        pyautogui.click(coord1)
        # time.sleep(0.2)
        
        # Click on the second coordinate
        pyautogui.click(coord2)
        time.sleep(0.35)
        
        # #this is temporary 
        # pyautogui.click(c4)
        # # time.sleep(1)
        
        # Click on the third coordinate
        pyautogui.click(coord3)
        # time.sleep(0.2)
        
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
