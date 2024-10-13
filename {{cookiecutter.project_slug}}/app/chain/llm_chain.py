from langchain.chains.llm import LLMChain
from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate

from config import OPENAI_API_KEY


def generate_answer(question: str) -> str:
    llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo-instruct", openai_api_key=OPENAI_API_KEY)
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        You re a helpful and concise assistant.
        Your task is to answer questions clearly and directly based on the given content.
        Answer the following question: {question}

        If you feel like you don't have enough information to answer that question, say "I don't know".
        Your answers should be detailed.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"question": question})

    return result.replace("\n", "")
