# Sports Frequency Counter (Python)

This project reads two text files—`sports.txt` and `played.txt`—and uses Python to count how many times each sport was played. It demonstrates file handling, dictionaries, and basic data parsing in Python.

## Project Description

The program (`NeilNayyarHW5.py`) loads:
- `sports.txt` — a list of valid sports (first line is the number of sports)
- `played.txt` — a list of sports that were actually played

The script then:
1. Reads the allowed sports
2. Reads the played sports
3. Counts occurrences using a dictionary
4. Prints the final results

This assignment practices:
- File I/O  
- Dictionaries  
- Loops and conditionals  
- Basic text processing  

## Folder Structure

python-sports-dictionary/  
│  
├── NeilNayyarHW5.py  
├── sports.txt  
├── played.txt  
└── README.md  

## File Descriptions

### NeilNayyarHW5.py
Main Python script. Reads both text files, validates sports, creates a dictionary of counts, and prints results.

### sports.txt
Contains the number of sports followed by one sport per line:

4  
Soccer  
Baseball  
Football  
Tennis  

### played.txt
Contains a list of sports that were played:

Tennis  
Baseball  
Baseball  
Football  
Tennis  
Tennis  

## How to Run

Make sure all three files are in the same folder.

Command:

python NeilNayyarHW5.py

The program will output how many times each sport was played.

## Example Output

Tennis: 3  
Baseball: 2  
Football: 1  
Soccer: 0  

## Skills Demonstrated
- Python file reading (`open`, `readlines`)
- Dictionary creation and counting
- Validation of entries
- Clean, organized program structure
