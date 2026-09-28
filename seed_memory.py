from memory import retain_memory, close_memory_client

try:
    retain_memory(
        "Customer PRIYA001 had a subscription payment failure. "
        "Restarting the app did not resolve the issue. "
        "Clearing the payment session resolved the issue."
    )

    print("Clean Priya memory stored successfully.")

finally:
    close_memory_client()