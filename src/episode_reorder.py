```
Use at your own risk
This was ported from my other project done in PHP and a Batchfile.
It may blow up your files, THIS IS UNTESTED!!! 
https://github.com/bct9321/EpisodeReorder
```
import os

def extract_season_from_parts(parts):
    for part in parts:
        if part.startswith('S') and part[1:].isdigit():
            return part[1:]
    return None

def extract_episode_from_parts(parts):
    for part in parts:
        if part.startswith('E') and part[1:].isdigit():
            return part[1:]
    return None

def parse_season_and_episode(filename):
    parts = filename.split()
    season = extract_season_from_parts(parts)
    episode_number = extract_episode_from_parts(parts)
    return season, episode_number

def format_episode_number(episode_number, ep_length):
    return str(int(episode_number)).zfill(ep_length)

def construct_new_filename(filename, season, episode_number, ep_length):
    episode_number = format_episode_number(episode_number, ep_length)
    start_index_s = filename.find('S') + 1
    start_index_e = filename.find('E') + 2
    return f"{filename[:start_index_s]}{season}E{episode_number}{filename[start_index_e:]}"

def get_valid_files(file_path):
    invalid_files = ['rename.bat', 'rename.php']
    return [filename for filename in os.listdir(file_path) if filename.lower() not in invalid_files]

def rename_file(file_path, old_name, new_name):
    try:
        os.rename(os.path.join(file_path, old_name), os.path.join(file_path, new_name))
        print("\033[1;37m\033[42mRENAMED\033[0m")
    except Exception as e:
        print(f"\033[1;37m\033[41mFAIL: {e}\033[0m")

def process_single_file(file_path, filename, season, ep_length, commit_rename):
    print(f"Parsing: {filename}")
    season, episode_number = parse_season_and_episode(filename)

    if not season or not episode_number:
        return

    new_name = construct_new_filename(filename, season, episode_number, ep_length)
    print(f" New Name: {new_name}")

    if commit_rename:
        rename_file(file_path, filename, new_name)

def validate_numeric_input(value):
    return value.isdigit()

def get_user_input(message):
    return input(message).strip()

def rename_files(file_path, season, execute_rename, ep_length):
    try:
        season = int(season)
        ep_length = int(ep_length)
        commit_rename = execute_rename.lower() == 'y'

        print(f"Renaming Season {season:02}")
        files = get_valid_files(file_path)

        for filename in files:
            process_single_file(file_path, filename, season, ep_length, commit_rename)

        print("\nDone\n")

    except ValueError:
        print("Invalid season or episode length. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_user_input_and_validate_numeric(message):
    return input(message).strip()

def main():
    while True:
        file_path = get_user_input("Enter Season File Path: ")
        season = get_user_input_and_validate_numeric("Enter Season Number: ")
        execute_rename = get_user_input("Type Y to apply, Q to quit, or M to restart: ").lower()
        ep_length = get_user_input_and_validate_numeric("Enter Length of Episode Numbering: ")

        if not file_path:
            continue

        if not validate_numeric_input(season):
            continue

        if execute_rename not in ['y', 'q', 'm']:
            continue

        if execute_rename == 'q':
            break

        if execute_rename == 'm':
            continue

        if not validate_numeric_input(ep_length):
            continue

        rename_files(file_path, season, execute_rename, ep_length)

if __name__ == "__main__":
    main()
