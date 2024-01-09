from langchain_core.prompts import PromptTemplate
template = """You are a chatbot having a conversation with a human your are a {ability}.

Given the following extracted parts of a long document and a question,
create a final answer using your intelligence.

(This context can be completely irrelevant to the question if so, skip it,
focus on giving the best answer to the human question)
{context}

{chat_history}
Human: {human_input}
Chatbot:"""

PROMPT = PromptTemplate.from_template(template)