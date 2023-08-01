import streamlit as st
from deta import Deta
from PIL import Image
import time
from streamlit_option_menu import option_menu

deta = Deta(st.secrets["db_key"])
db = deta.Drive("Marker")

def app():
    st.header("✏️ Marker", help="halaman untuk mengupload, melihat, dan mendelete gambar")
    st.divider()

    selected = option_menu(None, ["Add","Look","Delete"], 
            icons=['cloud-arrow-up',"card-image","trash"], 
            menu_icon="cast", default_index=0, orientation="horizontal")
    response = db.list()["names"]

    with st.expander("List Marker"):
        st.table({"nama" :response})
    
    if selected == 'Add':
        gambar = st.file_uploader("Masukan Marker",accept_multiple_files=True, type=['jpg','png'])
        submitGambar = st.button("Submit")

        if submitGambar:
            for i in gambar:
                db.put(i.name , data=i)
            st.success("Marker berhasil di upload")
            time.sleep(1)
            st.experimental_rerun()

    if selected == 'Look':
        hasilGambar = st.selectbox('pilih Marker', response)
        submitlist = st.button("submit")

        if submitlist:
            image = db.get(hasilGambar)
            imagedb = Image.open(image)
            st.image(imagedb, caption=hasilGambar)


    if selected == 'Delete':
        gambarBanyak = st.multiselect('pilih Marker', response)
        deleteGambar = st.button("Delete")

        if deleteGambar:
            db.delete_many(gambarBanyak)
            st.success("Marker berhasil di hapus")
            time.sleep(1)
            st.experimental_rerun()


if __name__ == "__main__":
    app()

# -- Menghilangkan Streamlit Style --
hide_st_style = """
    <style>
    footer {visibility: hidden;}
    </style>
"""

st.markdown(hide_st_style,unsafe_allow_html=True)