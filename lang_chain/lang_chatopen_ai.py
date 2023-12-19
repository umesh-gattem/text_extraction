import os

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma


os.environ['OPENAI_API_KEY'] = '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'

embeddings = OpenAIEmbeddings()
vectorstore = Chroma("langchain_store", embeddings)
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever())

context = "My name is Umesh Kumar. I finished my graduation in 2023 in Masters in Data Science program at" \
          " Indiana University Bloomington. I finished my undergraduation sever years earlier than graduation year. "

questions = "1. What is my name? \n 2. From which university did I graduate? \n " \
            "3. In which year I finished my undergraduate based on context?"

result = qa_chain({"query": context + questions})

print(result['result'])


