import pyautogui

print("Hover over the desired position and press Enter to get the coordinates.")

try:
    while True:
        input("Press Enter to capture the coordinates...")
        x, y = pyautogui.position()
        print(f"Captured coordinates: X: {x}, Y: {y}")
except KeyboardInterrupt:
    print("\nProgram terminated.")

    
    
    
    
    
