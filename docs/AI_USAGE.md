# AI_USAGE.md

## AI Tools Used

* ChatGPT
* GitHub Copilot (if used)

---

## Example Prompts

### Prompt 1

How can I analyze a CSV file using Pandas and identify missing values?

### Prompt 2

How can I generate an import report from detected anomalies?

### Prompt 3

How can I create a SQLite database and import CSV records into it?

---

## AI Mistake #1

### AI Suggestion

Treat missing notes as an error.

### Issue

Notes are optional and should not block imports.

### Fix

Missing notes were accepted without generating an error.

---

## AI Mistake #2

### AI Suggestion

Automatically assume INR when currency is missing.

### Issue

This could produce incorrect financial calculations.

### Fix

Missing currency was flagged for manual review instead.

---

## AI Mistake #3

### AI Suggestion

Treat settlement transactions as normal expenses.

### Issue

Settlement transactions are not actual expenses.

### Fix

Settlement transactions were flagged separately for review.

---

## Human Verification

All AI-generated suggestions were reviewed before implementation. Decisions regarding anomaly handling, database schema, and import behavior were validated manually.
