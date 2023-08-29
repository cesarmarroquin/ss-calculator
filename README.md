## Overview
This program is designed to be run on the command line. It prompts for two files, which contain shipment destination addresses and driver names (delimited by new lines). It assigns the best destinations to drivers, by assessing the sustainability score for each combination, using a top-secret algorithm. The program ensures that each driver only has one shipment, and outputs all the combinations and total sustainability score at the end of the program when it is done assigning destination addresses.

The program currently expects the input files to be text based, with each entry for each file delimited by a new line. Example files and data can be found in `tests/data`


## Setup & Installation
#### Python
- Navigate to the project root via the command line, and create/activate a python virtual environment
  - `python3 -m venv venv`
  - `source venv/bin/activate`

## Running the program
#### Python
- `python main.py`
