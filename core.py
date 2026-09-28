from memory import recall_memory, retain_memory
from llm import generate_response


from memory import recall_memory
from llm import generate_response


def handle_customer_message(customer_id, user_message):
    try:
        memory_query = (
            f"Relevant previous support history for customer {customer_id} "
            f"related to: {user_message}"
        )

        memories = recall_memory(
            customer_id=customer_id,
            query=memory_query
        )

    except Exception as e:
        print(f"Memory recall error: {e}")
        memories = []

    try:
        response = generate_response(
            user_message=user_message,
            memories=memories
        )

        return response

    except Exception as e:
        print(f"LLM error: {e}")

        return (
            "I'm having trouble processing your request right now. "
            "Please try again in a moment."
        )

def record_customer_outcome(customer_id, outcome):
    memory_text = (
        f"Customer {customer_id} confirmed this support outcome: {outcome}"
    )

    retain_memory(memory_text)