from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_OPENAI = os.getenv("OPENAI_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0,
                 openai_api_key=API_KEY_OPENAI)

template = PromptTemplate(
    input_variables=["name","question"],
    template="Greeting the user! name: {name} - Answer the following question: {question}",
)

# LCEL - Forma MODERNA y RECOMENDADA
chain = template | llm

def main():
    question = "What is the capital of France?"
    name = "Anthony"
    response = chain.invoke({"name": name, "question": question})
    print(f"Question: {question}")
    print(f"Answer: {response.content}")  # .content para obtener solo el texto
    print("Hello from initialsproj1!")

if __name__ == "__main__":
    main()