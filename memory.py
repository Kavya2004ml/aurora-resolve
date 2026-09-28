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

    result = client.recall(
        bank_id=bank_id,
        query=query
    )

    for memory in result.results:
        if customer_marker.lower() in memory.text.lower():
            memories.append(memory.text)

    if not memories:
        fallback_result = client.recall(
            bank_id=bank_id,
            query=f"Support history for Customer {customer_id}"
        )

        for memory in fallback_result.results:
            if customer_marker.lower() in memory.text.lower():
                memories.append(memory.text)

    return memories


def close_memory_client():
    client.close()