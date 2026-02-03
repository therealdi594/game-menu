#this code was made by therealdi594
import os
import subprocess
import time
import sys
from pathlib import Path

# --- CONFIGURATION ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# List of common places to look for game folders
SEARCH_DIRS = [
    Path(os.environ.get('USERPROFILE', '')),  # User Home
    Path(os.environ.get('USERPROFILE', '')) / "Downloads",
    Path(os.environ.get('USERPROFILE', '')) / "Desktop",
    Path(os.environ.get('USERPROFILE', '')) / "Documents",
    Path.cwd() # The folder this script is running in
]

# Game Definitions
# 'exe_path' should be the relative path from the folder found in SEARCH_DIRS
GAME_DB = [
    {
        "id": "1",
        "name": "Geometry Dash",
        "rel_path": r"Geometry_Dash\Geometry_Dash\Geometry-Dash-AnkerGames\Geometry_Dash\GeometryDash.exe",
        "args": ["-game", "-novid"]
    },
    {
        "id": "2",
        "name": "Portal",
        "rel_path": r"Portal\Portal\Portal\Portal.exe",
        "args": ["-game", "-novid"]
    },
    {
        "id": "3",
        "name": "DOOM 64",
        "rel_path": r"DOOM-64-AnkerGames\Doom 64\DOOM64_x64.exe",
        "args": ["-game", "-novid"]
    }
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_game_path(relative_path):
    """
    Scans SEARCH_DIRS to find where the game folder is hiding.
    Returns the full Path object if found, else None.
    """
    for directory in SEARCH_DIRS:
        if directory.exists():
            full_path = directory / relative_path
            if full_path.exists():
                return full_path
    return None

def print_header():
    clear_
