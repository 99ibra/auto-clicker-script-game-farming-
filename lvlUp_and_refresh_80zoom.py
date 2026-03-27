#this is for torn poster level up method on yoworld
# Updated version to refresh the webpage and go through the whole process by it self


import pyautogui
import keyboard
import time

# Define the coordinates
refresh = (98, 62)
confirmRefresh = (458,227)
map = (117, 742)
store = (413, 457)
go_store = (614 , 735)
enter = (449 , 465)
counter = (370 , 380)
search = (443 , 405)
findItem = (322 , 483)
buyItem = (391 , 655)
confirmItem = (392 , 592)

# Maximum number of loops
max_loops = 500
refresh_cycle = 8
stop_flag = False  # Global flag to stop the loop

word = "torn poster"

def click_coordinates():
    global stop_flag
    
    # Delay before starting the clicks
    print("Waiting 10 seconds before starting...")
    time.sleep(10)  # 10-second delay

    for j in range(refresh_cycle):
        if stop_flag:  # Check if stop_flag is set to True
                print("ESC pressed, exiting program.")
                break
        
        pyautogui.click(refresh)
        time.sleep(3)

        pyautogui.click(confirmRefresh)
        time.sleep(35)

        pyautogui.click(map)
        time.sleep(2)

        pyautogui.click(store)
        time.sleep(2)

        pyautogui.click(go_store)
        time.sleep(10)

        pyautogui.click(enter)
        time.sleep(10)

        pyautogui.click(counter)
        time.sleep(10)

        pyautogui.click(search)
        pyautogui.typewrite(word)
        time.sleep(4)

        for i in range(max_loops):
            if stop_flag:  # Check if stop_flag is set to True
                print("ESC pressed, exiting program.")
                break
            
            # Click on the first coordinate
            pyautogui.click(findItem)
            time.sleep(1)
            
            # Click on the second coordinate
            pyautogui.click(buyItem)
            time.sleep(1)
            
            # Click on the third coordinate
            pyautogui.click(confirmItem)
            time.sleep(1)
            
            print(f"Cycle-{j+1}:::Loop-{i+1} completed")

        print(f"*************Refresh {j+1} completed**************")


def stop_program():
    global stop_flag
    print("Hotkey pressed, stopping the loop.")
    stop_flag = True  # Set the flag to True to stop the loop

if __name__ == "__main__":
    # Set up a hotkey to stop the program
    keyboard.add_hotkey('esc', stop_program)
    
    print("Press ESC to stop the program.")
    click_coordinates()