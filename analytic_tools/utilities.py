"""Module containing functions used to achieve the desired restructuring of the pollution_data directory
"""
from __future__ import annotations

# Include the necessary packages here
from pathlib import Path
from typing import Dict, List
import os
import shutil


def get_diagnostics(dir: str | Path) -> dict[str, int]:
    """Get diagnostics for the directory tree, with root directory pointed to by dir.
       Counts up all the files, subdirectories, and specifically .csv, .txt, .npy, .md and other files in the whole directory tree.

    Parameters:
        dir (str or pathlib.Path) : Absolute path to the directory of interest

    Returns:
        res (Dict[str, int]) : a dictionary of the findings with following keys: files, subdirectories, .csv files, .txt files, .npy files, .md files, other files.

    """

    # Dictionary to return
    res = {
        "files": 0,
        "subdirectories": 0,
        ".csv files": 0,
        ".txt files": 0,
        ".npy files": 0,
        ".md files": 0,
        "other files": 0,
    }

    # Error handling
    if not isinstance(dir, (str, Path)):
        raise TypeError(f"Expected input to be of type 'str' or 'Path', but got {type(dir).__name__} instead.")

    if dir == "":
        raise NotADirectoryError("Empty string is not a valid directory.")

    dir = Path(dir)  # Convert string to Path if needed

    if not dir.exists():  # Check if path exists
        raise NotADirectoryError("The directory does not exist.")

    if not dir.is_dir():  # Check if it's a directory, not a file
        raise NotADirectoryError(f"{dir} is not a directory.")

    


    # Traverse the directory and find its contents
    #contents = [x for x in dir.iterdir() if x.is_dir()] #itererer gjennom alt fra current folder og alle subtrær og finner det som er subfolder
    #contents = [x for x in dir.iterdir()] 
    contents = [x for x in dir.rglob('*')] # Lager en liste for alle filer og folders i directoryet

    # Count folders and total num. of files
    for path in contents:
    #for path in dir.rglob('*'):
        if path.is_dir() and path != dir:
            #print(path)
            res["subdirectories"] +=1
        elif path.is_file():
            res["files"] += 1
            if path.suffix == ".csv":
                res[".csv files"] +=1
            elif path.suffix == ".txt":
                res[".txt files"] += 1
            elif path.suffix == ".npy":
                res[".npy files"] += 1
            elif path.suffix == ".md":
                res[".md files"] += 1
            else:
                res["other files"] += 1

    return res


def display_diagnostics(dir: str | Path, contents: dict[str, int]) -> None:
    """Display diagnostics for the directory tree, with root directory pointed to by dir.
        Objects to display: files, subdirectories, .csv files, .txt files, .npy files, .md files, other files.

    Parameters:
        dir (str or pathlib.Path) : Absolute path the directory of interest
        contents (Dict[str, int]) : a dictionary of the same type as return type of get_diagnostics, has the form:

            .. highlight:: python
            .. code-block:: python

                {
                    "files": 0,
                    "subdirectories": 0,
                    ".csv files": 0,
                    ".txt files": 0,
                    ".npy files": 0,
                    ".md files": 0,
                    "other files": 0,
                }

    Returns:
        None
    """

    # Error handling
    if not isinstance(dir, (str, Path)):
        raise TypeError(f"Expected input to be of type 'str' or 'Path', but got {type(dir).__name__} instead.")

    dir = Path(dir) # konverterer dir til en path objekt dersom det er en string

    if not dir.exists():
        raise NotADirectoryError(f"The directory {dir} does not exist.")

    if not dir.is_dir():
        raise NotADirectoryError(f"{dir} is not a directory.")
    
    # Error handling for 'contents'
    if not isinstance(contents, dict):
        raise TypeError(f"Expected 'contents' to be a dictionary, but got {type(contents).__name__} instead.")


    # Print the summary to the terminal
    print(f"Diagnostics for {dir}")
    
    for key, val in contents.items():
        print(f"Number of {key}: {val}")


def display_directory_tree(dir: str | Path, maxfiles: int = 3) -> None:
    """Display a directory tree, with root directory pointed to by dir.
       Limit the number of files to be displayed for convenience to maxfiles.
       This tree is built with inspiration from the code written by "Flimm" at https://stackoverflow.com/questions/6639394/what-is-the-python-way-to-walk-a-directory-tree

    Parameters:
        dir (str or pathlib.Path) : Absolute path to the directory of interest
        maxfiles (int) : Maximum number of files to be displayed at each level in the tree, default to three.

    Returns:
        None

    """
    # NOTE: This is a bonus task, if you implementing it, remove `raise NotImplementedError`
    #raise NotImplementedError("Remove me if you implement this bonus task")
    
    
    if not isinstance(dir, (str, Path)):
        raise TypeError(f"Expected input to be of type 'str' or 'Path', but got {type(dir).__name__} instead.")

    path = Path(dir)

    if not path.is_dir():
        raise NotADirectoryError
    
    # Error handling: Check if the input path is a valid directory
    if not path.exists():
        raise NotADirectoryError(f"{path} does not exist.")
    if not path.is_dir():
        raise NotADirectoryError(f"{path} is not a directory.")
    if not isinstance(maxfiles, int):
        raise TypeError
    if maxfiles < 1:
        raise ValueError
    

    
    # Print the root directory
    print(f"{path.name}/")

    indent = 0

    for dirpath, _, files in path.walk():
        # Calculate the indentation level based on the depth of the current directory
        depth = len(Path(dirpath).relative_to(path).parts)
        indent = "    " * depth
        
        # Print the directory
        print(f"{indent}- {Path(dirpath).name}/")
        
        # Limit the number of files displayed
        files_to_display = files[:maxfiles] if len(files) > maxfiles else files
        for file in files_to_display:
            print(f"{indent}    - {file}")
        
        # Indicate if there are more files than the limit
        if len(files) > maxfiles:
            print(f"{indent}    - ...")


def is_gas_csv(path: str | Path) -> bool:
    """Checks if a csv file pointed to by path is an original gas statistics file.
        An original file must be called '[gas_formula].csv' where [gas_formula] is
        in ['CO2', 'CH4', 'N2O', 'SF6', 'H2'].

    Parameters:
         - path (str of pathlib.Path) : Absolute path to .csv file that will be checked

    Returns
         - (bool) : Truth value of whether the file is an original gas file
    """
    # Remove if you implement this task
    # raise NotImplementedError("Remove me if you implement this mandatory task")

    # Do correct error handling first
    if not isinstance(path, (str, Path)):
        raise TypeError(f"Expected a path-like object (str or Path), but got {type(path).__name__}.")
    
    file = Path(path)

    # if not file.is_file():
    #     raise ValueError(f"Did not get a file")

    if file.suffix != ".csv":
        raise ValueError(f"Expected a '.csv' file, but got a file with extension '{file.suffix}'.")
    
    # Extract the filename from the .csv file and check if it is a valid greenhouse gas
    gas_name = file.stem

    # List of greenhouse gasses, correct filenames in front of a .csv ending
    gasses = ["CO2", "CH4", "N2O", "SF6", "H2"]

    return gas_name in gasses


def get_dest_dir_from_csv_file(dest_parent: str | Path, file_path: str | Path) -> Path:
    """Given a file pointed to by file_path, derive the correct gas_[gas_formula] directory name.
        Checks if a directory "gas_[gas_formula]", exists and if not, it creates one as a subdirectory under dest_parent.

        The file pointed to by file_path must be a valid file. A valid file must be called '[gas_formula].csv' where [gas_formula]
        is in ['CO2', 'CH4', 'N2O', 'SF6', 'H2'].

    Parameters:
        - dest_parent (str or pathlib.Path) : Absolute path to parent directory where gas_[gas_formula] should/will exist
        - file_path (str or pathlib.Path) : Absolute path to file that gas_[gas_formula] directory will be derived from

    Returns:
        - (pathlib.Path) : Absolute path to the derived directory

    """

    # Do correct error handling first

    if not isinstance(dest_parent, (str, Path)):
        raise TypeError
    if not isinstance(file_path, (str, Path)):
        raise TypeError
    
    dest_parent = Path(dest_parent)
    file_path = Path(file_path)

    # Check if the file has a valid gas name and .csv suffix before checking existence
    if file_path.stem not in ['CO2', 'CH4', 'N2O', 'SF6', 'H2']:
        raise ValueError(f"Invalid gas name: {file_path.stem}")
    if file_path.suffix != '.csv':
        raise ValueError(f"Invalid file extension: {file_path.suffix}. Expected '.csv'")

    # Check if the destination parent directory exists
    if not dest_parent.is_dir():
        raise NotADirectoryError(f"{dest_parent} is not a directory")

    # Now check if the file exists
    if not file_path.is_file():
        raise ValueError(f"File does not exist: {file_path}")



    # If the input file is valid:
    # Derive the name of the directory, pattern: gas_[gas_formula] directory
    gas_name = file_path.stem

    dest_name = f"gas_{gas_name}"
    # Derive its absolute path
    dest_path = dest_parent / dest_name

    # Check if the directory already exists, and create one of not
    if dest_path.exists():
        return dest_path.absolute()
    else:
        dest_path.mkdir(parents=True, exist_ok=True)
        return dest_path.absolute()


def merge_parent_and_basename(path: str | Path) -> str:
    """This function merges the basename and the parent-name of a path into one, uniting them with "_" character.
       It then returns the basename of the resulting path.

    Parameters:
        - path (str or pathlib.Path) : Absolute path to modify

    Returns:
        - new_base (str) : New basename of the path
    """
    # Remove if you implement this task
    # raise NotImplementedError("Remove me if you implement this mandatory task")

    if not isinstance(path, (str, Path)):
        raise TypeError(f"Input is not of correct type (str or Path). Input given was of type {type(path).__name__}")

    path = Path(path)

    # Check if the path has both a parent and a basename
    if path.parent == Path() or path.name == "":
        raise ValueError("The path must contain both a parent directory and a basename (filename or directory name).")

    # Merge the parent name and the basename, replacing the separator (os.sep) with "_"
    new_base = f"{path.parent.name}_{path.name}".replace(os.sep, "_")
    return new_base


def delete_directories(path_list: list[str | Path]) -> None:
    """Prompt the user for permission and delete the objects pointed to by the paths in path_list if
       permission is given. If the object is a directory, its whole directory tree is removed.

    Parameters:
        - path_list (List[str | Path]) : a list of absolute paths to all the objects to be removed.


    Returns:
    None
    """

    print("The following directories and files will be deleted:")
    for path in path_list:
        p = Path(path).resolve()
        if p.is_dir():
            print(f"Directory: {p}")
        elif p.is_file():
            print(f"File: {p}")
        else:
            print(f"Warning: {p} does not exist or is not a file/directory.")


    res = input("Are you sure you want to delete these files and directories (y / n): ")

    if res.lower().strip() == "y":
        for path in path_list:
            p = Path(path).resolve()

            # Delete directories with their contents
            if p.is_dir():
                try:
                    shutil.rmtree(p)
                    print(f"Deleted directory: {p}")
                except Exception as e:
                    print(f"Error deleting directory {p}: {e}")
            
            # Delete files
            elif p.is_file():
                try:
                    p.unlink()
                    print(f"Deleted file: {p}")
                except Exception as e:
                    print(f"Error deleting file {p}: {e}")
        
        print("Deletion completed.")
    else:
        print("Deletion canceled.")
        
