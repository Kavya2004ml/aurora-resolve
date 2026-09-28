from memory import retain_memory, close_memory_client

try:
    retain_memory(
        "Customer ARJUN002 had a login issue. "
        "Resetting the password did not solve the issue. "
        "Unlocking the account resolved the issue."
    )

    print("Arjun memory stored successfully.")

finally:
    close_memory_client()