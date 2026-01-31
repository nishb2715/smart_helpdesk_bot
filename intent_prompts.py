from langchain.prompts import PromptTemplate

intent_prompt = PromptTemplate(
    input_variables=["user_query"],
    template="""
You are an intent classification system for a helpdesk chatbot.

Classify the user's query into ONE of the following categories:

- TECHNICAL_ISSUE
- INFORMATIONAL
- FOLLOW_UP
- OUT_OF_SCOPE

Rules:
- Respond with ONLY the category name.
- Do not explain.
- Do not add extra text.

User Query:
{user_query}
"""
)
