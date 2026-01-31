from intent_chain import get_intent_chain
from chains import get_helpdesk_chain

intent_chain = get_intent_chain()
helpdesk_chain = get_helpdesk_chain()

def route_query(user_query):
    intent = intent_chain.run(user_query=user_query).strip()

    if intent == "TECHNICAL_ISSUE":
        return helpdesk_chain.run(user_query=user_query)

    elif intent == "FOLLOW_UP":
        return helpdesk_chain.run(user_query=user_query)

    elif intent == "INFORMATIONAL":
        return helpdesk_chain.run(user_query=user_query)

    elif intent == "OUT_OF_SCOPE":
        return (
            "I’m designed to help with technical helpdesk-related issues.\n\n"
            "Could you please describe a technical problem or question you need help with?"
        )

    else:
        return (
            "I’m not fully sure I understood your request.\n\n"
            "Could you please rephrase or provide more details?"
        )
