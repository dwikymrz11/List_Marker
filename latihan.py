import streamlit as st
import pandas as pd
from deta import Deta

deta = Deta(st.secrets["db_key"])
db = deta.Base("data")

def insert_user(nim,name,jurusan):
    try:
        db.put({"key": nim, "name": name, "jurusan": jurusan})
        return st.success("Berhasil")
    except:
        return st.warning("gagal") 


def admin_upload():
    nim = st.text_input("NIM")
    nama = st.text_input("NAMA")
    jurusan = st.selectbox("jurusan",['IT','SI'])

    submit = st.button("submit")
    if submit:
        insert_user(nim,nama,jurusan)
    

if __name__ == "__main__":
    admin_upload()