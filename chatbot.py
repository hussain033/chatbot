from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token="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",
    temperature = 0.6,
    max_new_tokens = 200,
    return_full_text = False
) 
from langchain_huggingface import ChatHuggingFace
chat_llm = ChatHuggingFace(llm = llm)
chain = chat_with_limit | StrOutputParser()

def chat_with_limit(prompt):
  return chat_llm.invoke(prompt, max_tokens = 300, stop = None)

def chat(question):
    return chain.invoke(question)
