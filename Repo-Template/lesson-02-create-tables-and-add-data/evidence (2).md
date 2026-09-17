# Lesson 02 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message:<br>   75c92f891335e6da53f42386b7ddb9d6d62035c3  
finished fixing the errors in the code, completed the theory questions
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python Repo-Template/lesson-02-create-tables-and-add-data/lesson2_create_table.py
- Terminal output pasted below:
NO OUTPUT IN TERMINAL

## SQL/Python changes I made
- 

## Error and fix
- Error I hit: I kept on getting an error along the lines of: sqlite3.OperationalError: table students has no column named favorite_subject
- How I fixed it: Deleted the previous school.db so it could create a new one

## Understanding check (answer in your own words)
1. Why do we use `commit()`?
We use `commit()` to save database changes permanently.
2. What does `PRIMARY KEY` mean?
`PRIMARY KEY` is a unique indentifier for eaach row
3. Why is `IF NOT EXISTS` useful when creating tables?
It  creates a column, only if it doesn't exist already; otherwise, it just alters the values.

## Quality checklist
- [☑] Script runs without unhandled errors
- [☑] I included at least 2 lesson commits
- [☑] I showed inserts and saved changes
- [☑] I answered all questions in my own words
