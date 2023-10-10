import os
import sys
import openai

import constants 
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = constants.APIKEY
openai.api_key = os.getenv("OPENAI_API_KEY")

query = sys.argv[1]
print(query) 

loader = DirectoryLoader("./data", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query, llm=ChatOpenAI()))