"""Module containing functions used to achieve the desired restructuring of the pollution_data directory
"""
from __future__ import annotations

# Include the necessary packages here
from pathlib import Path
from typing import Dict, List


def get_diagnostics(dir: str | Path) -> dict[str, int]:
    """Get diagnostics for the directory tree, with root directory pointed to by dir.
       Counts up all the files, subdirectories, and specifically .csv, .txt, .npy, .md and other files in the whole directory tree.

    Parameters:
        dir (str or pathlib.Path) : Absolute path to the directory of interest

    Returns:
        res (Dict[str, int]) : a dictionary of the findings with following keys: files, subdirectories, .csv files, .txt files, .npy files, .md files, other files.

    """

    # Remove if you implement this task
    raise NotImplementedError("Remove me if you implement this mandatory task")

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

    # Remember error handling
    ...

    # Traverse the directory and find its contents
    contents = ...

    # Count folders and total num. of files
    for path in contents:
        ...

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
    # Remove if you implement this task
    raise NotImplementedError("Remove me if you implement this mandatory task")

    # Print the summary to the terminal
    ...


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
    raise NotImplementedError("Remove me if you implement this bonus task")

    ...


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
    raise NotImplementedError("Remove me if you implement this mandatory task")

    # Do correct error handling first
    # Extract the filename from the .csv file and check if it is a valid greenhouse gas
    ...

    # List of greenhouse gasses, correct filenames in front of a .csv ending
    gasses = ["CO2", "CH4", "N2O", "SF6", "H2"]

    ...


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
    # Remove if you implement this task
    raise NotImplementedError("Remove me if you implement this mandatory task")

    # Do correct error handling first

    ...

    # If the input file is valid:
    # Derive the name of the directory, pattern: gas_[gas_formula] directory
    dest_name = ...
    # Derive its absolute path
    dest_path = ...

    # Check if the directory already exists, and create one of not
    if dest_path.exists():
        return dest_path
    ...


def merge_parent_and_basename(path: str | Path) -> str:
    """This function merges the basename and the parent-name of a path into one, uniting them with "_" character.
       It then returns the basename of the resulting path.

    Parameters:
        - path (str or pathlib.Path) : Absolute path to modify

    Returns:
        - new_base (str) : New basename of the path
    """
    # Remove if you implement this task
    raise NotImplementedError("Remove me if you implement this mandatory task")

    # New, merged, basename of the path, which will be the new filename
    new_base = ...
    return new_base


def delete_directories(path_list: list[str | Path]) -> None:
    """Prompt the user for permission and delete the objects pointed to by the paths in path_list if
       permission is given. If the object is a directory, its whole directory tree is removed.

    Parameters:
        - path_list (List[str | Path]) : a list of absolute paths to all the objects to be removed.


    Returns:
    None
    """
    # NOTE: This is an optional task, no points assigned. If you are skipping it, remove `raise NotImplementedError` in the function body
    raise NotImplementedError("Remove me if you implement this optional task")

    ...
