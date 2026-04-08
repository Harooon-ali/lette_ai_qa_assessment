# Test Strategy

This assessment simulates a distributed e-commerce and user management platform using separate public services. Since these services are not actually integrated, my approach was to model them as logical components of one system and validate how data would flow between them. The goal was not only to test individual endpoints or UI elements, but to assess consistency, resilience, and correctness across service boundaries.

## System Components

- **User Service – ReqRes API**  
  Used for authentication, signup/login simulation, and user profile retrieval.

- **Orders Service – JSONPlaceholder**  
  Used to simulate order creation and order retrieval.

- **Geo Service – Countries GraphQL API**  
  Used to enrich user or order data with country information.

- **Reliability Layer – httpbin**  
  Used to simulate delay, timeout, and dependency failure scenarios.

- **Validation Layer – Kaggle E-commerce Dataset**  
  Used to validate customer, order, and payment consistency.

## High-Level Architecture Diagram

```text
[Frontend / UI]
      |
      v
[User Service - ReqRes]
      |
      v
[Orders Service - JSONPlaceholder] -----> [Geo Service - Countries GraphQL]
      |
      v
[Dataset Validation - Kaggle]
      |
      v
[Reliability / Delay Simulation - httpbin]
```


## **Primary workflow tested:**
User login → fetch profile → create order → enrich country → validate dataset.

## Top risks:

- data inconsistency across services
- dependency failure
- broken authentication

## Trade-offs:
I prioritized end-to-end workflow testing and API validation over full UI coverage. Playwright is used for key UI flows, while pytest handles API and data validation. Performance testing focuses on latency behavior using mock endpoints.

I used Playwright for browser-based workflow automation because it is well suited for modern end-to-end testing and reliable waits. I kept Selenium in scope as a relevant browser automation tool, but did not duplicate the same workflow in both frameworks to avoid unnecessary overlap within the assessment timeline.

## Automation approach:
Playwright for UI  
pytest for API + data validation  
Python script for dataset checks  

---

# System Understanding & Risk Analysis

## How I Modelled Data Flow Between Non-Integrated Services

Because these services are independent, I treated them as a logical workflow connected by shared business identifiers such as `userId`, `email`, and `country`. Instead of testing real integration, I simulated cross-service consistency by validating whether output from one service could be reliably used as input to another.

**Example workflow:**
- login user in ReqRes  
- fetch user profile and extract `userId`  
- create simulated order in JSONPlaceholder using that `userId`  
- enrich the user with country data using GraphQL  
- validate the final user/order relationship against dataset rules  

This approach allowed me to test realistic distributed-system risks even though the services are not natively connected.

---

## Assumptions About System Behavior

- ReqRes is treated as the source of truth for user identity  
- JSONPlaceholder represents an orders service but does not enforce true business validation, so consistency checks must be simulated externally  
- Countries GraphQL provides enrichment data only, not transactional data  
- httpbin is used only to simulate reliability issues such as latency or timeout  
- The Kaggle dataset is used as a validation reference for expected relationships between customers, orders, and payments  
- A successful workflow means all required identifiers remain logically consistent across services  

---

## Single Points of Failure

The main single points of failure in this setup are:

- the user service for identity and authentication  
- the orders service for transaction creation  
- the dependency chain between services when one call relies on another  
- external enrichment through GraphQL when country information is required to complete the workflow  

Although the services are separate, the workflow becomes fragile when one dependency fails or returns incomplete data.

---

## Data Inconsistency Risks

The biggest inconsistency risks are:

- a user exists in ReqRes but the order references a different or missing `userId`  
- a country code is missing or does not map correctly in GraphQL  
- dataset validation shows missing customer, duplicate order, or payment mismatch  
- one service returns `200 OK` but the data itself is incomplete or wrong  

A key example is when a user exists in ReqRes but not in Orders. In that case, I would treat it as a consistency defect and validate whether the workflow blocks, flags, or silently accepts invalid data.

---

## Security Risks

The main security risks are:

- broken authentication or missing token enforcement  
- broken authorization such as accessing another user’s data  
- replayable API requests without safeguards  
- unsanitized UI input leading to XSS or malformed data entering the workflow  

---

## Top 3 Risks and Why They Matter Most

### 1. Data inconsistency across services
This is the most critical because distributed systems often fail at service boundaries rather than within a single component. If user and order data do not match, the system may look healthy at API level while still producing invalid business outcomes.

### 2. Broken authentication or authorization
If user data or order data can be accessed without proper validation, the impact is not just functional but also security-related. This is a high-risk failure because it can expose private data.

### 3. Partial dependency failure
If one service succeeds and another fails, the system may end up in a half-complete state. This is especially dangerous when failures are silent and the workflow appears successful.

These risks are more critical than minor UI bugs because they affect trust, correctness, and security of the whole system.

---

## If This System Scaled to 1M Users, What Would Break First?

At higher scale, the first likely issues would be:

- latency caused by chained dependency calls  
- timeouts and retries between services  
- increased inconsistency from partial failures  
- bottlenecks around order creation and enrichment  
- weak observability when debugging cross-service issues  

The workflow is most vulnerable where identity, orders, and enrichment depend on each other synchronously.

---

## Where I Would Place Monitoring and Why

I would place monitoring at:

- authentication boundaries to track failed logins and invalid token access  
- the handoff between user service and orders service to detect mismatched `userId`  
- GraphQL enrichment calls to track latency, failed lookups, and missing country data  
- retry and timeout boundaries to identify unstable dependencies  
- dataset validation checkpoints to catch duplicate, missing, or inconsistent records  

Monitoring should be placed at service boundaries because that is where distributed failures usually become visible.

---

# End-to-End Workflow Testing

## Core Workflow

- user signup/login through ReqRes  
- fetch user profile  
- create order in JSONPlaceholder  
- enrich user or order with country data from GraphQL  
- validate the final relationship against dataset expectations  

---

## What “Success” Means for This Workflow

A successful workflow means:

- authentication succeeds for valid credentials  
- the correct user profile is returned  
- the order is created using the expected `userId`  
- country enrichment returns valid data  
- no mismatch exists between user, order, and validation rules  
- failures are visible and handled explicitly rather than silently ignored  

---

## How I Validated Data Consistency Across Services

I validated consistency by comparing shared identifiers such as:

- `userId` between user and order  
- `email` where applicable  
- `country` or `country code` between profile and GraphQL enrichment  
- dataset-level checks such as whether customer and payment relationships remain valid  

Because the services were not integrated, I treated consistency as a validation layer rather than a system guarantee.

---

## Edge Cases Considered

- user exists but order references a different `userId`  
- order is accepted with missing or null amount  
- GraphQL enrichment fails after order creation  
- a service returns success but the content is incomplete  
- duplicated orders or duplicated customer references  
- delayed dependency causing the full workflow to exceed acceptable response time  

---

## Advanced API Testing

For REST APIs, I validated more than basic success responses. My checks included:

- status codes for expected and unexpected requests  
- schema validation to confirm required fields, types, and structure  
- idempotency for repeated requests where duplicate actions should not create inconsistent outcomes  
- pagination behavior, including page boundaries and missing or invalid page parameters  
- negative testing using invalid payloads, null values, wrong identifiers, and missing required fields  

For GraphQL, I tested:

- valid queries  
- invalid queries  
- query nesting  
- over-fetching vs under-fetching  
- whether failures were returned clearly or silently as partial/null data  

### How I ensured API tests were not just happy-path checks

To avoid only testing successful scenarios, I included:
- invalid payloads  
- missing fields  
- wrong user identifiers  
- malformed requests  
- duplicate or replayed requests  
- null or empty values  
- delayed dependency responses  
- cases where APIs returned technically valid responses but incorrect business data  

This helped validate not just whether the API responds, but whether it responds correctly under realistic failure and edge conditions.

### Schema Validation

I validated whether API responses contained the expected fields, correct data types, and consistent structure. A `200 OK` response was not treated as success unless the payload also matched expected schema and business meaning.

Examples:
- `userId` must be present and valid  
- required fields such as `amount` should not be missing or null  
- response body should match expected structure for downstream use  

### Idempotency

For idempotency, I checked whether repeating the same request caused duplicate or inconsistent results. This is especially important for order creation or retried requests after a timeout.

Example:
- if the same order request is sent twice, the system should not create duplicate business records unless duplication is intentionally allowed  

### Pagination

For endpoints that support pagination, I checked:
- valid page values  
- invalid page values  
- empty pages  
- boundary conditions such as first page, last page, and out-of-range page numbers  

The goal was to confirm the API returns predictable and consistent results across page navigation.

### Detecting Silent Failures

A silent failure happens when the response looks technically successful but the returned data is wrong or incomplete.

I detected silent failures by:
- validating response content, not only status code  
- comparing `userId`, `orderId`, and mapped identifiers across services  
- checking required fields before treating the workflow as successful  
- validating response values against dataset rules and expected business logic  
- flagging cases where the API returns `200 OK` but the data is null, mismatched, or incomplete  

Example:
- an order response returns `200 OK`, but the `userId` does not match the authenticated user  
- GraphQL returns `country: null` while the workflow continues as if enrichment succeeded  

This type of validation is important in distributed systems because many failures are logical rather than technical.

---

# Chaos / Failure Testing

## Objective

The goal of chaos and failure testing was to understand how the distributed workflow behaves when one or more dependencies become slow, fail, or return inconsistent data. Since the services in this assessment are independent, failure testing focused on whether the workflow handles interruptions safely rather than whether a real integration recovers automatically.

---

## Failure Scenarios Simulated

### API Timeout

I used the httpbin delay endpoint to simulate a slow downstream dependency:

```text
https://httpbin.org/delay/3
```

This was used to observe how the workflow behaves when one service takes longer than expected to respond.

Expected behavior:
- timeout is detected clearly
- request does not hang indefinitely
- failure is logged
- retry or fallback is triggered where appropriate

---

### Partial Failure

I simulated a scenario where:
- user API works correctly
- orders API fails

This represents a common distributed system issue where part of the workflow succeeds but the next dependency does not.

Expected behavior:
- workflow should not report false success
- partial completion should be visible
- system should avoid creating inconsistent state
- the error should be surfaced clearly

---

### Data Inconsistency

I simulated mismatched identifiers across services, such as:
- valid user exists in ReqRes
- order is created with a different or invalid `userId`

Expected behavior:
- inconsistency should be detected during validation
- workflow should be flagged or blocked
- mismatch should not be silently accepted

---

## How the System Behaves

In a distributed system, failure in one dependency can affect the full workflow even if other components appear healthy.

From a QA perspective, the most important behaviors to validate are:

- whether the workflow stops safely when a critical dependency fails
- whether partial failures are visible or hidden
- whether retries improve recovery or worsen load
- whether invalid data continues downstream after a mismatch
- whether the system returns a technical success while the business outcome is actually wrong

The biggest risk is not always a complete crash. A more dangerous failure is when the system appears successful but leaves data in a broken or inconsistent state.

---

## Example Scenarios

### Scenario 1: Timeout During Dependency Call
- login succeeds
- profile is fetched
- enrichment or downstream call times out

Risk:
The user may see a failed or incomplete workflow even though the earlier steps succeeded.

### Scenario 2: User API Works, Orders API Fails
- authentication succeeds
- user profile is valid
- order creation fails

Risk:
The system may incorrectly show checkout progress or leave the workflow half-complete.

### Scenario 3: Mismatched User IDs Across Services
- user profile returns `userId = 1`
- order is created with `userId = 3`

Risk:
Workflow technically completes, but the business data is invalid.

---

## What I Would Expect from a Resilient System

A resilient system should:

- fail clearly when a critical dependency cannot be completed
- avoid silent corruption of data
- separate required workflow steps from optional enrichment
- log the failure with enough detail for debugging
- retry only transient failures and not logical defects
- return a user-facing state that reflects the actual workflow outcome

For example, if country enrichment fails but the order is valid, the system may continue with a warning or fallback. But if order creation fails, the system should not continue as if the transaction succeeded.

---

## How I Would Improve Resilience

### 1. Add Retry Logic with Limits
Retries should be used only for transient failures such as timeout or temporary network instability. They should have limits and backoff so they do not create retry storms.

### 2. Validate Data at Service Boundaries
Before passing data from one step to the next, validate critical identifiers such as `userId`, `orderId`, and required fields. This reduces the chance of silent downstream corruption.

### 3. Surface Partial Failure Explicitly
The system should distinguish between:
- full success
- partial success
- hard failure

This is important when optional enrichment fails but the core transaction succeeds.

### 4. Improve Monitoring and Logging
Monitoring should be added around:
- timeout and retry behavior
- user-to-order mapping
- enrichment failures
- partial workflow completion

This makes debugging cross-service failures easier.

### 5. Decouple Optional Dependencies
Optional steps such as enrichment should not block the core workflow if the transaction itself can complete safely. This reduces the impact of non-critical dependency failures.

---

## Conclusion

Chaos and failure testing in this assessment focused on whether the system behaves safely under delay, partial outage, and data inconsistency. The key requirement is not just that failures happen, but that they are visible, controlled, and do not create incorrect business outcomes. In distributed systems, resilience comes from clear boundaries, strong validation, and controlled handling of partial failure.

---

# Test Strategy

## System Understanding & Risk Analysis
(already added)

## End-to-End Workflow Testing
(already added)

## Advanced API Testing
(already added)

## Chaos / Failure Testing
(paste chaos section)

## Observability & Debugging
(paste this section here)

## Production Scenario
(next section)

---


# Observability and Debugging

To debug failures, I captured:

- request payloads  
- response bodies  
- status codes  
- timing information  
- the logical mapping between user and order records  

If logs were missing, I would:

- replay API calls manually  
- inspect browser network traffic  
- compare identifiers across each step of the workflow  
- isolate whether the issue was caused by bad input, dependency failure, or incorrect data mapping  

My debugging approach was to trace the workflow step by step until I identified where expected data diverged from actual data.

---

# Production Scenario: 30 Minutes Before Release

With only 30 minutes before release, I would prioritize the highest-risk paths:

- authentication and login  
- user profile retrieval  
- order creation  
- cross-service consistency between user and order  
- critical authorization checks  
- dependency health for required APIs  

---

## Go / No-Go Decision

My go/no-go decision would be based on whether the core workflow is safe and consistent.

### No-Go
- broken authentication  
- unauthorized access  
- order creation failure  
- mismatched user/order data  
- dependency failure that causes false success  

### Go
- minor UI issue with no effect on core workflow  
- non-critical enrichment issue if fallback exists  
- low-impact cosmetic defect  

---

## Risks I Would Accept

I would accept low-risk, non-blocking issues that do not affect authentication, order integrity, or user data security. I would not accept risks that undermine correctness, trust, or privacy.
