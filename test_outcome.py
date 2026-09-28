from core import record_customer_outcome
from memory import close_memory_client

customer_id = "PRIYA001"

outcome = (
    "Clearing the payment session resolved the recurring "
    "subscription payment issue."
)

try:
    record_customer_outcome(customer_id, outcome)
    print("Verified customer outcome stored successfully.")

finally:
    close_memory_client()