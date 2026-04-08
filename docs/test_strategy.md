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

### How I Modelled Data Flow Between Non-Integrated Services  

Because these services are independent, I treated them as a logical workflow connected by shared business identifiers such as userId, email, and country. Instead of testing real integration, I simulated cross-service consistency by validating whether output from one service could be reliably used as input to another.  


Example:
- login user in ReqRes
- fetch user profile and extract userId
- create simulated order in JSONPlaceholder using that userId
- enrich the user with country data using GraphQL
- validate the final user/order relationship against dataset rules



This approach allowed me to test realistic distributed-system risks even though the services are not natively connected.



### Assumptions About System Behavior
- ReqRes is treated as the source of truth for user identity.
- JSONPlaceholder represents an orders service but does not enforce true business validation, so consistency checks must be simulated externally.
- Countries GraphQL provides enrichment data only, not transactional data.
- httpbin is used only to simulate reliability issues such as latency or timeout.
- The Kaggle dataset is used as a validation reference for expected relationships between customers, orders, and payments.
- A successful workflow means all required identifiers remain logically consistent across services.


### Single Points of Failure

The main single points of failure in this setup are:  

- the user service for identity and authentication
- the orders service for transaction creation
- the dependency chain between services when one call relies on another
- external enrichment through GraphQL when country information is required to complete the workflow



Although the services are separate, the workflow becomes fragile when one dependency fails or returns incomplete data.
