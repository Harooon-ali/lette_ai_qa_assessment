# Bug Reports

Bug 1: Data inconsistency across services  
Severity: High  
Description: Order created with userId not present in user service.  
Payload:  

{ "id":102, "userId":3 }

Expected:
Validation failure

Actual:
Order accepted

Impact:
Invalid business data

----

Bug 2: Unauthorized access  

Severity: Critical  
Accessing another user's data without authentication.  

Steps:  
Call user endpoint without token  

Expected:  
401 unauthorized  

Actual:  
200 response  
