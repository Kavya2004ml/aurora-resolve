import streamlit as st

from core import handle_customer_message, record_customer_outcome


st.set_page_config(
    page_title="Aurora Resolve",
    page_icon="✨"
)

st.title("✨ Aurora Resolve")
st.caption("Memory-powered customer support")


# Customer ID
customer_id = st.text_input(
    "Customer ID",
    placeholder="e.g. PRIYA001"
)


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_issue" not in st.session_state:
    st.session_state.last_issue = None


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Customer message
prompt = st.chat_input("How can I help you?")


if prompt:

    if not customer_id.strip():
        st.warning("Please enter your Customer ID first.")

    else:
        # Save current issue
        st.session_state.last_issue = prompt

        # Display and save customer message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.write(prompt)

        # Get response from backend
        with st.chat_message("assistant"):
            with st.spinner("Checking previous support history..."):

                response = handle_customer_message(
                    customer_id=customer_id.strip(),
                    user_message=prompt
                )

            st.write(response)

        # Save assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })


# Outcome confirmation
if customer_id.strip() and st.session_state.last_issue:

    st.divider()
    st.subheader("Did the solution work?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Yes, it worked"):
            outcome = (
                f"For issue '{st.session_state.last_issue}', "
                "the customer confirmed that the suggested solution worked."
            )

            record_customer_outcome(
                customer_id=customer_id.strip(),
                outcome=outcome
            )

            st.success("Outcome saved to memory.")

    with col2:
        if st.button("❌ No, it didn't work"):
            outcome = (
                f"For issue '{st.session_state.last_issue}', "
                "the customer confirmed that the suggested solution did not work."
            )

            record_customer_outcome(
                customer_id=customer_id.strip(),
                outcome=outcome
            )

            st.info("Failed outcome saved to memory.")