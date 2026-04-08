# Data Validation Testing

## Objective

The dataset was used as a validation layer to detect inconsistencies between users, orders, and payments across services.

Since the services are not integrated, validation ensures logical consistency of identifiers and totals.

---

## Validations Performed

### Order totals vs payments

I compared order totals with summed payment values for the same order.

Mismatch indicates:
- partial transaction
- duplicate payments
- incorrect totals

---

### Missing users

I validated that every order references an existing user.

Example:
order.userId = 3  
user dataset contains only 1 and 2  

Result:
Invalid order-user mapping

---

### Duplicate entries

I checked for duplicates in:
- customer_id
- order_id

Duplicates can cause:
- double billing
- inconsistent analytics
- incorrect reporting

---

## Validation Logic

Validation implemented using Python script.

Checks include:
- missing users
- duplicate orders
- duplicate customers
- payment mismatch
- null identifiers

---

## Handling Incomplete or Dirty Data

I handled dirty data by:

- normalizing column names
- removing whitespace
- detecting null identifiers
- flagging missing keys
- validating only trusted identifiers

Instead of silently ignoring bad data, I treated:
- null IDs
- duplicate IDs
- missing users
as validation failures.

This ensures correctness over silent acceptance.

---

## Trade-offs Between Accuracy and Performance

I prioritized validation accuracy over optimization.

Reason:
The assessment focuses on correctness and system thinking.

Trade-offs made:
- full dataset scan instead of partial sampling
- explicit joins instead of indexed lookups
- duplicate detection across entire dataset

For large-scale production data, I would optimize by:
- batching validation
- indexing keys
- filtering columns
- pushing validation into database layer

For this assessment, clarity and correctness were more important than performance.
