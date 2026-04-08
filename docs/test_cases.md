# Test Cases

## Authentication

TC01 valid login  
TC02 invalid login  
TC03 empty credentials  
TC04 invalid token  
TC05 expired token  

## User Service

TC06 fetch user valid  
TC07 fetch user invalid id  
TC08 missing user  
TC09 duplicate user  

## Orders

TC10 create order valid  
TC11 create order invalid user  
TC12 missing amount  
TC13 duplicate order  
TC14 invalid payload  

## GraphQL

TC15 valid country query  
TC16 invalid query  
TC17 nested query  
TC18 missing country  

## Data Consistency

TC19 user exists but order missing  
TC20 order user mismatch  
TC21 duplicate orders  
TC22 missing payment  

## API Negative

TC23 null payload  
TC24 large payload  
TC25 invalid schema  

## Failure Scenarios

TC26 user API works orders fail  
TC27 timeout scenario  
TC28 dependency delay  
TC29 partial workflow failure  

## Security

TC30 unauthorized access  
TC31 replay request  
TC32 XSS input test  
