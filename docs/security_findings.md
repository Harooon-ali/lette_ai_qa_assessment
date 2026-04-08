# Security Testing Findings

## Scope

Security testing focused on:
- authentication
- authorization
- API abuse
- input validation
- cross-service data exposure

---

## Finding 1: Broken Authentication

Severity: Critical

Description:
User data accessible without token validation.

Steps:
Call user endpoint without authentication token

Expected:
401 Unauthorized

Actual:
200 response returned

Impact:
Unauthorized data access

---

## Finding 2: IDOR (Insecure Direct Object Reference)

Severity: Critical

Description:
User can access another user's order using different userId.

Example:
GET /orders?userId=2

Expected:
Access restricted

Actual:
Data returned

Impact:
Cross-user data exposure

---

## Finding 3: Replay Attack

Severity: High

Description:
Same request can be replayed without validation.

Impact:
Duplicate orders
Duplicate transactions

---

## Finding 4: XSS Risk

Severity: Medium

Description:
Input fields accept unsanitized HTML.

Example:
<script>alert(1)</script>

Impact:
Client-side script execution

---

## Most Critical Vulnerability

Broken authorization allowing cross-user data access.

This impacts:
- data privacy
- data integrity
- user isolation
