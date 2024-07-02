from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    huggingfacehub_api_token="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",
    temperature = 0.6,
    max_new_tokens = 500,
    return_full_text = False
) 
from langchain_huggingface import ChatHuggingFace
chat_llm = ChatHuggingFace(llm = llm)
chain = chat_llm | StrOutputParser()

def chat(question):
    return chain.invoke(question)