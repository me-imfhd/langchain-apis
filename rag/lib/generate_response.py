from api.schemas.todo import GetResponse
from rag.lib.chain import custom_chain
from rag.lib.memory import get_memory
from rag.lib.llm import llm
# very imp and useful util
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

async def generate_response(body:GetResponse):
    memory = get_memory(llm=llm)
    response_data = custom_chain.invoke(
    {
        "input_documents":body.context,
        "chat_history":memory.load_memory_variables("chat_history")['chat_history'],
        "human_input": body.human_input, 
        "ability": body.ability
    }
    )   
    return response_data['text']