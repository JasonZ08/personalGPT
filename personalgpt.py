import os
import sys
import openai
import constants 
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import pickle
import sqlite3

def append_to_file(statement):
    try:
        file = open("./data/data.txt", "a")
        file.write(statement + "\n")
        file.close()
        print("Input successfully added to the file.")
    except:
        print("There was something wrong appending your message to the text file.")

def execute_sql_command(statement):

    #connect to database and execute the command
    conn = sqlite3.connect("./database/calendar.db")
    cur = conn.cursor()

    try:
        cur.execute(statement)
        print("SQL statement executed successfully.")
    except:
        print("There is something wrong with your SQL insert statement.")

    conn.commit()
    cur.close()
    conn.close()

def query_txt(query):

    #run the query taking in the personal text file
    loader = DirectoryLoader("./data", glob="*.txt")
    index = VectorstoreIndexCreator().from_loaders([loader])

    return index.query(query, llm=ChatOpenAI())

def query_db(query):

    #connect to the database
    db = SQLDatabase.from_uri("sqlite:///database/calendar.db")
    llm = ChatOpenAI()
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

    #run the query taking in the personal database
    return db_chain.run(query)

def main(): 

    #OpenAI API Key Configuration
    os.environ["OPENAI_API_KEY"] = constants.APIKEY
    openai.api_key = os.getenv("OPENAI_API_KEY")

    #Input text
    query = sys.argv[1]
    colon_index = query.find(":")
    if colon_index != -1 and query[:colon_index] == "SQLITEINPUT":

        #call the execute sql function
        execute_sql_command(query[colon_index+1:].strip())
    elif colon_index != -1 and query[:colon_index] == "TEXTINPUT":

        #open the file and append data to it
        append_to_file(query[colon_index+1:].strip())
    else:
        #get the model from the pickle file
        model_pkl_file = "database_text_question_classifier.pkl"
        with open(model_pkl_file, 'rb') as file:  
            model = pickle.load(file)
        max_length = 50

        #have the tokenizer convert the input into numeric data
        inp = [query]
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(inp)
        sequences = tokenizer.texts_to_sequences(inp)
        inp = pad_sequences(sequences, maxlen=max_length)

        #predict whether the question wants data from database vs text file
        res = model.predict(inp)

        if res[0][0] < 0.5:
            #model predicts its a database question
            answer = query_db(query)
        else:
            #model predicts its a text question
            answer = query_txt(query)

        print(answer)

        #if machine learning model predicted wrong, ask again and switch
        response = input("Did I query the wrong file? ")
        if response.lower() == "yes":
            if res[0][0] < 0.5:
                answer = query_txt(query)
            else:
                answer = query_db(query)
            print(answer)


if __name__ == "__main__":
    main()