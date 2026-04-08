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
