from operator import itemgetter
from langchain.chains import LLMChain

from rag.lib import llm
from rag.lib.prompt import PROMPT

custom_chain = (
    {
        "chat_history": itemgetter("chat_history") ,
        "ability": itemgetter("ability"),
        "human_input": itemgetter("human_input"),
        "context": itemgetter("input_documents")
    }
    # | PROMPT
    | LLMChain(
        llm=llm, 
        prompt=PROMPT,
        # verbose=True
    )
)