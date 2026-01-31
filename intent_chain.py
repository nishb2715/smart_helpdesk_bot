from langchain.chains import LLMChain
from config import get_llm
from intent_prompts import intent_prompt

def get_intent_chain():
    llm = get_llm()
    llm.temperature = 0.0  

    return LLMChain(
        llm=llm,
        prompt=intent_prompt,
        verbose=False
    )
