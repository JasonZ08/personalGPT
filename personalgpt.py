import os
import sys
import openai
import constants 
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import sqlite3

def main():

    #OpenAI API Key Configuration
    os.environ["OPENAI_API_KEY"] = constants.APIKEY
    openai.api_key = os.getenv("OPENAI_API_KEY")

    #Input text
    query = sys.argv[1]
    colon_index = query.find(":")
    if colon_index != -1 and query[:colon_index] == "SQLITEINPUT":

        conn = sqlite3.connect("./database/calendar.db")
        cur = conn.cursor()

        try:
            statement = query[colon_index+1:].strip()
            cur.execute(statement)
        except:
            print("There is something wrong with your SQL insert statement")

        conn.commit()
        cur.close()
        conn.close()
    else:
        """

        query = sys.argv[1]
        print(query) 

        loader = DirectoryLoader("./data", glob="*.txt")
        index = VectorstoreIndexCreator().from_loaders([loader])

        print(index.query(query, llm=ChatOpenAI()))
        """
        #connect to the database
        db = SQLDatabase.from_uri("sqlite:///database/calendar.db")
        llm = ChatOpenAI()
        db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

        #run the query
        answer = db_chain.run(query)
        print(answer)

if __name__ == "__main__":
    main()