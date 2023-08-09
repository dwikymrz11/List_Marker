import streamlit as st
from deta import Deta
from PIL import Image
import time
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth

deta = Deta(st.secrets["db_key"])
db = deta.Drive("Marker")
dbs = deta.Base("admin")

def insert_user(username,name,password):
    try:
        dbs.put({"key": username, "name": name, "password": password})
        return st.success("Berhasil Registrasi")
    except:
        return st.warning("username telah dipakai") 

def fetch_all_users():
    res = dbs.fetch()
    return res.items

def app():
    
    
    
        users = fetch_all_users()
        usernames = [user["key"] for user in users]
        names = [users["name"] for users in users]
        passwords = [user["password"] for user in users]

        credentials = {"usernames":{}}

        for un, name, pw in zip(usernames, names, passwords):
            user_dict = {"name":name,"password":pw}
            credentials["usernames"].update({un:user_dict})

        authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)
    

        authenticator._check_cookie()
        if not st.session_state['authentication_status']:
            selection = option_menu(None, ["Login","Register"], 
                icons=['door-open-fill',"person-add"], 
                menu_icon="cast", default_index=0, orientation="horizontal")
            if selection == "Login":
                name_user, authenticator_status, username = authenticator.login("Login", "main")

                if authenticator_status == False:
                    st.error("Username/Passwordnya salah")

                if authenticator_status == None:
                    st.warning("Tolong masukan username dan passsword anda")   
            if selection == "Register":
                with st.form("Add Account"):
                    inputUser = st.text_input("Masukan Username")
                    inputName = st.text_input("Masukan Nama")
                    inputPassword = st.text_input("Masukan Password", type="password")
                    hashed_passwords = stauth.Hasher([inputPassword]).generate()
                    hashed_password = hashed_passwords[0]
                    buttonS = st.form_submit_button("Register")
                    if buttonS:
                        insert_user(inputUser,inputName,hashed_password)
                        time.sleep(1)
                        st.experimental_rerun()   

        else:      
            selection = None
            st.header("✏️ Marker", help="halaman untuk mengupload, melihat, dan mendelete marker")
            st.divider()

            selected = option_menu(None, ["Tambahkan","Lihat","Hapus"], 
                    icons=['cloud-arrow-up',"card-image","trash"], 
                    menu_icon="cast", default_index=0, orientation="horizontal")
            response = db.list()["names"]

            with st.expander("List Marker"):
                st.table({"nama" :response})
            
            if selected == 'Tambahkan':
                gambar = st.file_uploader("Masukkan Marker",accept_multiple_files=True, type=['jpg','png'])
                submitGambar = st.button("Masukkan")
                authenticator.logout("Logout", "main")
                if submitGambar:
                    for i in gambar:
                        db.put(i.name , data=i)
                    st.success("Marker berhasil di upload")
                    time.sleep(1)
                    st.experimental_rerun()

            if selected == 'Lihat':
                hasilGambar = st.selectbox('Pilih Marker', response)
                submitlist = st.button("Lihat")
                authenticator.logout("Logout", "main")
                if submitlist:
                    image = db.get(hasilGambar)
                    imagedb = Image.open(image)
                    st.image(imagedb, caption=hasilGambar)


            if selected == 'Hapus':
                gambarBanyak = st.multiselect('Pilih Marker', response)
                deleteGambar = st.button("Delete")
                authenticator.logout("Logout", "main")
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