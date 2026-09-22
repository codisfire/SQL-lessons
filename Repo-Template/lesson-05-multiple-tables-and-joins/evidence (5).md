# Lesson 05 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: 56656a76090369ca99ebb3a9e448578d0d15aa04 <br>
started to write the code for lesson 5, put in the 3rd hash and commit message for lesson 4
- Commit 2 hash + message:e88a8e29da5a628d8bd6bcdd0916d02d761e8628 <br>
i finished writing the code in, and im planning to do the practical questions, theory questions, and quality checklist next lesson
- Optional Commit 3 hash + message: 

## Run evidence
- Command run: python Repo-Template/lesson-05-multiple-tables-and-joins/lesson5_join.py
- Terminal output pasted below:
('Ava', 'Science Club')
('Leo', 'Math Team')
## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
I added a new cursor.execute in order to insert a new course (Chess Club) and assigned it to Leo's id.
## Prediction before run
- JOIN query version: 
```
cursor.execute("""
SELECT students.name, courses.course_name
FROM students
JOIN courses ON students.id = courses.student_id
""")
```
- My prediction (student-course pairs): I predicted that Ava would be assigned the Science club, and Leo would be assigned both the Math and Chess Teams
- What actually happened:
My prediction was correct
## SQL/Python changes I made
- Change 1: made a new cursor.execute function for The Chess Team and assigned it to Leo
- Change 2: Changed the Math club to the Software Team
- Why these changes were mine (not just starter code): I inserted another course by writing the code that I thought of my by own brain because I actually paid attention in these lessons

## Error and fix
- Error I hit: Didn't hit any errors
- How I fixed it: N/A

## Understanding check (answer in your own words)
1. Why do we use more than one table?
Using more than one table enables us to combine information whilst reducing repeated data
2. What is the purpose of `JOIN`?
The purpose of join is to combine relevent information from more than one tab;le
3. Which columns connect your two tables?
student_id's

## Quality checklist
- [☑] Script runs without unhandled errors
- [☑] I included at least 2 lesson commits
- [☑] I included joined output evidence
- [☑] I showed a prediction and compared it to actual output
- [☑] I made at least 2 personal changes to the starter work
- [☑] I answered all questions in my own words
