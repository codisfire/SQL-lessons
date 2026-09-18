# Lesson 03 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: af18bd1fafe14cdd583c4466bbc523730c875b79 <br>
started lesson 3, created the file
- Commit 2 hash + message: e55e74c3fdd5dbc19087af2bf6d7500145b1cfb7 <br>
finished code + theory questions for lesson 3, and quality checklist
- Optional Commit 3 hash + message:

## Run evidence
- Command run:
- Terminal output pasted below:
```
(1, 'Ava', 10)
(2, 'Leo', 10)
(3, 'John', 12)
```
## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
First, I changed ```cursor.execute("SELECT id, name, year_group FROM students")``` to ```cursor.execute("SELECT name FROM students")```. Then, after seeing the output, I changed the cursor.execute function back to how it previously was, and then I changed the output from 
```
for row in rows:
    print(row)
```
to 
```
for student_id, name, year_group in rows:
print(f"{name} is in year {year_group}.")
```


## Prediction before run
- Query version: cursor.execute("SELECT name FROM students")
- My prediction (rows/columns or sample output): I predicted it would just print out the names
- What actually happened: printed out the names, in a numbered list
## SQL/Python changes I made
- Change 1: cursor.execute("SELECT name FROM students")
- Change 2: for student_id, name, year_group in rows:
print(f"{name} is in year {year_group}.")
- Why these changes were mine (not just starter code): These changes were mine as I decided where to put each change, and I also decided what to replace with the new change. 

## Error and fix
- Error I hit: ValueError: not enough values to unpack (expected 3, got 1)
- How I fixed it: I didn't change the execute.cursor function back to normal before I typed in the new output, and it tried to retrieve information that wasn't available

## Understanding check (answer in your own words)
1. What is the job of `SELECT`?
 `SELECT`'s job is to read data
2. What type of value does `fetchall()` return?
 `fetchall()` returns all returned rows from a query
3. How did your output change when you selected fewer columns?
When I selected fewer colums, it would give me less data in the output

## Quality checklist
- [☑] Script runs without unhandled errors
- [☑] I included at least 2 lesson commits
- [☑] I included query output evidence
- [☑] I showed a prediction and compared it to actual output
- [☑] I made at least 2 personal changes to the starter work
- [☑] I answered all questions in my own words
