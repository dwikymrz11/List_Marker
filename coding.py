import streamlit as st

st.header("Dwiky Muhammad Reza")
st.subheader("2019230048")
st.divider()

def main():
    st.title("Contoh Perulangan di Streamlit")
    
    st.write("Angka dari 1 hingga 10:")
    for i in range(1, 11):
        st.write(i)
        
    st.write("Angka genap dari 1 hingga 10:")
    for i in range(2, 11, 2):  # Memulai dari 2, melompat 2 angka setiap iterasi
        st.write(i)
    
    st.write("Angka ganjil dari 1 hingga 10:")
    for i in range(1, 11, 2):  # Memulai dari 2, melompat 2 angka setiap iterasi
        st.write(i)
    
    st.divider() 
    cuaca = "hujan"
    if cuaca == "hujan":
        st.write("Hari ini hujan, Anda perlu membawa payung.")
    else:
        st.write("Hari ini tidak hujan, Anda tidak perlu membawa payung.")
    
    st.divider()
    cuaca = st.text_input("Cuaca")
    button = st.button("submit")
    if button :
        if cuaca == "Hujan":
            st.write("Hujan Hari Ini")
        else:
            st.write("Tidak Hujan")
    
    st.divider()
    # Input harga awal dan persentase diskon menggunakan st.text_input
    harga_awal = st.number_input("Harga Awal:", min_value=0)
    persentase_diskon = st.number_input("Persentase Diskon (%):", min_value=0, max_value=100)
    
    # Hitung diskon dan harga setelah diskon
    diskon = (persentase_diskon / 100) * harga_awal
    harga_setelah_diskon = harga_awal - diskon
    
    # Tampilkan hasil
    #st.write(f"Harga Awal: Rp {harga_awal:.2f}")
    #st.write(f"Diskon: Rp {diskon:.2f}")
    st.write(f"Harga Setelah Diskon: Rp {harga_setelah_diskon:.2f}")

if __name__ == "__main__":
    main()