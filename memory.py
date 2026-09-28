import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

bank_id = os.getenv("HINDSIGHT_BANK_ID")


def retain_memory(content):
    client.retain(
        bank_id=bank_id,
        content=content
    )


def recall_memory(customer_id, query):
    customer_marker = f"Customer {customer_id}"
    memories = []

    print(f"DEBUG customer_id: {customer_id}")
    print(f"DEBUG bank_id: {bank_id}")

    # First recall
    result = client.recall(
        bank_id=bank_id,
        query=query
    )

    print(f"DEBUG first recall count: {len(result.results)}")

    for memory in result.results:
        print(f"DEBUG recalled text: {memory.text}")

        if customer_marker.lower() in memory.text.lower():
            memories.append(memory.text)

    print(f"DEBUG filtered count after first recall: {len(memories)}")

    # Fallback
    if not memories:
        fallback_result = client.recall(
            bank_id=bank_id,
            query=f"Support history for Customer {customer_id}"
        )

        print(f"DEBUG fallback recall count: {len(fallback_result.results)}")

        for memory in fallback_result.results:
            print(f"DEBUG fallback text: {memory.text}")

            if customer_marker.lower() in memory.text.lower():
                memories.append(memory.text)

    print(f"DEBUG final memory count: {len(memories)}")

    return memories


def close_memory_client():
    client.close()