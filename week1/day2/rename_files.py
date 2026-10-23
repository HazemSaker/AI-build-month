import os

def rename_files(path: str, prefix: str = "") -> None:
    files_paths = os.listdir(path)

    for count, file in enumerate(files_paths, start = 1):
        full_old_path = os.path.join(path, file)
        if os.path.isfile(full_old_path):
            name = os.path.splitext(file)
            name = f"{prefix}_{count:02d}_{name[0]}_{name[1]}"

            os.rename(os.path.join(path, file), os.path.join(path, name))


    
