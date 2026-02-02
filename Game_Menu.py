#this code was made by therealdi594
import os
import subprocess
import time

# Get the current user's home folder (e.g., C:\Users\Student123)
user_home = os.environ.get('USERPROFILE')
downloads_path = os.path.join(user_home, "Downloads")

# --- THE GAMES ---
# We use relative folders from the Downloads folder
GAMES = {
    "1": {
        "name": "Geometry Dash",
        "rel_path": r"Geometry_Dash\Geometry_Dash\Geometry-Dash-AnkerGames\Geometry_Dash\GeometryDash.exe",
        "args": ["-game", "-novid"]
    },
    "2": {
        "name": "Portal",
        "rel_path": r"Portal\Portal\Portal\Portal.exe",
        "args": ["-game", "-novid"]
    },
    "3": {
        "name": "DOOM 64",
        "rel_path": r"DOOM-64-AnkerGames\Doom 64\DOOM64_x64.exe",
        "args": ["-game", "-novid"]
    }
}

def run_launcher():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== SCHOOL LAUNCHER | USER: {os.getlogin()} ===")
        
        valid_games = {}
        for key, game in GAMES.items():
            # Combine Downloads path with the game's specific folder
            full_exe_path = os.path.join(downloads_path, game['rel_path'])
            
            if os.path.exists(full_exe_path):
                print(f"{key}: {game['name']} [READY]")
                valid_games[key] = full_exe_path
            else:
                print(f"{key}: {game['name']} [NOT FOUND IN DOWNLOADS]")
        
        print("-" * 40)
        print("Q: Quit")
        
        choice = input("\nSelect Game: ").upper()
        
        if choice in valid_games:
            exe_path = valid_games[choice]
            game_folder = os.path.dirname(exe_path)
            
            print(f"Launching from: {game_folder}")
            try:
                # Use the specific game's folder as the 'cwd' so it finds its files
                subprocess.Popen([exe_path] + GAMES[choice]['args'], cwd=game_folder, shell=False)
                print("Success! Closing in 2 seconds...")
                time.sleep(2)
                break
            except Exception as e:
                print(f"Blocked by school security: {e}")
                time.sleep(3)
        elif choice == 'Q':
            break

if __name__ == "__main__":
    run_launcher()

