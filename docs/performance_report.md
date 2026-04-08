# Performance Testing Report

## Objective
Validate system behavior under latency and concurrent usage in a distributed environment.

## Target
httpbin delay endpoint  
https://httpbin.org/delay/3

This endpoint simulates slow dependency responses.

## Scenario

Simulated:
- 50 concurrent users
- delayed dependency response
- chained service calls

Workflow tested:
User login → fetch profile → create order → enrichment → validation

## Metrics Measured

- response time
- timeout rate
- failure rate
- retry success rate

## Observations

- latency propagates across dependent services
- order creation is delayed when enrichment is slow
- chained calls amplify total response time
- timeout threshold exceeded during dependency delay

## Bottlenecks

Primary bottleneck:
Orders service dependency

Secondary bottleneck:
GraphQL enrichment latency

## Risk

High latency in dependency services may cause:
- partial workflow completion
- retry storms
- inconsistent data state

## Recommendation

- implement timeout thresholds
- add retry logic with backoff
- introduce async enrichment
- add circuit breaker for dependency failure
