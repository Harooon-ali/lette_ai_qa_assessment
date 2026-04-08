# Security Testing & Findings

## Scope

Security testing focused on authentication, authorization, API abuse, and input validation across the distributed workflow. Since this system relies on multiple independent services, the goal was to identify vulnerabilities that could affect cross-service data integrity, user isolation, and transactional correctness.

The following areas were tested:
- XSS input handling
- broken authentication
- broken authorization
- replay attacks
- rate limit behavior

---

## XSS Testing

**Target:**  
https://the-internet.herokuapp.com/

**Approach:**  
I tested form inputs using script injection payloads to validate whether user input is sanitized.

**Example Payload**
```
<script>alert(1)</script>
```

**Expected Result**  
Input should be sanitized or rendered safely.

**Risk**  
Unsanitized input could allow client-side script execution.

**Impact**
- client-side script execution  
- session compromise  
- unsafe rendering of user input  

---

## Broken Authentication Testing

I tested access to user endpoints without authentication token.

**Scenario**
- login skipped  
- user endpoint accessed directly  

**Expected Result**  
401 Unauthorized

**Risk**  
If access is granted, user data can be retrieved without authentication.

**Impact**
- unauthorized access to user data  
- exposure of protected endpoints  
- reduced trust in authentication layer  

This creates a high-risk security issue in distributed workflows.

---

## Broken Authorization (IDOR)

I tested accessing another user's data using a different identifier.

**Scenario**
- authenticate as user A  
- access data belonging to user B  

**Expected Result**  
Access should be denied.

**Risk**  
Cross-user data exposure.

**Impact**
- data privacy breach  
- incorrect user isolation  
- integrity issues across services  

---

## API Abuse — Replay Attack

I tested replaying the same API request multiple times.

**Example**
- create order request captured  
- resend same request repeatedly  

**Expected Result**  
Duplicate request blocked or handled safely.

**Risk**
Duplicate orders or repeated transactions.

**Impact**
- duplicate records  
- inconsistent order state  
- incorrect analytics  

---

## Rate Limit Simulation

I simulated rapid repeated requests to endpoints.

**Goal**  
Check whether the system detects excessive usage.

**Risk**  
Without rate limiting, APIs can be abused causing:
- denial of service  
- data flooding  
- duplicate records  

**Impact**
- increased service load  
- duplicate operations  
- degraded system performance  

---

## Vulnerability Summary

| Vulnerability | Severity | Impact |
|-------------|----------|--------|
Broken authentication | Critical | Unauthorized access  
Broken authorization | Critical | Cross-user data exposure  
Replay attack | High | Duplicate transactions  
XSS | Medium | Client-side injection  
Missing rate limiting | Medium | API abuse  

---

## Most Critical Vulnerability

The most critical vulnerability in this system is **broken authorization**.

### Reason

If one user can access another user's order data, it directly impacts:
- data privacy  
- data integrity  
- user isolation  
- downstream consistency  

In a distributed system, this type of failure propagates across services and is harder to detect.

### Business Impact

- cross-user data leakage  
- incorrect transaction ownership  
- inconsistent reporting  
- security and compliance risk  

---

## Conclusion

Security testing focused on validating authentication boundaries, user isolation, and API abuse scenarios. The highest-risk issues are those that affect cross-service consistency and user ownership, particularly broken authorization and replayable requests. These vulnerabilities should be treated as release blockers because they affect both system integrity and user trust.
