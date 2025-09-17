import streamlit as st

st.set_page_config(page_title='SCRIPTS', page_icon='🛰️')
st.title("SCRIPTS PARA CONFIGURACION")

# Diccionario de zonas
zonas = {
    'ZONA1(los_reyes_higerita)': 651000000,
    'ZONA2(Playa, Vallarta, Teocaltiche,Irapuato,Pachuca,Ixtapaluca,Aguascalientes,Villahermosa,Ensenada,Tlaxcala,Cuernavaca,Cuautla,Tijuana,Ecatepec,Tula,Minatitlan,CD_Valles,Lagos,Irapuato,Cancun,Coatzacoalcos,Merida,Mante,Campeche,Poza_rica,Zapopan,Iguala,Oaxaca, Montemorelos,Acapulco,Chilpancingo,Tampico,San_Luis_Potosi,Linares)': 219000000,
    'ZONA3(Ramos arizpe)': 393000000,
    'ZONA4(Tlalpan,Santa_fe,San_angel,Sevilla,Cento_21,24,25,Cuauhtemoc_3,Cuautitlan,Arboledas)': 159000000,
    'ZONA5(Apodaca,Cadereyta,Monterrey,Cercado,Cumbres,Escobedo,Guadalupe,Huinala,Juarez_1,2,Lincoln,Linda Vista,Monterrey,San Nicolas,Santa Barbara,Santa Catarina,Villa de Garcia,Villa de las Fuentes,Altamira,Centro_2)': 411000000,
    'ZONA6(Chapala)': 579000000,
    'ZONA7(Ciudad Guzman)': 627000000,
    'ZONA8(Manzanillo)': 711000000,
    'ZONA9(Piedras_Negras)': 549000000,
    'ZONA10(Matamoros (E6K_MTM_4, 6 y 7),Saltillo(SS-e6k1,2,3,SA-e6k1,2,3,4,5y todos los que comiencen asi))': 345000000,
    'ZONA11(CD Victoria,Reynosa,Palma_sola,Balcones)': 363000000,
    'ZONA12(Parral)': 177000000,
    'ZONA13(Chimalhuacan,Melchor_Ocampo)': 441000000,
    'ZONA14(Chihuahua)': 147000000,
    'ZONA15(Mexicali)': 513000000,
    'ZONA16(Queretaro)': 147000000,
    'ZONA17(Monclova)': 423000000,
    'ZONA18(CD Sahagun, Tizayucan)': 711000000,
    'ZONA19(Juarez_11,12,13,14,15)': 117000000,
    'ZONA20(Delicias)': 147000000,
    'ZONA21(Laredo)': 297000000
}

def script_us():
    generacion = st.selectbox('Que tipo de generacion es:', ['GEN1','GEN2'])
    cableupstream = st.text_input('Dame el cable-upstream:')
    cableupstreamrango = st.text_input('Dame el cable-upstream rango:')
    cablemac = st.text_input('Dame el cable-mac:')
    frequency = st.selectbox('Dame el frequency:', ['38200000', '34400000', '30600000', '26800000', '23000000', '19200000'])
    powerlevel = st.text_input('Dame el power-level:')
    supervision = st.text_input('Dame el supervision:')
    connector = st.text_input('Dame el connector:')
    fibernode = st.text_input('Dame el fiber-node:')
    slot = st.text_input('Slot:')
    count = st.text_input('Channel count:')
    key = st.text_input('Key:')

    if generacion == 'GEN1':
        st.text(f'configure slot {slot} channel-count {count} key {key} annex b')
    else:
        st.text(f'configure license type docsis-upstream-30-B key {key} count {count}')

    st.write('configure interface cable-upstream', cableupstream, 'cable cable-mac', cablemac)
    st.write('configure interface cable-upstream', cableupstream, 'cable ingress-cancellation interval 100')
    st.write('configure interface cable-upstream', cableupstream, 'cable frequency', frequency)
    st.write('configure interface cable-upstream', cableupstream, 'cable power-level', powerlevel)
    st.write('configure interface cable-upstream', cableupstream, 'cable supervision', supervision)
    st.write('configure interface cable-upstream', cableupstream, 'cable connector', connector)
    st.write('configure interface cable-upstream', cableupstream, 'cable channel-id 1')
    st.write('configure interface cable-upstream', cableupstream, 'cable pre-eq-enable true')
    st.write('configure interface cable-upstream', cableupstream, 'modulation-profile 64')
    st.write('configure interface cable-upstream', cableupstream, 'docsis-mode atdma')
    st.write('configure cable fiber-node', f'"{fibernode}"', 'cable-upstream', cableupstreamrango)
    st.write('configure interface cable-upstream', cableupstream, 'cable no shutdown')

def script_ds():
    generacion = st.selectbox('Que tipo de generacion es:', ['GEN1','GEN2'])
    frequencydownstream = st.selectbox('Elige la zona de la frecuencia:', list(zonas.keys()))
    frecuencia_inicial = zonas.get(frequencydownstream, 0)
    incremento = 6000000 if frecuencia_inicial else 0

    slot = st.text_input('Slot:')
    count = st.text_input('Channel count:')
    key = st.text_input('Key:')
    scriptinterfaces = st.selectbox('Cuantas interfaces quieres aumentar:', ['8_16','24', '32'])

    cabledownstream = st.text_input('Dame el cable-downstream:')
    cablemacdownstream = st.text_input('Dame la cable-mac:')
    cableupstream = st.text_input('Dame el cable-upstream:')
    supervision = st.text_input('Dame el supervision:')
    cableupstreamrango = st.text_input('Dame el cable-upstream rango:')
    fibernode = st.text_input('Dame el fiber-node:')

    if generacion == 'GEN1':
        st.text(f'configure slot {slot} channel-count {count} key {key} annex b')
    else:
        st.text(f'configure license type docsis-downstream-30-B key {key} count {count}')

    if scriptinterfaces == '8_16':
        for a in range(8):
            st.write('configure interface cable-downstream', f'{cabledownstream}/{a}', 'shutdown')
        for b in range(8):
            st.write('configure interface cable-downstream', f'{cabledownstream}/{b}', 'cable frequency 0')
        for c in range(16):
            st.write('configure interface cable-downstream', f'{cabledownstream}/{c}', 'type docsis cable-mac', cablemacdownstream)
            st.write('configure interface cable-downstream', f'{cabledownstream}/{c}', 'cable frequency', frecuencia_inicial + c * incremento)
            st.write('configure interface cable-downstream', f'{cabledownstream}/{c}', 'no shutdown')
    elif scriptinterfaces == '24':
        st.write('configure interface cable-downstream', f'{cabledownstream}', 'power-level 430')
        for a in range(24):
            st.write('configure interface cable-downstream', f'{cabledownstream}/{a}', 'type docsis cable-mac', cablemacdownstream)
            st.write('configure interface cable-downstream', f'{cabledownstream}/{a}', 'cable frequency', frecuencia_inicial + a * incremento)
            st.write('configure interface cable-downstream', f'{cabledownstream}/{a}', 'no shutdown')
    elif scriptinterfaces == '32':
        st.write('configure interface cable-downstream', f'{cabledownstream}', 'power-level 420')
        for a in range(32):
            st.write('configure interface cable-downstream', f'{cabledownstream}/{a}', 'type docsis cable-mac', cablemacdownstream)
            st.write('configure interface cable-downstream', f'{cabledownstream}/{a}', 'cable frequency', frecuencia_inicial + a * incremento)
            st.write('configure interface cable-downstream', f'{cabledownstream}/{a}', 'no shutdown')

    for b in range(4):
        st.write('configure interface cable-upstream', f'{cableupstream}/{b}', 'cable supervision', supervision)
    st.write('configure cable fiber-node', f'"{fibernode}"', 'cable-upstream', cableupstreamrango)

# Selección del tipo de script
tipo_script = st.selectbox('Tipo de configuracion', ['US', 'DS', 'OFDM','INTEGRACION'])

if tipo_script == 'US':
    script_us()
elif tipo_script == 'DS':
    script_ds()
else:
    st.write("Configuración no implementada aún para este tipo de script.")

