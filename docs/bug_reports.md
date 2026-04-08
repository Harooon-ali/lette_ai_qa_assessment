# Bug Reports

---

## Bug 1: Data inconsistency between user and order

Severity: High  
Priority: P1

Description:
Order created with userId not present in user service.

Payload:
{
"id":102,
"userId":3
}

Expected:
Validation error

Actual:
Order accepted

Impact:
Invalid business data

---

## Bug 2: Unauthorized user data access

Severity: Critical  
Priority: P0

Description:
User data accessible without authentication.

Steps:
Call user endpoint without token

Expected:
401 unauthorized

Actual:
200 response

Impact:
Security breach

---

## Bug 3: Silent failure in GraphQL enrichment

Severity: Medium  
Priority: P2

Description:
GraphQL returns empty country but API success.

Expected:
Error or fallback

Actual:
Workflow continues silently

Impact:
Incorrect enrichment

---

## Bug 4: Timeout not handled

Severity: High  
Priority: P1

Description:
Dependency delay causes workflow failure.

Endpoint:
httpbin delay

Expected:
Retry or fallback

Actual:
Failure not handled
