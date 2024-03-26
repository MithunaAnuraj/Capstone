import streamlit as st
from io import BytesIO
import os



def justnames(docs):
    names = []
    for d in docs:
        u = d.name.split('.')[0]
        names.append(u)
    return names    ## retrieving names and storing them in a file for future use


def frontend():

    paths = []
    files = st.file_uploader(label="Upload your pdfs here", accept_multiple_files=True)  # user uploads files here 
    names = justnames(files) # we send our input files of bytesIO type to this function to just retrieve their names
    for f in files:
        n = f.name.split('.')[0]
        f.seek(0)
        with open("{}.pdf".format(n), mode="wb") as doc:
            doc.write(f.read())
            paths.append(os.path.abspath("{}.pdf".format(n)))

    return paths, names


    

