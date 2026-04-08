# Automation Framework

## Approach

Automation focuses on:
- core workflow
- API validation
- data consistency

Tools used:
- Playwright (UI)
- pytest (API)
- Python (data validation)

## Framework Structure

tests/
api/
ui/
clients/
data/

## Automated Scenarios

- login workflow
- user retrieval
- order creation
- cross-service consistency
- invalid payload handling

## Retry Logic

Retries added for:
- timeout
- transient failures
- dependency delay

## Data Driven Tests

Parameterized tests using:
- user dataset
- order dataset
- invalid payloads

## Parallel Execution

pytest-xdist used for parallel test runs.

## What I Automated

- core workflow
- API validation
- consistency checks

## What I Did Not Automate

- exploratory security testing
- performance testing
- chaos testing

Reason:
These require manual validation and environment control.
