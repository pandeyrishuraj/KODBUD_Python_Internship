import os

folder_path = r"C:\Users\Hp\Desktop\File_Renaming_Test"

files = os.listdir(folder_path)

print(files)

for index, file in enumerate(files, start=1):
    new_name = f"file_{index}.txt"

    print(index, file, "→", new_name)

    os.rename(
        os.path.join(folder_path, file),
        os.path.join(folder_path, new_name)
    )