from memory import recall_memory, close_memory_client

customers = [
    ("PRIYA001", "My payment issue is happening again."),
    ("ARJUN002", "I can't log in again."),
    ("NEHA003", "I'm having trouble cancelling my subscription.")
]

try:
    for customer_id, message in customers:
        print("\n" + "=" * 60)
        print(f"Customer: {customer_id}")
        print(f"Query: {message}")
        print("=" * 60)

        memories = recall_memory(
            customer_id=customer_id,
            query=message
        )

        if memories:
            for i, memory in enumerate(memories, 1):
                print(f"\nMemory {i}:")
                print(memory)
        else:
            print("\nNO MEMORY FOUND")

finally:
    close_memory_client()