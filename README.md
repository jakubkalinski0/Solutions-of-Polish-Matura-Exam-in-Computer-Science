# Solutions of Polish Matura Exam in Computer Science

A collection of solutions to tasks from the Polish high school final exam (matura) in computer science, covering both basic and extended levels. The repository includes programming, database, and spreadsheet tasks from 2005 to 2023.

## Repository structure

| Directory | Description | Tasks |
|-----------|-------------|-------|
| [`coding_tasks/`](coding_tasks/) | Programming tasks in Python | 47 |
| [`database_tasks/`](database_tasks/) | Microsoft Access databases (`.accdb`) with source data files | 36 |
| [`excel_tasks/`](excel_tasks/) | Excel spreadsheets (`.xlsx`) and answer files | 13 |

Each task lives in its own folder. Folder names follow this pattern:

```
<prefix>_<year>_<task_name>
```

### Name prefixes

| Prefix | Meaning |
|--------|---------|
| `mp_` | Basic level matura |
| `mr_sf_` | Extended level matura, old formula (until 2014) |
| `mr_nf_` | Extended level matura, new formula (from 2015) |
| `mr_nf_dod_` | Additional tasks (new formula) |
| `mr_prob_` / `mr_nf_prob_` | Sample / practice tasks |

## Programming tasks (`coding_tasks/`)

Solutions written in Python. A typical folder contains:

- `1.py`, `2.py`, ...: solutions for individual sub-tasks
- `dane.txt`, `przyklad.txt`: input data from the exam paper
- `wyniki*.txt`: generated answers

To run a solution, go to the task folder and execute:

```bash
python 1.py
```

> Scripts expect data files to be in the same directory as the program.

## Database tasks (`database_tasks/`)

Contains Microsoft Access databases (`.accdb`) and text files with source data (`.txt`). Open the databases in Microsoft Access or compatible software and run SQL queries as required by the exam task.

## Spreadsheet tasks (`excel_tasks/`)

Contains Excel workbooks (`.xlsx`) along with text files holding answers to theoretical sub-questions. Requires Microsoft Excel or a compatible spreadsheet editor.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Jakub Kaliński
