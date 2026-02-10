import os
import shutil


def renamefiles(directory_path):
    print(f"Will begin renaming files for easier readability in the directory {os.path.abspath(directory_path)}")
    
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            original_path = os.path.join(directory_path, filename)

            name, extension = os.path.splitext(filename)
            month = name[:-4] # 1-2 digits before the last four are month
            year = name[-4:] # last four digits are the year

            month = month.zfill(2)
            new_name = f"{month}-{year}{extension}"

            new_path = os.path.join(directory_path, new_name)
            try:
                shutil.move(original_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
            except OSError as e:
                print(f"Error renaming file {filename}: {e}")
                return 1

    print("\nFile renaming complete.")
    return 0
            

def main():
    directory_name = "C:/Users/sjeng/OneDrive - The University of Texas at Austin/Coding/Music_Display/playlist_files"
    print(f"Exit {renamefiles(directory_name)}")


if __name__ == "__main__":
    main()