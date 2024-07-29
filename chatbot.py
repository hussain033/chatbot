from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature = 0.6,
    max_new_tokens = 100,
    return_full_text = False
) 
from langchain_huggingface import ChatHuggingFace
chat_llm = ChatHuggingFace(llm = llm)
chain = chat_llm | StrOutputParser()

def chat(question):
    return chain.invoke(question)
