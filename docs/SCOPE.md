# SCOPE.md

## Project Scope

The application imports an expense CSV file, detects anomalies, generates an import report, and stores valid records in a SQLite database.

---

## Database Schema

### expenses

| Column        | Type                |
| ------------- | ------------------- |
| id            | INTEGER PRIMARY KEY |
| date          | TEXT                |
| description   | TEXT                |
| paid_by       | TEXT                |
| amount        | REAL                |
| currency      | TEXT                |
| split_type    | TEXT                |
| split_with    | TEXT                |
| split_details | TEXT                |
| notes         | TEXT                |
| status        | TEXT                |

---

## Detected Anomalies

### 1. Missing Payer

Description:
Expense record has no value in the paid_by field.

Example:
House cleaning supplies

Action Taken:
Marked as ERROR and excluded from import.

---

### 2. Missing Currency

Description:
Expense record has no currency specified.

Example:
Groceries DMart

Action Taken:
Marked as WARNING for manual review.

---

### 3. Missing Split Type

Description:
Expense record has no split_type value.

Example:
Rohan paid Aisha back

Action Taken:
Marked as WARNING.

---

### 4. Settlement Transaction

Description:
A repayment transaction is present in the expense dataset.

Example:
Rohan paid Aisha back

Action Taken:
Flagged for manual review because it is not a true expense.

---

### 5. Missing Notes

Description:
Several records contain empty notes.

Action Taken:
Accepted because notes are optional.

---

### 6. Potential Logical Duplicate

Description:
Records appear to represent the same expense but use different text formatting.

Examples:

* Dinner at Marina Bites
* dinner - marina bites

Action Taken:
Flagged as potential duplicate for manual review.
