# Data Validation Testing

For data validation, I focused on three critical checks using a Python script:

- order totals vs payment totals  
- missing users referenced by orders  
- duplicate customer or order entries  

The script simulates dataset validation logic that would normally be applied to the Kaggle e-commerce data. Since the assessment uses public services that are not actually integrated, I treated the dataset as a validation layer to confirm whether transactional relationships remain logically correct.

## What I validated

### Order totals vs payments
I compared each order total with the summed payment value for the same `order_id`. Any mismatch was flagged as a data integrity issue because it indicates incomplete or inconsistent transaction data.

### Missing users
I validated whether every `customer_id` referenced in the orders data exists in the customer dataset. Orders linked to non-existent users were flagged as critical inconsistencies.

### Duplicate entries
I checked for duplicate `customer_id` and `order_id` records. Duplicate business identifiers can lead to reporting errors, duplicate transactions, or incorrect downstream analytics.

## How I handle incomplete or dirty data

I handle incomplete or dirty data by:
- standardizing column names before validation
- ignoring nulls only where appropriate and flagging them when they affect business logic
- using left joins and explicit mismatch checks rather than assuming data completeness
- treating missing identifiers and duplicate keys as validation failures, not as acceptable noise

In practice, I prefer to fail clearly on data quality issues that affect correctness, especially around identity, order references, and payments.

## Trade-offs Between Accuracy and Performance

The main trade-off I made was prioritizing validation accuracy over optimization. Since this assessment is focused on correctness and system thinking, I used clear DataFrame-based comparisons that are easy to audit and explain, even if they are not the most optimized approach for very large datasets.

For larger-scale production data, I would improve performance by:
- validating only required columns
- processing in batches
- indexing join keys
- pushing heavy validation into database queries or distributed jobs

For this assessment, a simpler and more transparent validation approach was the better choice because it makes inconsistencies easy to detect and explain.
