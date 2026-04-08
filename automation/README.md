# Automation Framework

## Objective

The automation approach focuses on validating the highest-risk parts of the distributed workflow using Python and pytest. Since the assessment combines UI, APIs, and data validation, I chose a framework that keeps these concerns separate but reusable.

The main goal was to automate stable, repeatable checks around authentication, order creation, and cross-service consistency rather than trying to automate every possible scenario.

---

## Language and Test Framework

- Python  
- pytest  

Python was chosen because it is simple, readable, and well suited for API testing, data validation, and test orchestration. pytest provides a clean structure for fixtures, parameterization, assertions, and parallel execution.

---

## Framework Design

The framework is structured into separate layers so UI, API, and data logic are easy to maintain.

### Page Object Model (POM)

For UI testing, I used a Page Object Model structure. This keeps page locators and page actions separate from the actual test logic.

Example:
- login page contains locators and actions for email, password, and submit  
- tests only call reusable methods such as `login()` instead of repeating selectors everywhere  

This improves readability and reduces maintenance when UI changes.

---

### API Client Layer

For API testing, I used an API client layer to centralize request logic.

This layer is responsible for:
- sending requests  
- setting headers  
- reusing base URLs  
- handling authentication tokens  
- applying retry logic where needed  

This avoids repeating raw request code in each test and makes the framework easier to scale.

---

## Suggested Structure

```
automation/
  tests/
    test_login.py
    test_order_flow.py
    test_data_consistency.py

  ui/
    pages/
      login_page.py

  api/
    client.py

  data/
    test_data.json

  conftest.py
```

---

## Retry Logic

Retry logic is included for transient failures such as:
- timeout  
- temporary service delay  
- unstable dependency response  

Retries are useful for dependency-level instability, but they should be limited so real failures are not hidden.

I would apply retry logic mainly to:
- delayed API calls  
- dependency timeouts  
- non-deterministic transient failures  

I would not use retries to mask functional defects like invalid data or authorization failures.

---

## Data-Driven Tests

I used data-driven testing to run the same test logic with multiple inputs.

Examples:
- valid and invalid login credentials  
- valid and invalid `userId`  
- missing required fields  
- duplicate or mismatched data  
- null and malformed payloads  

This helps expand coverage without duplicating the same test structure repeatedly.

In pytest, this would typically be implemented using parameterization.

---

## Parallel Execution

Parallel execution is included using pytest-compatible parallel execution tools such as `pytest-xdist`.

This helps:
- reduce runtime  
- execute API tests more efficiently  
- separate independent scenarios into parallel runs  

Parallel execution is most suitable for:
- API tests  
- validation tests  
- non-dependent negative scenarios  

I would be more careful with parallel execution for UI tests if shared state or test data collisions are possible.

---

## What I Chose to Automate

I chose to automate:
- login and authentication checks  
- user retrieval  
- order creation workflow  
- cross-service consistency validation  
- negative API scenarios  
- data validation checks  

These are the most repeatable and highest-risk parts of the system. They are also the areas where automation gives the most value for regression testing.

---

## What I Chose Not to Automate

I did not prioritize automation for:
- exploratory security testing  
- deep manual UI exploration  
- full performance/load testing  
- all chaos scenarios  

Reason:
These areas often require manual analysis, environment control, or specialized tooling beyond a standard pytest workflow.

For example:
- XSS testing is better supported by targeted manual validation plus security tools  
- performance testing is better handled by k6 or JMeter  
- chaos testing often needs controlled fault injection rather than only scripted assertions  

---

## Why I Chose This Framework Structure

I chose this structure because it supports both clarity and scalability.

Benefits:
- UI logic is separated using POM  
- API logic is centralized in one client layer  
- tests remain readable and focused on behavior  
- data-driven tests improve coverage  
- retry logic supports resilience testing  
- parallel execution reduces runtime  

Most importantly, the structure reflects the distributed nature of the system. Instead of treating each test as an isolated script, the framework is organized around reusable components that mirror how real workflows move between UI, APIs, and validation layers.
