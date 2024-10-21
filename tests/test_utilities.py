""" Test script executing all the necessary unit tests for the functions in analytic_tools/utilities.py module
    which is a part of the analytic_tools package
"""

# Include the necessary packages here
from pathlib import Path

import pytest

# mine pakker
from typing import Dict

# This should work if analytic_tools has been installed properly in your environment
from analytic_tools.utilities import (
    get_dest_dir_from_csv_file,
    get_diagnostics,
    is_gas_csv,
    merge_parent_and_basename,
)


@pytest.mark.task12
def test_get_diagnostics(example_config):
    """Test functionality of get_diagnostics in utilities module

    Parameters:
        example_config (pytest fixture): a preconfigured temporary directory containing the example configuration
                                     from Figure 1 in assignment2.md

    Returns:
    None
    """
    # Remove if you implement this task
    #raise NotImplementedError("Remove me if you implement this mandatory task")
    
    # Run get_diagnostics on the example_config directory
    res = get_diagnostics(example_config)

    assert isinstance(res, dict), f"Return type was {type(res)}, but expected a dict"

    # Assertions based on the manually counted data from Figure 1
    assert res['.csv files'] == 8, f"Expected 8 .csv files, but got {res['.csv files']}"
    assert res['.npy files'] == 2, f"Expected 2 .npy files, but got {res['.npy files']}"
    assert res['files'] == 10, f"Expected 10 total files, but got {res['files']}"
    assert res['subdirectories'] == 5, f"Expected 4 subdirectories, but got {res['subdirectories']}"
    assert res['other files'] == 0, f"Expected 0 other files, but got {res['other files']}"


@pytest.mark.task12
@pytest.mark.parametrize(
    "exception, dir",
    [
        (NotADirectoryError, "Not_a_real_directory"),
        # add more combinations of (exception, dir) here.
        (TypeError, 123),
        (TypeError, False),
        (TypeError, None),
        (NotADirectoryError, Path(__file__)),
        (NotADirectoryError, "")
    ],
)
def test_get_diagnostics_exceptions(exception, dir):
    """Test the error handling of get_diagnostics function

    Parameters:
        exception (concrete exception): The exception to raise
        dir (str or pathlib.Path): The parameter to pass as 'dir' to the function

    Returns:
        None
    """
    # Remove if you implement this task
    #raise NotImplementedError("Remove me if you implement this mandatory task")
    
    with pytest.raises(exception):
        get_diagnostics(dir)



@pytest.mark.task22
def test_is_gas_csv():
    """Test functionality of is_gas_csv from utilities module

    Parameters:
        None

    Returns:
        None
    """
    # Remove if you implement this task
    # raise NotImplementedError("Remove me if you implement this mandatory task")
    
    assert is_gas_csv("CO2.csv")
    assert is_gas_csv("test/SF6.csv")

    assert not is_gas_csv("sdf.csv")
    assert not is_gas_csv("co2.csv")

    # with pytest.raises(ValueError):
    #     is_gas_csv("SF6")
    #     is_gas_csv("test/SF6.txt")

    with pytest.raises(TypeError):
        is_gas_csv(5)
        is_gas_csv(True)

@pytest.mark.task22
@pytest.mark.parametrize(
    "exception, path",
    [
        (ValueError, Path(__file__).parent.absolute()),
        # add more combinations of (exception, path) here
        (ValueError, "SF6"),
        (ValueError, "test/SF6.txt"),
        (TypeError, 5),
        (TypeError, True)
    ],
)
def test_is_gas_csv_exceptions(exception, path):
    """Test the error handling of is_gas_csv function

    Parameters:
        exception (concrete exception): The exception to raise
        path (str or pathlib.Path): The parameter to pass as 'path' to function

    Returns:
        None
    """
    # Remove if you implement this task
    # raise NotImplementedError("Remove me if you implement this mandatory task")
    
    with pytest.raises(exception):
        is_gas_csv(path)


@pytest.mark.task24
def test_get_dest_dir_from_csv_file(example_config):
    """Test functionality of get_dest_dir_from_csv_file in utilities module.

    Parameters:
        example_config (pytest fixture): a preconfigured temporary directory containing the example configuration
            from Figure 1 in assignment2.md

    Returns:
        None
    """
    dest_parent = Path(example_config) / 'pollution_data_restructured' / 'by_gas'

    # Ensure dest_parent directory exists
    if not dest_parent.exists():
        dest_parent.mkdir(parents=True)

    for dirpath, dirs, files in Path(example_config).walk():
        for file in files:
            file_path = Path(dirpath) / file
            if file_path.suffix == ".csv":

                if is_gas_csv(file_path):
                    # Call get_dest_dir_from_csv_file to get the destination directory
                    dest_dir = get_dest_dir_from_csv_file(dest_parent, file_path)
                    
                    # Expected directory name based on the gas name
                    expected_gas = file_path.stem  # 'CO2', 'CH4', etc.
                    expected_dest_dir = dest_parent / f'gas_{expected_gas}'
                    
                    # Assert that the destination directory matches the expected path
                    assert dest_dir == expected_dest_dir, f"Expected {expected_dest_dir}, but got {dest_dir}"
                    
                    # Assert that the destination directory exists
                    assert dest_dir.exists(), f"Directory {dest_dir} was not created"
                    assert dest_dir.is_dir(), f"{dest_dir} is not a directory"

@pytest.mark.task24
@pytest.mark.parametrize(
    "exception, dest_parent, file_path",
    [
        # (1) File is not a CSV file - expect ValueError
        (ValueError, Path(__file__).parent.absolute(), "foo.txt"),
        
        # (2) file_path is not path-like - expect TypeError
        (TypeError, Path(__file__).parent.absolute(), 12345), 
        
        # (3) file_path is not a valid gas CSV - expect ValueError
        (ValueError, Path(__file__).parent.absolute(), "invalid_file.csv"),  
        
        # (4) dest_parent is not a path-like object - expect TypeError
        (TypeError, 12345, "CO2.csv"),  
        
        # (5) dest_parent is not a directory - expect NotADirectoryError
        (NotADirectoryError, Path(__file__).parent.absolute() / "not_a_dir", "CO2.csv"), 
        
        # (6) Valid gas CSV file but non-existing dest_parent directory - expect NotADirectoryError
        (NotADirectoryError, Path("/non/existing/directory"), "CO2.csv"),
    ],
)
def test_get_dest_dir_from_csv_file_exceptions(exception, dest_parent, file_path):
    """Test the error handling of get_dest_dir_from_csv_file function

    Parameters:
        exception (concrete exception): The exception to raise
        dest_parent (str or pathlib.Path): The parameter to pass as 'dest_parent' to the function
        file_path (str or pathlib.Path): The parameter to pass as 'file_path' to the function

    Returns:
        None
    """
    with pytest.raises(exception):
        get_dest_dir_from_csv_file(dest_parent, file_path)


@pytest.mark.task26
def test_merge_parent_and_basename():
    """Test functionality of merge_parent_and_basename from utilities module

    Parameters:
        None

    Returns:
        None
    """
    # Remove if you implement this task
    # raise NotImplementedError("Remove me if you implement this mandatory task")
    
    assert "src_agriculture_CO2.csv" == merge_parent_and_basename("/User/.../assignment2/pollution_data/by_src/src_agriculture/CO2.csv")
    assert "src_agriculture_CO2.csv" == merge_parent_and_basename(Path("/User/.../assignment2/pollution_data/by_src/src_agriculture/CO2.csv"))
    assert 'some_dir_some_sub_dir' == merge_parent_and_basename('some_dir/some_sub_dir')
    assert 'some_dir_some_file.txt' == merge_parent_and_basename('some_dir/some_file.txt')

@pytest.mark.task26
@pytest.mark.parametrize(
    "exception, path",
    [
        (TypeError, 33),
        # add more combinations of (exception, path) here
        (ValueError, "/")
    ],
)
def test_merge_parent_and_basename_exceptions(exception, path):
    """Test the error handling of merge_parent_and_basename function

    Parameters:
        exception (concrete exception): The exception to raise
        path (str or pathlib.Path): The parameter to pass as 'pass' to the function

    Returns:
        None
    """
    # Remove if you implement this task
    with pytest.raises(exception):
        merge_parent_and_basename(path)
