# Test Cases

## Test Case Format
Each test case includes:
- ID
- Area
- Scenario
- Steps
- Expected Result
- Priority

---

## Authentication

### TC01
**Area:** Authentication  
**Scenario:** Valid login using ReqRes  
**Steps:**  
1. Send valid login request to ReqRes  
2. Provide registered email and password  
3. Submit request  
**Expected Result:**  
Authentication succeeds and token is returned  
**Priority:** High  

### TC02
**Area:** Authentication  
**Scenario:** Invalid login with wrong password  
**Steps:**  
1. Send login request with valid email and wrong password  
2. Submit request  
**Expected Result:**  
Authentication fails with appropriate error response  
**Priority:** High  

### TC03
**Area:** Authentication  
**Scenario:** Login with missing password  
**Steps:**  
1. Send login request with email only  
2. Submit request  
**Expected Result:**  
Validation error returned, login not allowed  
**Priority:** High  

### TC04
**Area:** Authentication  
**Scenario:** Access user profile without token  
**Steps:**  
1. Call protected user endpoint without token  
**Expected Result:**  
Unauthorized access is rejected  
**Priority:** Critical  

### TC05
**Area:** Authentication  
**Scenario:** Access user profile with invalid token  
**Steps:**  
1. Call protected user endpoint with invalid token  
**Expected Result:**  
Request is rejected with authorization failure  
**Priority:** Critical  

---

## User Service

### TC06
**Area:** User Service  
**Scenario:** Fetch valid user profile  
**Steps:**  
1. Request user profile using valid user ID  
**Expected Result:**  
Correct user data is returned  
**Priority:** High  

### TC07
**Area:** User Service  
**Scenario:** Fetch user profile with invalid ID  
**Steps:**  
1. Request user profile using invalid user ID  
**Expected Result:**  
User not found response returned  
**Priority:** Medium  

### TC08
**Area:** User Service  
**Scenario:** User exists in auth service but missing in downstream workflow  
**Steps:**  
1. Authenticate valid user  
2. Attempt workflow where downstream mapping does not contain matching user  
**Expected Result:**  
Mismatch is detected and workflow is flagged  
**Priority:** High  

### TC09
**Area:** User Service  
**Scenario:** Duplicate user records in validation data  
**Steps:**  
1. Run data validation on customer dataset  
2. Check for duplicate identifiers  
**Expected Result:**  
Duplicate records are flagged  
**Priority:** Medium  

---

## Orders Service

### TC10
**Area:** Orders Service  
**Scenario:** Create order with valid user ID  
**Steps:**  
1. Authenticate user  
2. Create order using valid mapped user ID  
**Expected Result:**  
Order is accepted and linked to expected user  
**Priority:** High  

### TC11
**Area:** Orders Service  
**Scenario:** Create order with non-existent user ID  
**Steps:**  
1. Create order using user ID not present in user service  
**Expected Result:**  
Consistency issue is detected  
**Priority:** High  

### TC12
**Area:** Orders Service  
**Scenario:** Create order with missing amount  
**Steps:**  
1. Send order request without amount field  
**Expected Result:**  
Validation error or defect is recorded  
**Priority:** High  

### TC13
**Area:** Orders Service  
**Scenario:** Create order with null amount  
**Steps:**  
1. Send order request with amount set to null  
**Expected Result:**  
Null value is rejected or flagged  
**Priority:** High  

### TC14
**Area:** Orders Service  
**Scenario:** Create duplicate order ID in validation data  
**Steps:**  
1. Run validation against orders dataset  
2. Check for duplicate order_id  
**Expected Result:**  
Duplicate order is flagged  
**Priority:** Medium  

### TC15
**Area:** Orders Service  
**Scenario:** Large payload in order creation  
**Steps:**  
1. Submit order request with unusually large optional payload  
**Expected Result:**  
System handles request safely without corruption  
**Priority:** Medium  

---

## GraphQL / Geo Service

### TC16
**Area:** GraphQL  
**Scenario:** Valid country enrichment query  
**Steps:**  
1. Send valid GraphQL query for country code  
**Expected Result:**  
Correct country data is returned  
**Priority:** Medium  

### TC17
**Area:** GraphQL  
**Scenario:** Invalid GraphQL query syntax  
**Steps:**  
1. Send malformed GraphQL query  
**Expected Result:**  
Explicit query error returned  
**Priority:** Medium  

### TC18
**Area:** GraphQL  
**Scenario:** Query with invalid country code  
**Steps:**  
1. Request country using invalid code  
**Expected Result:**  
No data or controlled failure returned  
**Priority:** Medium  

### TC19
**Area:** GraphQL  
**Scenario:** Over-fetching test  
**Steps:**  
1. Request more country fields than needed  
**Expected Result:**  
System returns data correctly, but inefficiency is noted  
**Priority:** Low  

### TC20
**Area:** GraphQL  
**Scenario:** Under-fetching test  
**Steps:**  
1. Request incomplete country data needed for downstream validation  
**Expected Result:**  
Insufficient data is detected before workflow completion  
**Priority:** Medium  

---

## End-to-End Workflow

### TC21
**Area:** End-to-End  
**Scenario:** Complete workflow succeeds  
**Steps:**  
1. Login user  
2. Fetch profile  
3. Create order  
4. Enrich with country data  
5. Validate against dataset  
**Expected Result:**  
Workflow completes with consistent identifiers and valid data  
**Priority:** Critical  

### TC22
**Area:** End-to-End  
**Scenario:** User exists but order userId does not match  
**Steps:**  
1. Authenticate valid user  
2. Create order with different userId  
**Expected Result:**  
Mismatch is detected and flagged  
**Priority:** Critical  

### TC23
**Area:** End-to-End  
**Scenario:** GraphQL enrichment fails after order creation  
**Steps:**  
1. Authenticate user  
2. Create valid order  
3. Trigger invalid or failed country enrichment  
**Expected Result:**  
Partial failure is visible and does not create false success  
**Priority:** High  

### TC24
**Area:** End-to-End  
**Scenario:** Service returns 200 OK but wrong business data  
**Steps:**  
1. Execute workflow  
2. Inspect returned identifiers and mapped values  
**Expected Result:**  
Silent failure is detected through content validation  
**Priority:** High  

---

## Data Validation

### TC25
**Area:** Data Validation  
**Scenario:** Order total matches payment total  
**Steps:**  
1. Compare order total with aggregated payment value for same order_id  
**Expected Result:**  
Matching values pass validation  
**Priority:** High  

### TC26
**Area:** Data Validation  
**Scenario:** Order total does not match payment total  
**Steps:**  
1. Compare order total with payment value  
2. Use mismatched payment data  
**Expected Result:**  
Mismatch is flagged as integrity defect  
**Priority:** High  

### TC27
**Area:** Data Validation  
**Scenario:** Order references missing customer  
**Steps:**  
1. Compare orders dataset with customers dataset  
2. Identify missing customer_id  
**Expected Result:**  
Invalid order-to-customer mapping is flagged  
**Priority:** High  

### TC28
**Area:** Data Validation  
**Scenario:** Duplicate customer entry  
**Steps:**  
1. Scan customer dataset for duplicate customer_id  
**Expected Result:**  
Duplicate customer is flagged  
**Priority:** Medium  

### TC29
**Area:** Data Validation  
**Scenario:** Duplicate order entry  
**Steps:**  
1. Scan orders dataset for duplicate order_id  
**Expected Result:**  
Duplicate order is flagged  
**Priority:** Medium  

### TC30
**Area:** Data Validation  
**Scenario:** Dirty data with null identifiers  
**Steps:**  
1. Run validation on dataset containing null customer_id or order_id  
**Expected Result:**  
Invalid records are flagged and excluded from trusted validation  
**Priority:** High  

---

## Failure / Chaos Testing

### TC31
**Area:** Failure Testing  
**Scenario:** Orders API times out  
**Steps:**  
1. Simulate delay using httpbin  
2. Run workflow dependent on delayed response  
**Expected Result:**  
Timeout is handled with retry, fallback, or visible failure  
**Priority:** High  

### TC32
**Area:** Failure Testing  
**Scenario:** User API succeeds but Orders API fails  
**Steps:**  
1. Authenticate valid user  
2. Simulate order API failure  
**Expected Result:**  
Workflow does not falsely report success  
**Priority:** High  

### TC33
**Area:** Failure Testing  
**Scenario:** Dependency delay causes full workflow slowdown  
**Steps:**  
1. Add artificial delay to one dependency  
2. Execute full workflow  
**Expected Result:**  
Increased latency is observed and documented  
**Priority:** Medium  

### TC34
**Area:** Failure Testing  
**Scenario:** Retry logic for transient failure  
**Steps:**  
1. Simulate transient dependency failure  
2. Reattempt request using retry logic  
**Expected Result:**  
Transient error is recovered within retry limit  
**Priority:** Medium  

---

## Security Testing

### TC35
**Area:** Security  
**Scenario:** Unauthorized access to another user’s data  
**Steps:**  
1. Authenticate as one user  
2. Attempt to access another user’s order data  
**Expected Result:**  
Access is denied  
**Priority:** Critical  

### TC36
**Area:** Security  
**Scenario:** Replay request  
**Steps:**  
1. Capture valid request  
2. Resend same request multiple times  
**Expected Result:**  
Duplicate or abusive request is detected or limited  
**Priority:** High  

### TC37
**Area:** Security  
**Scenario:** XSS in UI input field  
**Steps:**  
1. Submit `<script>alert(1)</script>` in test form field  
**Expected Result:**  
Input is sanitized or rendered safely  
**Priority:** High  

### TC38
**Area:** Security  
**Scenario:** Rate limit simulation  
**Steps:**  
1. Send repeated rapid requests to same endpoint  
**Expected Result:**  
System rate limits or records abuse pattern  
**Priority:** Medium  

---

## Performance

### TC39
**Area:** Performance  
**Scenario:** 50 concurrent users on delayed endpoint  
**Steps:**  
1. Execute load against httpbin delay endpoint  
2. Measure response time and failure rate  
**Expected Result:**  
Latency and failure behavior are captured  
**Priority:** Medium  

### TC40
**Area:** Performance  
**Scenario:** 100 concurrent users on delayed endpoint  
**Steps:**  
1. Execute higher concurrency load  
2. Compare results with lower load test  
**Expected Result:**  
System bottleneck behavior is observable  
**Priority:** Medium  
