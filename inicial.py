# encoding: iso-8859-1
import funcoes as fun 
from sklearn.feature_extraction.text import TfidfVectorizer
import pprint 
import emoji
import re
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
pd.set_option('display.max_columns', None)
import time
from PIL import Image


# Tokenizador que reconhece emojis como tokens separados
def tokenizer_emoji_aware(text):
    text = fun.separar_emojis(text)
    return text.split()

#Fun��o pra limpar o que o usu�rio digitou da primeira vez
def clear_text():
    st.session_state["texto"] = '' 
    alert.empty()

# Menu lateral colorido
with st.sidebar:
    selected = option_menu(
        menu_title="Op��es",
        options=["Home", "Aplica��o", "Recursos", "Contatos", "Refer�ncias", "M�tricas"],
        icons=["house-heart-fill", "code-slash", "folder-fill", "person-lines-fill", "bookmark-heart", "file-bar-graph"],
        default_index=0,
        styles={
            "container": {"background-color": "black"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "5px"},
            "nav-link-selected": {"background-color": "#FF1493", "color": "white"},
        }
    )

#Isso aqui mostra o menu com as op��es #outro modelo de menu
#selected = option_menu(
#    menu_title=None,
#    options = ["Home_page", "Aplica��o", "Recursos","Contatos","Refer�ncias","M�tricas"],
#    icons = ["house-heart-fill","code-slash","folder-fill","person-lines-fill","bookmark-heart","bookmark-heart"],
#    default_index=0,
#   orientation="horizontal",
#   )

#Cada if � o conte�do de um menu 
if selected =="Refer�ncias":
    st.title("Refer�ncias")
    st.markdown(""" 
    
    * <p style="text-align:justify; font-size: 18px;"> <i>Text Mining for Cyberbullying Detection: a Brazilian Portuguese Evaluation</i> (2021) - Autores: Carolina Eberhart, Luciano Ignaczak, M�rcio Garcia Martins - <a href="https://sol.sbc.org.br/index.php/stil/article/view/17788"> Acesse aqui </a></p>
    
    * <p style="text-align:justify; font-size: 18px;"><i>Cyberbullying Detection in Social Networks: A Comparison Between Machine Learning and Transfer Learning Approaches </i> (2023)- </i> Autores: Teoh Wai Teng and Kasturi Dewi Varathan - <a href="https://ieeexplore.ieee.org/document/10122521"> Acesse aqui </a></p>
   
    
    """ , unsafe_allow_html=True)
    


if selected == "Home":
    st.title("Detec��o de cyberbullying em Portugu�s Brasileiro  &#127463;&#127479; &#128187;")

    
    st.markdown("""   
    
    <p style="text-align:justify; font-size: 18px;">Esta aplica��o tem como objetivo auxiliar na amplia��o dos estudos em <strong>detec��o autom�tica de mensagens com potencial de <i>cyberbullying</i></strong> em portugu�s brasileiro investigando o uso de t�cnicas de <strong> aprendizado de m�quina <i>(machine learning)</i></strong>. </p>

    <p style="text-align:justify ; font-size: 18px;">A aplica��o � um prot�tipo, isto �, uma pequena amostra como parte de uma <strong>pesquisa de Doutorado</strong> em Inform�tica que investiga a exposi��o de crian�as e adolescentes a amea�as nos ambientes digitais e prop�e o uso de Intelig�ncia Artificial para detect�-las e mitig�-las. 
    
      
    """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Como funciona? &#128289; </font></h1> """, unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify; font-size: 18px;"> Ao digitar uma frase e envi�-la para an�lise, o sistema verifica se ela tem <strong>caracter�sticas similares a mensagens de <i>cyberbullying</i></strong> , 
    com base em modelos treinados com dados reais. </p> """, unsafe_allow_html=True)


    st.caption("""<h2><font color="ff1493"> SVM x Naive Bayes &#128202; </font></h1>""", unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify; font-size: 18px;"> 
    Nesta aplica��o, utilizamos dois algoritmos de aprendizado de m�quina: <i>Naive Bayes</i> e SVM <i>(Support vector machine)</i>. 
    Ambos s�o capazes de aprender com exemplos previamente classificados para identificar se uma frase pode ser considerada <i>cyberbullying</i> ou n�o, 
    mas adotam abordagens diferentes. </p>


    <p style="text-align:justify; font-size: 18px;"> O SVM considera o padr�o geral da frase, buscando separar frases ofensivas e n�o ofensivas com base em limites definidos 
    durante o treinamento. J�, o Naive Bayes se baseia na frequ�ncia das palavras e estima a probabilidade de uma frase ser ofensiva  
    ou n�o com base nas palavras que ela cont�m. </p>

    <p style="text-align:justify; font-size: 18px;"> Em frases curtas com termos mais agressivos, ambos os algoritmos costumam concordar. Em frases mais sutis ou com ironia, o SVM pode 
    oferecer uma an�lise um pouco mais precisa. </p> """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Como usar? &#128220</font></h1>""", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:justify; font-size: 18px;"> Acesse a aba <strong>App</strong>, digite uma frase no campo indicado e selecione o modelo de classifica��o desejado. Clique no bot�o "Analisar".
    A resposta ser� exibida em poucos segundos.</p>

    <p style="text-align:justify; font-size: 18px;"> Mais informa��es sobre o conjunto de dados utilizado na etapa de treinamento do modelo est�o dispon�veis no menu <strong>Recursos</strong>. </p> """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Importante </font>   <font color="ffd700"> &#9888;</font>   </h1>""", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:justify; font-size: 18px;"> Esta ferramenta � apenas um <strong>suporte � detec��o</strong>. A determina��o de um caso de cyberbullying envolve outros fatores importantes,
     como <strong>contexto</strong>, <strong>recorr�ncia</strong> e <strong>inten��o</strong>. A an�lise autom�tica n�o substitui a 
     avalia��o humana.</p> """, unsafe_allow_html=True)
               
    st.caption("""<h2><font color="ff1493">Trabalhos futuros &#128679; </font></h2>""", unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify; font-size: 18px;"> Em vers�es futuras, a aplica��o dever� ser aprimorada e adaptada para funcionar como uma <strong>extens�o
     de navegador</strong> e/ou um <strong>aplicativo</strong>, permitindo a detec��o em tempo real e envio de notifica��es aos usu�rios 
     incentivando a reflex�o antes de publicar mensagens ofensivas. Al�m disso, o <i>dataset</i> tamb�m deve ser aprimorado para incluir exemplos mais diversos e representativos,
     incluindo textos advindos de outras plataformas. </p> """, unsafe_allow_html=True)

if selected == "M�tricas":

    st.caption("""<h2><font color="ff1493"> M�tricas do modelo treinado com Naive Bayes </font></h1>""", unsafe_allow_html=True)
    
    spamreader = fun.ler("rel_class_nb.txt")
    
    for row in spamreader:

        st.markdown(row)
    
    spamreader = fun.ler("rel_class_svm.txt")
    
    st.caption("""<h2><font color="ff1493"> M�tricas do modelo treinado com SVM </font></h1>""", unsafe_allow_html=True)
    

    for row in spamreader:
        st.markdown(row)


if selected == "Recursos":
    st.title("Recursos")
    st.markdown(""" 
                
                
                ***C�digo fonte***
                >  https://github.com/raquelmachado4993/cyberbullying-br 
                ---
                ***Dataset***
                > Aqui est� o[link](vou colocar) para o Kaggle
                ---
    """)
    
if selected =="Contatos":
    st.title("Contatos dos pesquisadores")
    st.markdown("""
                
                
                #### Professora Ma. Raquel M. M. Fernandes
                ##### ***Doutoranda em Inform�tica, Programa de P�s-Gradua��o em Inform�tica (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                Email: raquel.fernandes@ufrj.br
                               
                ---
                #### Professor Dr. Luiz Fernando Rust da Costa Carmo
                ##### ***Programa de P�s-Gradua��o em Inform�tica (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                Email: rust@nce.ufrj.br
         
                ---

                #### Professora Dra. Claudia Lage Rebello da Motta
                ##### ***Programa de P�s-Gradua��o em Inform�tica (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                Email: claudiam@nce.ufrj.br
         
                ---
                
                """)

    
 
if selected == "Aplica��o":  

      
# Disponibilizei o resultado do treinamento com SVM e NB, o usu�rio pode escolher aqui 

  
   
    tipo = st.radio(
        "Selecione o algoritmo de aprendizado supervisionado:",
        ["SVM", "NB"],
        captions=[
            "Support vector machine",
            "Naive bayes",
        ],
    )

    
    
    # CSS para bot�es rosa
    st.markdown("""
    <style>
        .stButton > button {
            background-color: #FF1493;
            color: white;
            border: none;
            padding: 0.6em 1.2em;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease;
            outline: none;
        }
        .stButton > button:hover {
            background-color: #e01382;
            color: white;
        }

        .stButton > button:focus,
        .stButton > button:active {
            background-color: #FF1493 !important;
            color: white !important;
            box-shadow: none !important;
            outline: none !important;
        }
    </style>
""", unsafe_allow_html=True)


 

# Pegando a frase que o usu�rio vai digitar para analisar..
    input_text = st.text_input('Digite uma frase para an�lise:', key="texto")

    
    #button = st.button("Analisar")
    #st.button("Limpar", on_click=clear_text)

    spacer1, col1, col2, spacer2 = st.columns([1, 3, 3, 1])

    
    with col1:
        button = st.button("Analisar")

    with col2:
        st.button("Limpar", on_click=clear_text)

    if input_text and button:

        #Lendo o input
        input_data = {
                       "text" : [input_text] 
                  }

    

    #Dependendo da escolha, vai chamar uma fun��o ou outra

        with st.spinner("Analisando..."):
            
            if tipo == "SVM":
                # Carregando o modelo e o vetor
                modelo = fun.carregarmodelo('finalized_svm_model.joblib')
                vectorizer = fun.carregarmodelo('finalized_svm_vectorizer.joblib')
                
                # Mostra a resposta da an�lise aqui 
                resp, flag = fun.classificar_frase_svm(modelo,vectorizer,input_text)
                if(flag):
                    alert =st.warning(resp)
                else:
                    alert =st.success(resp)
                

            elif tipo == "NB":
                # Carregando o modelo e o vetor
                modelo_nb = fun.carregarmodelo('finalized_nb_model.joblib')
                vectorizer_nb = fun.carregarmodelo('finalized_nb_vectorizer.joblib')
                
                # Mostra a resposta da an�lise aqui 
                resp, flag = fun.classificar_frase_nb(modelo_nb,vectorizer_nb,input_text)
                if(flag):
                    alert =st.warning(resp)
                else:
                    alert =st.success(resp)

            
            else:
                st.success("nada selecionado")
            
    st.markdown("""
    <style>
    .disclaimer-box {
        background-color: #fff0f5; /* rosa clarinho */
        border-left: 6px solid #FF1493; /* borda rosa forte � esquerda */
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 2px 2px 8px rgba(255, 20, 147, 0.2);
        font-style: italic;
        color: #333333;
        text-align: justify;
        margin-bottom: 20px;
    }
    </style>
    <div class="disclaimer-box">
        <strong>Disclaimer:</strong><br>
        As informa��es contidas neste formul�rio t�m car�ter exclusivamente acad�mico e s�o destinadas a fins de pesquisa.
        N�o constituem aconselhamento jur�dico e s�o fornecidas como prot�tipo, sem garantias de exatid�o, completude ou atualidade.
        Os autores n�o se responsabilizam por eventuais erros ou omiss�es.
    </div>
""", unsafe_allow_html=True)    

            
