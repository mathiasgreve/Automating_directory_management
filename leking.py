from pathlib import Path
from typing import Union, Dict
import analytic_tools.utilities as ut




#def get_diagnostics(dir: str | Path) -> dict[str, int]:
def get_diagnostics(dir: Union[str, Path]) -> Dict[str, int]:

    """Get diagnostics for the directory tree, with root directory pointed to by dir.
       Counts up all the files, subdirectories, and specifically .csv, .txt, .npy, .md and other files in the whole directory tree.

    Parameters:
        dir (str or pathlib.Path) : Absolute path to the directory of interest

    Returns:
        res (Dict[str, int]) : a dictionary of the findings with following keys: files, subdirectories, .csv files, .txt files, .npy files, .md files, other files.

    """

    # Remove if you implement this task
    #raise NotImplementedError("Remove me if you implement this mandatory task")

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
    if not isinstance(dir, (str, Path)):
        raise TypeError(f"Expected input to be of type 'str' or 'Path', but got {type(input_path).__name__} instead.")

    dir = Path(dir)

    if not dir.exists(): # checks if path/dir exists
        raise NotADirectoryError
    if not dir.is_dir(): # checks if the path/dir exists AND indeed is a dir
        raise NotADirectoryError


    # Traverse the directory and find its contents
    #contents = [x for x in dir.iterdir() if x.is_dir()] #itererer gjennom alt fra current folder og alle subtrær og finner det som er subfolder
    #contents = [x for x in dir.iterdir()] 
    contents = [x for x in dir.rglob('*')] # Lager en liste for alle filer og folders i directoryet

    # Count folders and total num. of files
    for path in contents:
        if path.is_dir():
            print(path.name)
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

    print(f"All files {res['files']}")
    print(f"Subdirectories: {res['subdirectories']}")
    print(f"CSV files {res['.csv files']}")
    print(f"TXT files {res['.txt files']}")
    print(f"NPY files  {res['.npy files']}")
    print(f"MD files  {res['.md files']}")
    print(f"Other files {res['other files']}")

    return res

def main():
    # get_diagnostics(Path("."))
    #utilities.display_diagnostics(Path("."))
    # ut.display_directory_tree("/Users/mathiasgreve/Documents/problemlosning_hoynivasprak/assignemnts/assignment2/tests/")
    ut.display_directory_tree(Path("."))

if __name__ == "__main__":
    main()
