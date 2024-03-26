import streamlit as st
from front import frontend
from front import justnames
paths, names = frontend()

from vector import vectordb
from toolkit import toolbox
vectordb(paths, names)

from vector import box
y = box()  
from tbox import repl
tools = repl(y)

from agent import agent_ini
answer = agent_ini(tools)
st.text("{}".format(answer))

