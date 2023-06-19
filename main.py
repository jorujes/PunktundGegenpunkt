import streamlit as st
import string

# Configurar o layout da página
st.set_page_config(page_title="PunktundGegenpunkt", layout="wide")

# Reduzir o espaço vazio no topo da página
st.write("")

def get_author_text(author_name):
    text_file_map = {
        'Eça de Queirós - O Crime do Padre Amaro': 'amaro.txt',
        'Eça de Queirós - O Primo Basílio': 'primo.txt',
        'Eça de Queirós - Os Maias': 'maias.txt',
        'Machado de Assis - Dom Casmurro': 'dom.txt',
        'Machado de Assis - Memórias Póstumas de Brás Cubas': 'memorias.txt',
        'Machado de Assis - Memorial de Aires': 'memorial.txt',
        'António Lobo Antunes - Memória de Elefante': 'memoria.txt',
        'António Lobo Antunes - Que Cavalos São Aqueles Que Fazem Sombra no Mar?': 'cavalos.txt',
        'António Lobo Antunes - Explicação dos Pássaros': 'passaros.txt',
        'João Guimarães Rosa - Grande Sertão: Veredas': 'sertao.txt',
        'João Guimarães Rosa - Sagarana': 'sagarana.txt',
        'João Guimarães Rosa - Manuelzão e Miguilim': 'manuelzao.txt',
        'Ernest Hemingway - The Old Man and The Sea': 'sea.txt',
        'Ernest Hemingway - The Sun Also Rises': 'sun.txt',
        'Ernest Hemingway - For Whom the Bell Tolls': 'bell.txt',
        'Herman Melville - Moby Dick': 'moby.txt',
        'Herman Melville - Bartleby, Benito Cereno and Other Stories': 'billy.txt',
    }
    text_file = text_file_map[author_name]
    with open(text_file, 'r') as f:
        text = f.read()
        return text

def get_punctuation(text):
    punctuation = ""
    for character in text:   
        if character in string.punctuation:      
            punctuation += character    
    return punctuation

st.markdown("<h2 style='text-align: center;'>PunktundGegenpunkt</h2>", unsafe_allow_html=True)

authors_list = ['Eça de Queirós - O Crime do Padre Amaro', 'Eça de Queirós - O Primo Basílio', 'Eça de Queirós - Os Maias', 'Machado de Assis - Dom Casmurro', 'Machado de Assis - Memórias Póstumas de Brás Cubas', 'Machado de Assis - Memorial de Aires', 'António Lobo Antunes - Memória de Elefante', 'António Lobo Antunes - Que Cavalos São Aqueles Que Fazem Sombra no Mar?', 'António Lobo Antunes - Explicação dos Pássaros', 'João Guimarães Rosa - Grande Sertão: Veredas', 'João Guimarães Rosa - Sagarana', 'João Guimarães Rosa - Manuelzão e Miguilim', 'Ernest Hemingway - The Old Man and The Sea', 'Ernest Hemingway - The Sun Also Rises', 'Ernest Hemingway - For Whom the Bell Tolls', 'Herman Melville - Moby Dick', 'Herman Melville - Bartleby, Benito Cereno and Other Stories']

author_select1, author_select2 = st.columns(2)

with author_select1:
    author1 = st.selectbox('', authors_list, key='author1')
    author1_text = get_author_text(author1)
    author1_punctuation = get_punctuation(author1_text)
    st.text_area("", author1_punctuation, height=600, key='text_area1')

with author_select2:
    author2 = st.selectbox('', authors_list, key='author2')
    author2_text = get_author_text(author2)
    author2_punctuation = get_punctuation(author2_text)
    st.text_area("", author2_punctuation, height=600, key='text_area2')
