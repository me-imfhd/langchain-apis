from langchain.memory import ConversationSummaryBufferMemory

def get_memory(llm):
    return ConversationSummaryBufferMemory(
        memory_key="chat_history",
        input_key="human_input",
        output_key="AI",
        max_token_limit=100,
        llm=llm
    )
