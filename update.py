# UPDATE THE userChrome.css FILE
import os
import requests

ZEN_CSS_URL = "https://raw.githubusercontent.com/Orbiva/zen-css/main/userChrome.css"

APPDATA_PATH = os.path.expandvars(r"%APPDATA%\zen\Profiles")
if not os.path.exists(APPDATA_PATH):
    print("Firefox profile directory not found.")
    exit()

profile_folders = [f for f in os.listdir(APPDATA_PATH) if os.path.isdir(os.path.join(APPDATA_PATH, f))]
if not profile_folders:
    print("No Firefox profiles found.")
    exit()

PROFILE_PATH = os.path.join(APPDATA_PATH, profile_folders[0], "chrome")
USERCHROME_PATH = os.path.join(PROFILE_PATH, "userChrome.css")

os.makedirs(PROFILE_PATH, exist_ok=True)

try:
    print(f"Downloading latest Zen CSS from {ZEN_CSS_URL}...")
    response = requests.get(ZEN_CSS_URL, timeout=10)
    response.raise_for_status()

    with open(USERCHROME_PATH, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"✅ Zen CSS updated successfully! Restart Firefox to apply changes.")
    print(f"Saved to: {USERCHROME_PATH}")

except requests.RequestException as e:
    print(f"❌ Failed to download Zen CSS: {e}")
except IOError as e:
    print(f"❌ File write error: {e}")

except requests.RequestException as e:
    print(f"Failed to download Zen CSS: {e}")
