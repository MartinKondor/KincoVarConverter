<p align="center">
  <img src="docs/Képernyőkép 2024-03-08 150403.png" height=140>
</p>

# Kinco Var Parser

This Python script parses KincoVar definitions from a file and extracts the variables into a list of `KincoVar` objects.

## Overview

The script consists of the following components:

- `KincoVar` class: Represents a KincoVar with attributes `name`, `address`, `type`, and `comment`.
- `read_vars_file` function: Reads the contents of a file.
- `parse_line` function: Parses a line of variable definition and returns a `KincoVar` object.
- `parse_vars` function: Parses the contents of a variables file and returns a list of `KincoVar` objects.
- Main script: Handles command-line arguments, searches for the variables file, reads its contents, parses the variables, and prints the result.

## Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the script with the command `python script.py <path_to_project_folder>` where `<path_to_project_folder>` is the path to the folder containing the KincoVar (.kgv) file.

### Example:
```bash
$ python script.py /path/to/project/folder
```

Replace `<path_to_project_folder>` with the actual path where the project folder containing the KincoVar files is located. Also, make sure to include any additional information or sections relevant to your project.

## Requirements
* Python 3.x

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Authors

* **[Martin Kondor](https://github.com/MartinKondor)**

# License

See the [LICENSE](LICENSE) file for details.
