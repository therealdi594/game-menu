#this code was made by therealdi594
import os
import subprocess
import time

# --- THE GAMES ---
# Updated to use the folder containing the exe as the working directory
GAMES = {
    "1": {
        "name": "Geometry Dash",
        "exe": r"C:\Users\your_name\Downloads\Geometry_Dash\Geometry_Dash\Geometry-Dash-AnkerGames\Geometry_Dash\GeometryDash.exe",
        "args": ["-game", "-novid"]
    },
    "2": {
        "name": "Portal",
        "exe": r"C:\Users\your_name\Downloads\Portal\Portal\Portal\Portal.exe",
        "args": ["-game", "-novid"]
    },
    "3": {
        "name": "DOOM 64",
        "exe": r"C:\Users\your_name\Downloads\DOOM-64-AnkerGames\Doom 64\DOOM64_x64.exe",
        "args": ["-game", "-novid"]
    }
}

def run_launcher():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- GAME LAUNCHER ---")
        for key, game in GAMES.items():
            print(f"{key}: {game['name']}")
        print("Q: Quit | S: Shutdown | L: Logout")
        print("-" * 40)
        
        choice = input("Select Game (1-3) or System Action: ").upper()
        
        if choice in GAMES:
            g = GAMES[choice]
            exe_path = g['exe']
            
            # Key Change: Get the specific directory for THIS game's executable
            game_dir = os.path.dirname(exe_path)
            
            print(f"Starting {g['name']} in {game_dir}...")
            
            try:
                # Use 'cwd' to tell the game to look in its own folder for files
                # Changed shell to False for better stability with direct exe paths
                subprocess.Popen([exe_path] + g['args'], cwd=game_dir, shell=False)
                time.sleep(2) 
            except Exception as e:
                print(f"Error launching game: {e}")
                time.sleep(3)
                
        elif choice == 'S':
            os.system("shutdown /s /t 0")
        elif choice == 'L':
            os.system("shutdown /l")
        elif choice == 'Q':
            break

if __name__ == "__main__":
    run_launcher()
