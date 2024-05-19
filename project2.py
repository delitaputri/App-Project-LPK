import streamlit as st 

st.title('Molaritätor')

st.sidebar.header("Molaritätor")
selected = st.sidebar.selectbox('Menu:', ['Anggota Tim', 'Apa itu Molaritätor?', 'Perhitungan Molaritas Secara Tidak Langsung', 'Perhitungan Molaritas Secara Langsung'])

if selected == 'Anggota Tim': 
    with st.chat_message('user'):
        st.write('Hello 👋')

    st.title('KELOMPOK 9:')
    st.text_area(''' 
                 Hallo teman-teman,
    Perkenalkan kami dari kelas 1A yang beranggotakan 5 orang, diantaranya: 
    1. Delita Putri Dewantari (2360098)
    2. Fatma Ayu Maulida (2360125)
    3. Muhammad Iqbal Nurfajrianto (2360187)
    4. Reza Atthariq (2360237)
    5. Salwaa Dhiya Ulhaq (2360257) 
                ''')
    
    st.image('https://benzenablog.wordpress.com/wp-content/uploads/2024/05/gambar-4-edited-1.jpg?w=1024&h=576')


elif selected == 'Apa itu Molaritätor?':
    st.title('Molaritätor')
    
    st.video('https://youtu.be/fnagahljLjg?si=7lnRDekkWc75HsyN')

    st.write('''Apa sih itu Molaritätor?
    
    Molaritätor adalah web aplikasi penghitung molaritas dalam proses standardisasi. 
    Dimana Molaritätor diambil dari kata “molarität” yang berarti molaritas dan penggalan suku kata dari kalkulator.
             
Seperti yang kita tau, bahwa Molaritas adalah satuan untuk menyatakan konsentrasi larutan yang dinyatakan dalam banyaknya jumlah mol zat terlarut dalam 1 liter larutan.
Konsentrasi molaritas dapat digunakan dalam titrasi maupun standardisasi. 
Standardisasi dan titrasi, merupakan istilah penting yang digunakan dalam kimia analitik yang menggunakan standar primer.
Standardisasi merupakan proses titrasi, tetapi tidak semua titrasi merupakan proses standardisasi.
Dalam standarisasi, larutan dalam buret adalah larutan standar primer atau sekunder yang tidak diketahui konsentrasinya, 
sedangkan titrasi berisi larutan standar saja yang sudah diketahui konsentrasinya.
Untuk proses standardisasi, diperlukan larutan standar sebagai acuan. 
Dalam titrasi menggunakan dua metode, yaitu secara langsung dan tidak langsung.

Lalu apa yang dimaksud dengan metode secara langsung dan tidak langsung?
    ''')
    
    option = st.selectbox(
        'Metode Dalam Titrasi',
        ['Secara Langsung', 'Secara Tidak Langsung'],
        index=None,
        placeholder='Pilih',
    )
    if option == 'Secara Langsung':
        st.title('Titrasi Secara Langsung')
        st.write('''Titrasi langsung adalah metode yang langsung mengukur kadar suatu zat dalam sampel dengan menggunakan larutan standar yang reaksinya diketahui secara pasti.
Keuntungan dari titrasi langsung adalah kecepatan dan kemudahan penggunaannya. 
Titrasi langsung dapat dilakukan dengan berbagai metode, seperti:
    
    > Titrasi asam-basa
    > Titrasi pengendapan
    > Titrasi oksidasi-reduksi. 
''')
        st.image('https://benzenablog.wordpress.com/wp-content/uploads/2024/05/gambar-1.jpg')
        st.write('*https://youtu.be/hodj9QAzyCY?si=lQxtU1srV0Dsd5IQ*')

    elif option == 'Secara Tidak Langsung': 
        st.title('Titrasi Secara Tidak Langsung')
        st.write('''Titrasi tidak langsung adalah metode titrasi di mana reaksi kimia antara analit dan titran terjadi dalam dua atau lebih langkah yang melibatkan reaksi redoks, di mana terdapat transfer elektron antara analit dan titran.
Pada titrasi ini menggunakan faktor pengenceran atau perkalian dengan memipet sekian volume lalu diencerkan atau dilarutkan dalam labu takar pada volume tertentu.
Keuntungan dari metode ini adalah tingkat akurasi yang lebih tinggi karena melibatkan reaksi kimia yang lebih banyak.

                 Contoh umum dari titrasi tidak langsung adalah titrasi iodometri.
''')    
        st.image('https://benzenablog.wordpress.com/wp-content/uploads/2024/05/gambar-2.jpg')
        st.write('*https://youtu.be/hodj9QAzyCY?si=lQxtU1srV0Dsd5IQ*')

elif selected == 'Perhitungan Molaritas Secara Langsung':
    st.title('PERHITUNGAN MOLARITAS SECARA LANGSUNG')
    st.markdown('---')
    st.latex(r'''
    M = \left(\frac{massa}{volume \times bm}\right)
    ''')
    
    massa = st.number_input('Massa (mg):')
    st.write('Massa senyawa =', massa, 'mg')
    volume = st.number_input('Volume (mL):')
    st.write('Volume senyawa =', volume, 'mL')
    bm = st.number_input('BM (mg/mmol):')
    st.write('BM senyawa =', bm, 'mg/mmol')

    hitung_molaritas = st.button('Hitung Molaritas')
    if hitung_molaritas:
        molaritas = massa / (volume * bm)
        st.write(f'''
        M = {molaritas} mmol/mL
        ''')
        st.balloons()

elif selected == 'Perhitungan Molaritas Secara Tidak Langsung':
    st.title('PERHITUNGAN MOLARITAS SECARA TIDAK LANGSUNG')
    st.markdown('---')
    st.latex(r'''
    M = \left(\frac{massa}{fp \times volume \times bm}\right)
    ''')
    
    massa = st.number_input('Massa (mg):')
    st.write('Massa senyawa =', massa, 'mg')
    fp = st.number_input('FP:')
    st.write('FP senyawa =', fp)
    volume = st.number_input('Volume (mL):')
    st.write('Volume senyawa =', volume, 'mL')
    bm = st.number_input('BM (mg/mmol):')
    st.write('BM senyawa =', bm, 'mg/mmol')

    hitung_molaritas = st.button('Hitung Molaritas')
    if hitung_molaritas:
        molaritas = massa / (fp * volume * bm)
        st.write(f'''
        M = {molaritas} mmol/mL
        ''')
        st.balloons()
