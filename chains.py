from langchain.chains import LLMChain
from config import get_llm
from prompts import helpdesk_prompt
from memory import get_memory

def get_helpdesk_chain():
    llm = get_llm()
    memory = get_memory()

    chain = LLMChain(
        llm=llm,
        prompt=helpdesk_prompt,
        memory=memory,
        verbose=False
    )

    return chain
