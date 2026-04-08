# QA + AI Distributed System Testing Assessment

This repository contains my approach to testing a distributed system composed of UI, REST APIs, GraphQL services, and dataset validation. The goal of this assessment is to demonstrate system thinking, risk-based testing, and validation of cross-service consistency.

The system simulates an e-commerce and user management platform using independent public services. Since these services are not actually integrated, the focus is on validating logical data flow, detecting inconsistencies, and handling partial failures.

## System Components

User Service: ReqRes  
Orders Service: JSONPlaceholder  
Geo Service: Countries GraphQL API  
Reliability Layer: httpbin  
Validation Layer: Kaggle E-commerce Dataset  

## Primary Workflow

User login → fetch profile → create order → enrich country → validate dataset

This workflow is validated across independent services to detect:
- data inconsistency
- dependency failures
- authentication issues
- silent API failures
- performance bottlenecks

## Repository Structure

```
docs/
  test_strategy.md
  test_cases.md
  bug_reports.md
  performance_report.md
  security_findings.md
  coverage_matrix.md

automation/
  README.md

data_validation/
  validate_data.py
```

## Testing Scope

This assessment covers:

- system understanding and risk analysis
- end-to-end workflow validation
- REST API testing
- GraphQL testing
- performance testing
- security testing
- data validation using dataset
- automation using pytest and Playwright
- chaos and failure scenarios
- observability and debugging
- production readiness decision

## Automation Approach

Automation focuses on core workflow validation using:

- Playwright for UI flows
- pytest for API testing
- Python for dataset validation
- retry logic for unstable dependencies
- data-driven tests
- modular test structure

## Data Validation

Dataset validation checks:

- order totals vs payments
- missing users
- duplicate entries
- inconsistent identifiers

Implemented using Python script in `data_validation/`.

## Performance Testing

Latency simulated using httpbin delay endpoint.

Metrics measured:
- response time
- failure rate
- timeout behavior
- dependency bottlenecks

## Security Testing

Security validation includes:

- broken authentication
- authorization checks
- replay attacks
- XSS validation
- rate limit simulation

## Chaos Testing

Failure scenarios simulated:

- API timeout
- partial service failure
- data mismatch
- dependency delay

## Production Readiness

Risk-based validation performed for:

- authentication
- order creation
- cross-service consistency
- dependency health

Go/no-go decision based on workflow integrity and data correctness.

## Goal

The objective of this assessment is not only to test features, but to evaluate:

- distributed system thinking
- debugging approach
- risk prioritization
- cross-service validation
- real-world QA strategy
