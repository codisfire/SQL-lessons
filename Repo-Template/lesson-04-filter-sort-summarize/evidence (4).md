# Lesson 04 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: 9ce0d312d6f0682ff1309a9af3c93fa37ba00515 <br>
created new file for lesson 4
- Commit 2 hash + message: 22336bef29c2294876ab1e661b04b637c7fe816c <br>
i've finished the coding and practical question in lesson 4, will move onto the theory questions next
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python Repo-Template/lesson-04-filter-sort-summarize/lesson4_filter.py
- Terminal output pasted below:
('Leo', 11)
Total students: 3

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
First, I changed the value of 10 to 12. Then, I went back to a previous file and changed the year group of one of my students, so i had one from years 10, 11, and 12. I then ran the code again, this time changing the value to 11. Then, I swapped `name` and `year_group` in the `"SELECT name, year_group FROM students WHERE year_group = ? ORDER BY name"` statement to get the program to print out the year group first. 

## Prediction before run
- Query version: 12
- My prediction (filtered rows, order, or count): I predicted it would give one result
- What actually happened: It gave one result
## SQL/Python changes I made
- Change 1: Changed the query value to 12
- Change 2: Changed the name and year_group order
- Why these changes were mine (not just starter code): These changes were mine because I had to determine what to change and where

## Error and fix
- Error I hit: **no errors**
- How I fixed it:

## Understanding check (answer in your own words)
1. What does `WHERE` do?
It narrows results and matches the rows with the query
2. Why is `?` used in the query?
Used as a placeholder for a parameter in a parameterized query
3. What does `COUNT(*)` tell you in this lesson?
It counts the matching rows

## Quality checklist
- [☑] Script runs without unhandled errors
- [☑] I included at least 2 lesson commits
- [☑] I included filtered/sorted summary evidence
- [☑] I showed a prediction and compared it to actual output
- [☑] I made at least 2 personal changes to the starter work
- [☑] I answered all questions in my own words
