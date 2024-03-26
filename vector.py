from toolkit import toolbox

tools = []

def vectordb(l,noun):
           
    # this function takes the paths of the files and their names as inputs 
           
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_community.vectorstores import FAISS
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langchain_text_splitters import CharacterTextSplitter
    import os
    os.environ["OPENAI_API_KEY"] = "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"


    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")


    for id,road in enumerate(l):  # l is the list with paths 
        loader = PyPDFLoader(road)
        pages = loader.load_and_split()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(pages)
        embeddings = OpenAIEmbeddings()
        retriever = FAISS.from_documents(docs, embeddings).as_retriever()
        t = toolbox(llm, retriever, noun[id])  ## function call to the function in toolkit.py
        tools.append(t)


def box():
    return tools   ## returns list of tools - currently only contains our input pdfs as tools(contexts)



