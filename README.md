# Aurora Resolve

Aurora Resolve is a memory-powered customer support assistant built with Hindsight.

Instead of treating every support conversation as a new interaction, Aurora Resolve remembers previous customer issues, failed troubleshooting attempts, successful resolutions, and newly confirmed outcomes.

This allows returning customers to continue from past support history instead of starting from zero.

## Problem

Traditional customer support assistants are often stateless.

When customers return with the same issue, they may need to:

- Repeat their previous problem
- Retry troubleshooting steps that already failed
- Re-explain what worked before
- Start the support process from the beginning

This creates unnecessary friction for both customers and support teams.

## Solution

Aurora Resolve uses persistent memory to maintain customer-specific support history.

It can:

- Recall previous customer issues
- Remember failed troubleshooting attempts
- Remember successful resolutions
- Use relevant past outcomes in future conversations
- Avoid unnecessarily repeating known failed fixes
- Store newly confirmed customer outcomes
- Keep support history separated by customer

## How Hindsight Is Used

Hindsight provides the persistent memory layer for Aurora Resolve.

For every customer interaction:

1. Aurora Resolve receives the customer ID and current support message.
2. Relevant support history is recalled from Hindsight.
3. Retrieved memories are filtered to the current customer.
4. The current message and relevant memories are passed to the LLM.
5. The LLM generates a context-aware support response.
6. When the customer confirms whether a suggested solution worked, the verified outcome is stored back in Hindsight.
7. That outcome can be recalled during future interactions.

This creates a continuous learning loop:

**Recall → Respond → Confirm Outcome → Retain → Recall Again**

## Architecture

```text
Customer
   ↓
Streamlit UI
   ↓
Python Backend
   ↓
 ┌───────────────┬───────────────┐
 │               │               │
Hindsight        Groq LLM
Memory           Response Generation
```

## Tech Stack

- Python
- Streamlit
- Hindsight
- Groq
- openai/gpt-oss-120b
- python-dotenv

## Project Structure

```text
aurora-resolve/
│
├── app.py
├── core.py
├── memory.py
├── llm.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── seed_memory.py
├── seed_arjun.py
├── test_core.py
└── test_outcome.py
```

## Main Files

### `app.py`

Streamlit frontend for the customer support chat experience.

It allows a customer to:

- Enter a customer ID
- Send a support message
- Receive a memory-aware response
- Confirm whether the suggested solution worked

### `core.py`

Coordinates the main application flow.

It connects:

- Hindsight memory recall
- LLM response generation
- Confirmed outcome retention

### `memory.py`

Contains the Hindsight memory integration.

It is responsible for:

- Storing support outcomes
- Recalling relevant support history
- Filtering recalled memories by customer ID

### `llm.py`

Contains the Groq LLM integration.

The prompt is designed to:

- Use relevant customer memory
- Avoid inventing memories
- Avoid repeating troubleshooting steps that already failed
- Prefer previously successful solutions
- Avoid claiming unsupported external capabilities
- Avoid inventing product-specific instructions when they are unknown

## Demo Scenario

The main demo uses a returning customer:

```text
PRIYA001
```

Priya previously experienced a subscription payment failure.

Her previous support history is:

- Restarting the app did not resolve the issue
- Clearing the payment session resolved the issue

Later, Priya returns and says:

> My payment issue is happening again.

Aurora Resolve recalls the previous support history.

Instead of starting from zero or repeating the failed restart step, it recognizes that clearing the payment session previously worked and uses that information in the response.

If Priya confirms that the solution worked again, Aurora Resolve stores the newly verified outcome in Hindsight for future interactions.

## Additional Test Scenarios

### Returning Customer — ARJUN002

Previous support history:

- Arjun experienced a login issue
- Resetting the password did not resolve it
- Unlocking the account resolved the issue

Aurora Resolve recalls the successful and failed outcomes from the previous interaction and uses them in the current response.

### New Customer

A customer with no previous support history receives a normal first-time support response.

Aurora Resolve does not use another customer's memory for the new customer.

## Memory Safety

Aurora Resolve does not automatically store every AI-generated response as trusted memory.

Instead, verified customer outcomes are stored after the customer confirms whether a solution worked.

This helps prevent model-generated assumptions from being treated as historical facts.

The application also filters recalled memories by customer ID to reduce cross-customer memory leakage.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Kavya2004ml/aurora-resolve.git
cd aurora-resolve
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root.

Use `.env.example` as a reference:

```env
GROQ_API_KEY=your_groq_api_key_here
HINDSIGHT_API_KEY=your_hindsight_api_key_here
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
HINDSIGHT_BANK_ID=your_hindsight_bank_id
```

Do not commit your real `.env` file or API keys to GitHub.

### 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## Live Demo

**Aurora Resolve:**  
https://aurora-resolve-jy4hnhcq9c2qzbbb5p5mtu.streamlit.app/

## GitHub Repository

https://github.com/Kavya2004ml/aurora-resolve

## Core Learning Loop

```text
Customer Message
      ↓
Recall Relevant Memory
      ↓
Generate Context-Aware Response
      ↓
Customer Confirms Outcome
      ↓
Store Verified Outcome
      ↓
Use It In Future Interactions
```

## Future Improvements

Possible future improvements include:

- CRM integration
- Support ticket integration
- Knowledge-base integration
- Richer customer profiles
- Analytics for recurring support issues
- Human support handoff
- Structured memory metadata
- More advanced memory ranking and retrieval

## Team

Aurora Resolve was built as a focused MVP to demonstrate how persistent memory can improve customer support continuity.

The project focuses on one simple idea:

**Remember what happened before, use it now, and learn from the new outcome.**
