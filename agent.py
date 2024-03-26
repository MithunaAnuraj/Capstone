def agent_ini(reper):

    from langchain.agents import AgentType, initialize_agent
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    import streamlit as st

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

    agent = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
        tools=reper,
        llm=llm,
        verbose=True,
)
    
    query = st.text_input(label="Enter query here")
    return (agent({"input":query}))

    #agent({"input": "what is cost of revenue?"})