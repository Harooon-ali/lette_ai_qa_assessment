import pandas as pd

# Sample simulated data based on the assessment requirement.
# In a real version, these would be loaded from Kaggle CSV files.
customers = pd.DataFrame([
    {"customer_id": "C1", "customer_unique_id": "U1"},
    {"customer_id": "C2", "customer_unique_id": "U2"},
    {"customer_id": "C2", "customer_unique_id": "U2"}  # duplicate customer
])

orders = pd.DataFrame([
    {"order_id": "O1", "customer_id": "C1", "order_total": 100.0},
    {"order_id": "O2", "customer_id": "C3", "order_total": 200.0},  # missing user
    {"order_id": "O2", "customer_id": "C3", "order_total": 200.0}   # duplicate order
])

payments = pd.DataFrame([
    {"order_id": "O1", "payment_value": 100.0},
    {"order_id": "O2", "payment_value": 150.0}  # payment mismatch
])


def validate_missing_users(orders_df: pd.DataFrame, customers_df: pd.DataFrame):
    valid_customers = set(customers_df["customer_id"].dropna())
    missing_user_orders = orders_df[~orders_df["customer_id"].isin(valid_customers)]
    return missing_user_orders


def validate_duplicate_entries(df: pd.DataFrame, key_columns: list[str]):
    duplicates = df[df.duplicated(subset=key_columns, keep=False)]
    return duplicates


def validate_order_totals_vs_payments(orders_df: pd.DataFrame, payments_df: pd.DataFrame):
    payment_totals = payments_df.groupby("order_id", as_index=False)["payment_value"].sum()
    merged = orders_df.merge(payment_totals, on="order_id", how="left")
    merged["payment_value"] = merged["payment_value"].fillna(0)
    mismatches = merged[merged["order_total"] != merged["payment_value"]]
    return mismatches


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    return df


def main():
    clean_customers = clean_data(customers)
    clean_orders = clean_data(orders)
    clean_payments = clean_data(payments)

    print("\n=== Missing Users Validation ===")
    missing_users = validate_missing_users(clean_orders, clean_customers)
    if missing_users.empty:
        print("No missing users found.")
    else:
        print(missing_users.to_string(index=False))

    print("\n=== Duplicate Customers ===")
    duplicate_customers = validate_duplicate_entries(clean_customers, ["customer_id"])
    if duplicate_customers.empty:
        print("No duplicate customers found.")
    else:
        print(duplicate_customers.to_string(index=False))

    print("\n=== Duplicate Orders ===")
    duplicate_orders = validate_duplicate_entries(clean_orders, ["order_id"])
    if duplicate_orders.empty:
        print("No duplicate orders found.")
    else:
        print(duplicate_orders.to_string(index=False))

    print("\n=== Order Totals vs Payments Validation ===")
    mismatched_payments = validate_order_totals_vs_payments(clean_orders, clean_payments)
    if mismatched_payments.empty:
        print("No order/payment mismatches found.")
    else:
        print(mismatched_payments.to_string(index=False))


if __name__ == "__main__":
    main()
