# Assessment Overview (Non-Technical Summary)

This submission demonstrates how I would test a distributed system made up of multiple independent services. Instead of testing a single application, the goal was to validate how different components behave together and how failures affect the overall workflow.

The system simulates a simple flow:

User logs in → profile fetched → order created → country added → data validated

Each step uses a different public service, so testing focused on whether data stays consistent and whether the system behaves correctly when something goes wrong.

## What I Tested

I focused on:

- user authentication  
- order creation  
- cross-service data consistency  
- API failures and delays  
- incorrect or missing data  
- security vulnerabilities  
- performance under load  

The goal was to detect issues that could affect correctness, reliability, and security.

## What This Repository Contains

Test Strategy  
Explains how the system works, key risks, and how testing was prioritized.

Test Cases  
Positive, negative, and edge case scenarios for the main workflow.

Bug Reports  
Example defects with severity, logs, and impact.

Automation Approach  
How core scenarios would be automated using pytest and Playwright.

Data Validation  
Python script to detect missing users, duplicates, and payment mismatches.

Performance Testing  
Simulation of delayed dependencies and concurrent users.

Security Testing  
Checks for authentication issues, replay attacks, and input validation.

Chaos Testing  
Testing partial failures and timeout scenarios.

Production Decision  
Risk-based approach for deciding whether the system is safe to release.

## Goal of This Assessment

The goal was not just to test individual features, but to:

- understand the system as a whole  
- detect cross-service inconsistencies  
- validate behavior during failures  
- identify security risks  
- prioritize testing based on impact  

This reflects a real-world QA approach for distributed systems.
