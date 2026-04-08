# Performance Testing Report

## Objective

The purpose of this test was to evaluate how the system behaves when one dependency becomes slow under concurrent usage. Since this assessment uses public mock services, I treated performance testing as a way to validate latency handling, timeout behavior, and failure propagation rather than full production-scale benchmarking.

## Endpoint Used

httpbin delay endpoint: `https://httpbin.org/delay/3`

This endpoint was used to simulate a slow downstream service.

## Test Approach

I simulated concurrent requests in the range of **50 to 100 users** to observe how the workflow behaves under dependency delay.

The goal was to measure:
- response time  
- failure rate  
- timeout behavior  
- effect of retries on overall workflow stability  

Tool considered:
- **k6** for lightweight concurrent API testing  
- **JMeter** as an alternative for higher-volume or GUI-based load simulation  

## Scenario

The delayed endpoint was treated as a dependency within the workflow.

Example flow:
- user authentication succeeds  
- user profile is fetched  
- order creation begins  
- downstream dependency is delayed  
- workflow response time increases or fails depending on timeout handling  

## Metrics That Matter Most and Why

### Response Time
This is the most visible indicator of how dependency latency affects the end-to-end workflow. In a distributed system, even a single slow dependency can increase the total response time significantly.

### Failure Rate
Failure rate matters because it shows how often the workflow breaks under pressure. A system that slows down is one issue, but a system that starts failing requests creates a much higher business risk.

### Timeout Rate
This helps identify whether the system has realistic timeout thresholds and whether delayed dependencies are handled gracefully.

### Retry Success Rate
Retries can improve resilience, but they can also increase load and make bottlenecks worse. Measuring retry success helps determine whether retries are useful or harmful.

## Observations

- delayed responses in one dependency increased total workflow time  
- chained service calls amplified the latency effect  
- failures became more likely when the delayed dependency was part of a synchronous flow  
- without retry or fallback logic, the user-facing workflow became fragile  

## Where I Expect Bottlenecks in This System

The main bottlenecks are likely to appear in:

### Orders Service
The orders flow is central to the business workflow and depends on valid user context. If this service slows down or fails, the most important business transaction is affected.

### GraphQL Enrichment
Country enrichment is an additional dependency. While it may be non-transactional, it can still delay the workflow if called synchronously.

### Chained Service Calls
The biggest bottleneck is not only one service, but the dependency chain itself. When user lookup, order creation, and enrichment happen one after another, the total latency compounds quickly.

### Retry Handling
If retries are added without limits or backoff, transient failures can create extra traffic and worsen the original bottleneck.

## Risk

At moderate concurrency, the biggest risks are:
- slower end-to-end workflow  
- timeout escalation  
- partial completion of requests  
- increased inconsistency if one call succeeds and another fails  

## Recommendation

To improve performance resilience, I would:
- apply sensible timeout thresholds  
- use retry logic with limits and backoff  
- avoid synchronous enrichment for non-critical data  
- monitor dependency latency at service boundaries  
- separate critical workflow steps from optional enrichment where possible  
