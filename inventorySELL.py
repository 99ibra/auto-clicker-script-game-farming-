#this is for torn poster level up method on yoworld


import pyautogui
import keyboard
import time

# Define the coordinates
c1 = (107, 474)
c2 = (441, 629)
c3 = (387, 706)
c4 = (327,661)
c5 = (386,708)


# Maximum number of loops
max_loops = 210
stop_flag = False  # Global flag to stop the loop

word = "00"

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
        pyautogui.click(c1)
        # time.sleep(2)
        
        # Click on the second coordinate

        pyautogui.doubleClick(c2)
        time.sleep(1.2)
        pyautogui.typewrite('00')
        # time.sleep(1)
        
        #this is temporary 
        pyautogui.click(c3)
        time.sleep(0.2)
        
        pyautogui.click(c4)
        time.sleep(3)

        pyautogui.click(c5)
        # time.sleep(1)
        
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
