# Security Testing

## Scope

Security testing focused on authentication, authorization, API abuse, and input validation across the distributed workflow.

The goal was to identify vulnerabilities that could affect cross-service data integrity and user isolation.

---

## XSS Testing

Target:
https://the-internet.herokuapp.com/

Approach:
I tested form inputs using script injection payloads to validate whether user input is sanitized.

Example payload:

```<script>alert(1)</script>```   



Expected:
Input is sanitized or rendered safely

Risk:
Unsanitized input could allow client-side script execution.

---

## Broken Authentication Testing

I tested access to user endpoints without authentication token.

Scenario:
- login skipped  
- user endpoint accessed directly  

Expected:
401 Unauthorized

Risk:
If access is granted, user data can be retrieved without authentication.

This creates a high-risk security issue in distributed workflows.

---

## API Abuse — Replay Attack

I tested replaying the same API request multiple times.

Example:
- create order request captured  
- resend same request repeatedly  

Expected:
Duplicate request blocked or handled safely

Risk:
Duplicate orders or repeated transactions.

---

## Rate Limit Simulation

I simulated rapid repeated requests to endpoints.

Goal:
Check whether the system detects excessive usage.

Risk:
Without rate limiting, APIs can be abused causing:
- denial of service
- data flooding
- duplicate records

---

## Most Critical Vulnerability

The most critical vulnerability in this system is **broken authorization**.

Reason:
If one user can access another user's order data, it impacts:
- data privacy
- data integrity
- user isolation
- downstream consistency

In a distributed system, this type of failure propagates across services and is harder to detect.

