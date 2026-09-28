from core import handle_customer_message
from memory import close_memory_client

customer_id = "PRIYA001"
message = "My payment issue is happening again."

try:
    response = handle_customer_message(customer_id, message)

    print("\nAurora Resolve response:\n")
    print(response)

finally:
    close_memory_client()