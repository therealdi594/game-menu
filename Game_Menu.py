#this code was made by therealdi594
import subprocess
import os
import sys

# --- THE GAMES ---
GAMES = {
    "1": {
        "name": "Geometry Dash",
        "exe": r"C:\Users\there_mskrv0t\Downloads\Geometry_Dash\Geometry_Dash\Geometry-Dash-AnkerGames\Geometry_Dash\GeometryDash.exe",
        "args": ["-game", "-novid"]
    },
    "2": {
        "name": "Mr President",
        "exe": r"C:\Users\there_mskrv0t\Downloads\Mr-President-AnkerGames\Mr.President!\Mr.Prez.exe",
        "args": ["-game", "-novid"]
    },
    "3": {
        "name": "DOOM 64",
        "exe": r"C:\Users\there_mskrv0t\Downloads\DOOM-64-AnkerGames\Doom 64\DOOM64_x64.exe",
        "args": ["-game", "-novid"]
    }
}

def find_runnable_directive():
    """Quickly finds the first writable/runnable folder using system commands."""
    print("Locating a valid directive folder... (Skipping Windows/Program Files)")
    
    # We check common user-writable areas first for speed
    search_paths = [os.environ['USERPROFILE'], "D:\\", "E:\\"]
    
    for path in search_paths:
        if not os.path.exists(path): continue
        
        # Check current folder and its first level of subfolders
        try:
            for entry in os.scandir(path):
                if entry.is_dir():
                    # If we can write a test file, it's a valid directive
                    test_file = os.path.join(entry.path, "temp.txt")
                    try:
                        with open(test_file, 'w') as f: f.write('1')
                        os.remove(test_file)
                        return entry.path # Found it!
                    except:
                        continue
        except PermissionError:
            continue
    return os.environ['USERPROFILE'] # Fallback to User folder

def main():
    directive = find_runnable_directive()
    print(f"\nDIRECTIVE ACTIVE: {directive}")
    print("-" * 30)
    print("1: Launch Geometry Dash")
    print("2: Launch Mr President")
    print("3: Launch DOOM 64")
    print("Q: Quit | S: Shutdown | L: Logout")
    print("-" * 30)

    choice = input("Select an option: ").upper()

    if choice in GAMES:
        game = GAMES[choice]
        print(f"Launching {game['name']}...")
        try:
            subprocess.Popen(
                [game['exe']] + game['args'],
                cwd=directive, # The EXE will now 'read' this folder
                shell=True
            )
        except Exception as e:
            print(f"Error: {e}")
            
    elif choice == 'S':
        os.system("shutdown /s /t 0")
    elif choice == 'L':
        os.system("shutdown /l")
    elif choice == 'Q':
        sys.exit()

if __name__ == "__main__":
    while True:
        main()
