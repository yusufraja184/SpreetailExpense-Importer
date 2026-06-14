# DECISIONS.md

## Decision 1: Database Selection

### Options Considered

* SQLite
* PostgreSQL
* MySQL

### Selected

SQLite

### Reason

The dataset is small and SQLite is lightweight, easy to set up, and sufficient for the assignment requirements.

---

## Decision 2: Handling Missing paid_by

### Options Considered

* Import the record anyway
* Assign a default user
* Reject the record

### Selected

Reject the record

### Reason

The payer is a critical field. Without it, ownership of the expense cannot be determined accurately.

---

## Decision 3: Handling Missing Currency

### Options Considered

* Assume INR
* Reject the record
* Flag for manual review

### Selected

Flag for manual review

### Reason

Assuming a currency automatically could lead to incorrect financial calculations.

---

## Decision 4: Settlement Transactions

### Options Considered

* Treat as a normal expense
* Ignore completely
* Flag separately

### Selected

Flag separately

### Reason

Settlement transactions represent money transfers between people and are not actual expenses.

---

## Decision 5: Missing Notes

### Options Considered

* Reject records
* Require notes
* Allow missing notes

### Selected

Allow missing notes

### Reason

Notes are optional metadata and do not affect expense calculations.

---

## Decision 6: Import Report Generation

### Options Considered

* Display anomalies only in terminal
* Generate a report file

### Selected

Generate import_report.txt

### Reason

The assignment explicitly requires an import report listing anomalies and actions taken.

---

## Decision 7: Technology Stack

### Selected Stack

* Python
* Pandas
* SQLite
* Git/GitHub

### Reason

This stack supports both data analysis and software engineering requirements while remaining simple to deploy and maintain.
