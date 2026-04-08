# Bug Reports

---

## Bug 1 — Order created with non-existent userId

**Severity:** High  
**Priority:** P1  

### Description
Order is accepted even when `userId` does not exist in user service.

### Steps to Reproduce
1. Authenticate valid user  
2. Create order using `userId = 999`  
3. Submit request  

### Request Payload
```json
{
  "id": 102,
  "userId": 999,
  "amount": 200
}
```

### Expected Result
Order should be rejected due to invalid user mapping.

### Actual Result
Order is accepted and returned with success response.

### Response
```json
{
  "id": 102,
  "userId": 999,
  "amount": 200
}
```

### Impact
Creates inconsistent business data and breaks referential integrity.

---

## Bug 2 — Unauthorized access to another user’s data

**Severity:** Critical  
**Priority:** P0  

### Description
User can access another user's data without proper authorization.

### Steps to Reproduce
1. Authenticate as user A  
2. Call orders endpoint with `userId` of user B  

### Request
```
GET /orders?userId=2
```

### Expected Result
Access denied with authorization error.

### Actual Result
Order data returned successfully.

### Response
```json
[
  {
    "id": 201,
    "userId": 2,
    "amount": 150
  }
]
```

### Impact
Cross-user data exposure. Security vulnerability.

---

## Bug 3 — GraphQL silent failure

**Severity:** Medium  
**Priority:** P2  

### Description
Invalid country query returns empty result but workflow continues.

### Query
```graphql
{
  country(code: "XX") {
    name
  }
}
```

### Expected Result
Error or fallback handling.

### Actual Result
Empty response returned and workflow continues.

### Response
```json
{
  "data": {
    "country": null
  }
}
```

### Impact
Incorrect data enrichment without failure visibility.

---

## Bug 4 — Timeout not handled

**Severity:** High  
**Priority:** P1  

### Description
Delayed dependency causes workflow failure without retry.

### Endpoint
```
https://httpbin.org/delay/3
```

### Steps
1. Call dependent workflow  
2. Trigger delay endpoint  

### Expected Result
Retry or timeout handling.

### Actual Result
Workflow fails immediately.

### Log
```
TimeoutError: request exceeded 2s threshold
```

### Impact
Dependency instability causes system failure.

---

## Bug 5 — Duplicate order accepted

**Severity:** Medium  
**Priority:** P2  

### Description
Duplicate order ID allowed.

### Payload
```json
{
  "id": 101,
  "userId": 1,
  "amount": 100
}
```

Sent twice.

### Expected Result
Second request rejected.

### Actual Result
Both requests accepted.

### Impact
Duplicate transaction records.

---

## Bug 6 — Payment mismatch not detected

**Severity:** High  
**Priority:** P1  

### Description
Order total does not match payment value.

### Order
```json
{
  "order_id": "O1",
  "total": 100
}
```

### Payment
```json
{
  "order_id": "O1",
  "payment": 50
}
```

### Expected Result
Mismatch flagged.

### Actual Result
Accepted without validation.

### Impact
Financial inconsistency.

---

## Bug 7 — Missing required field accepted

**Severity:** High  
**Priority:** P1  

### Description
Order accepted without amount.

### Payload
```json
{
  "id": 104,
  "userId": 1
}
```

### Expected Result
Validation error.

### Actual Result
Order created.

### Impact
Invalid order data.

---

## Bug 8 — XSS vulnerability in input

**Severity:** Medium  
**Priority:** P2  

### Input
```
<script>alert(1)</script>
```

### Expected Result
Input sanitized.

### Actual Result
Script executed.

### Impact
Client-side vulnerability.

---

## Bug 9 — Retry logic missing

**Severity:** Medium  
**Priority:** P2  

### Description
Transient failure not retried.

### Steps
1. Simulate temporary API failure  
2. Retry not triggered  

### Expected Result
Retry within threshold.

### Actual Result
Immediate failure.

### Impact
Reduced resilience.

---

## Bug 10 — 200 OK but wrong data returned

**Severity:** High  
**Priority:** P1  

### Description
API returns success but wrong user mapping.

### Response
```json
{
  "userId": 5,
  "orderId": 101
}
```

### Expected userId
```
1
```

### Expected Result
Mismatch detected.

### Actual Result
Workflow continues.

### Impact
Silent data corruption.
