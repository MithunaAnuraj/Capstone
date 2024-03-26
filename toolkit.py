# from langchain.agents import Tool,load_tools
# from langchain.chains import RetrievalQA
# from langchain_core.pydantic_v1 import BaseModel, Field
# class DocumentInput(BaseModel):
#         question: str = Field()


def toolbox(model, context, n):
        
        from langchain.agents import Tool,load_tools
        from langchain.chains import RetrievalQA
        from langchain_core.pydantic_v1 import BaseModel, Field
        
        class DocumentInput(BaseModel):
            question: str = Field()
        
    # tools.append(
        t = Tool(
            args_schema=DocumentInput,
            name=n,
            description="useful when you want to answer questions about {}".format(n),
            func=RetrievalQA.from_chain_type(llm=model, retriever=context),
        )

        return t
    #)