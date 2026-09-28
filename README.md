# Aurora Resolve

Aurora Resolve is a memory-powered customer support assistant built with Hindsight.

Instead of treating every support conversation as a new interaction, Aurora Resolve remembers previous customer issues, failed troubleshooting attempts, and successful resolutions.

## Problem

Traditional support assistants are often stateless.

When customers return with the same issue, they may need to repeat their history and retry troubleshooting steps that already failed.

## Solution

Aurora Resolve uses persistent memory to remember customer-specific support history.

It can:

- Recall previous customer issues
- Remember failed troubleshooting attempts
- Remember successful resolutions
- Use relevant past outcomes in future conversations
- Store newly confirmed customer outcomes

## How It Works

1. Customer sends a support message
2. Aurora Resolve recalls relevant customer memory from Hindsight
3. The retrieved memory is passed to the LLM
4. The LLM generates a context-aware response
5. Confirmed support outcomes are stored back in Hindsight

## Architecture

Customer
↓
Streamlit UI
↓
Python backend
↓
Hindsight + Groq

## Tech Stack

- Python
- Streamlit
- Hindsight
- Groq
- openai/gpt-oss-120b

## Demo Scenario

A customer named PRIYA001 previously experienced a subscription payment failure.

- Restarting the app did not work
- Clearing the payment session resolved the issue

When Priya later reports:

> "My payment issue is happening again."

Aurora Resolve recalls the previous outcome and recommends the solution that worked before instead of repeating the failed troubleshooting step.

After the customer confirms that the solution worked again, Aurora Resolve stores the new verified outcome for future interactions.