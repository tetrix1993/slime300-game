# Slime 300 Game Score Incremental Program
This is a simple script to send GET/POST requests quickly to increase the global score in https://game.slime300-anime.com/

## Prerequisites
1. Download and install the latest version of [Python](https://www.python.org/downloads/)
2. When installing Python, make sure to check 'Add Python 3.X to PATH':\
3. Open the Command Prompt (for Windows) or Terminal (for MacOS).
4. Using the Command Prompt (Terminal for MacOS), change to the directory to where the file `slime.py` and `requirements.txt` is located. (E.g. if `slime.py` is located at `D:/Program`, enter `cd D:/Program` to change directory)
5. Run the following command to install all the packages needed to run the program:
```
pip install -r requirements.txt
```

## Running the Program
1. Using the Command Prompt (Terminal for MacOS), change to the directory to where the file `slime.py` is located.
2. Run the following command: `python slime.py`
3. To close the program, simply close the Command Prompt (or Terminal).

## Configuration
1. You can configure the number of concurrent process in `slime.py`. Simply change the value after `PROCESSES =`.
2. You can set how many times each process sends the GET/POST request by changing the value after `MAX_ITERATIONS = `. Set `-1` to run forever.
