# CLI Expense Tracker

A command-line tool to track expenses, built with Python and argparse.

## Features
- Add expenses with amount, category, and date
- List all expenses, or filter by category
- View monthly spending summaries
- Delete expenses by index

## Usage

Add an expense:
python tracker.py add --amount 45 --category transport --date 08-08-2026

List all expenses:
python tracker.py list

List expenses in a specific category:
python tracker.py list --category coffee

View monthly totals:
python tracker.py summary

Delete an expense by index:
python tracker.py delete --index 0

## What I learned
- Working with JSON files for persistence (load/append/save pattern)
- Building a CLI with argparse subcommands
- Handling edge cases like missing files and invalid indexes
- Accumulating and grouping data using dictionaries