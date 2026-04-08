# Test Strategy
This system represents a distributed architecture composed of user service, orders service, geo service, and reliability layer. Since these services are not integrated, testing focuses on validating consistency between responses and detecting partial failures.

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
