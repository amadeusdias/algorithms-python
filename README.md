# Python Algorithm Challenges
This project consists of a collection of five algorithmic challenges implemented in Python. The challenges are designed to help me practice and improve my algorithmic problem-solving skills.

## Challenges
The following challenges are included in this project:

1. **Anagram Challenge**: Anagram Checker
  * *Implementation*: The solution compares the sorted versions of the two words.
2. **Palindrome Challenge (Recursion)**: Palindrome Checker
  * *Implementation*:  The solution uses a recursive function to check if the word is a palindrome.
3. **Palindrome Challenge (Iteration)**: Palindrome Checker
  * *Implementation*: The solution uses a recursive function to check if the word is a palindrome.
4. **Duplicate Letter Challenge***: Find the Duplicate Letter
  * *Implementation*: The solution iterates through the characters in the word, using a dictionary to keep track of letter occurrences.
5. **Study Schedule Challenge**: Study Schedule
  * *Description*: Find the time interval with the highest number of students present in the school.
  * *Implementation*: The solution analyzes the start and end times of students' study schedules to determine the interval with the maximum attendance.

## Getting Started

To run the algorithm challenges, follow these steps:
1. Make sure you have Python installed and start the virtual environment:
```python  
   python3 -m venv .venv
```
2. Activate the virtual environment: 
```python
source .venv/bin/activate
```
3. Install the dependencies: 
```python 
python3 -m pip install -r dev-requirements.txt
```
4. Run the tests for the chellanges: 
```python 
python3 -m pytest
```
5. Or execute the functions by hand: 
```python 
python anagram_challenge.py 
# for exemple
```
## Contributing
If you would like to contribute to this project, you can:

* Fork the repository.
* Create a new branch for your feature or bug fix.
* Make your changes and commit them with descriptive commit messages.
* Push your changes to your fork.
* Submit a pull request explaining your changes.

Please make sure to follow the existing code style and add appropriate tests for your changes.

## Final observation: 
Please note that this small project, even this readme, is done as part of my study of Python, algorithms, and programming in general. So please be kind regarding any criticism or contribution you may have for the project. Thank you.
