# Automation Framework

## Overview

This automation framework focuses on validating core distributed workflows across UI, APIs, and dataset validation. The goal is to automate high-risk paths rather than every possible scenario.

## Tools Used

- Playwright for UI automation
- pytest for API testing
- Python for data validation
- requests for API client
- pytest-xdist for parallel execution

## Framework Structure

```
automation/
  tests/
    test_login.py
    test_order_flow.py
    test_data_consistency.py

  api/
    client.py

  ui/
    pages/
      login_page.py

  data/
    test_data.json
```

## Design Approach

The framework follows:

- Page Object Model for UI tests
- API client abstraction for REST calls
- data-driven tests using pytest parameters
- retry logic for unstable dependencies
- modular test organization

## Automated Scenarios

The following workflows are automated:

- user login validation
- fetch user profile
- create order
- cross-service data consistency
- invalid payload handling
- silent failure detection

## Retry Logic

Retry logic implemented for:

- API timeout
- transient failures
- delayed dependency responses

Retries are limited to avoid masking real failures.

## Data Driven Testing

Tests run with:

- valid users
- invalid users
- duplicate data
- missing fields
- mismatched identifiers

## Parallel Execution

Parallel execution enabled using:

pytest -n auto

This allows concurrent API and validation tests.

## What Was Automated

- core workflow validation
- API consistency tests
- data validation checks
- negative scenarios

## What Was Not Automated

- exploratory security testing
- performance load testing
- manual UI exploration

These require environment control and manual validation.

## Why This Structure

This structure allows:

- separation of UI and API logic
- reusable API client
- scalable test additions
- maintainable automation suite
- easy parallel execution

The focus was on stability, readability, and distributed-system validation.
