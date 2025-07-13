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

#Isso aqui mostra o menu com as op��es
selected = option_menu(
    menu_title=None,
    options = ["Home", "App", "Recursos","Contatos","Ref"],
    icons = ["house-heart-fill","code-slash","folder-fill","person-lines-fill","bookmark-heart"],
    default_index=0,
    orientation="horizontal",
    )

#Cada if � o conte�do de um menu 
if selected =="Ref":
    st.title("Pagina de refer�ncias")
    st.markdown(""" Vou colocar refer�ncias aqui nessa p�gina. """)



if selected == "Home":
    st.title("Detec��o de cyberbullying em Portugu�s Brasileiro &#128187;")

    
    st.markdown("""   
    
    <p style="text-align:justify">Esta aplica��o tem como objetivo auxiliar na <strong>detec��o autom�tica de mensagens com potencial de cyberbullying</strong> em portugu�s brasileiro, utilizando <strong>t�cnicas de aprendizado de m�quina (machine learning)</strong>. Voc� pode analisar frases com dois classificadores diferentes: <strong>SVM (Support Vector Machine)</strong> e <strong>Naive Bayes</strong>.</p>

    <p style="text-align:justify">Ela foi desenvolvida como parte de uma <strong>tese de doutorado</strong> que investiga a exposi��o de crian�as e adolescentes a amea�as nos ambientes digitais. A pesquisa busca apoiar o trabalho pedag�gico em conformidade com a <strong>BNCC</strong> (Base Nacional Comum Curricular), a <strong>PNED</strong> (Pol�tica Nacional de Educa��o Digital) e a <strong>E-Ciber</strong> (Estrat�gia Nacional de Seguran�a Cibern�tica).</p>

    <p style="text-align:justify">A hip�tese central considera que uma <strong>taxonomia organizada de amea�as digitais</strong> pode facilitar sua identifica��o e servir como ferramenta pr�tica em Computa��o e Educa��o. Como parte dessa investiga��o, esta aplica��o foi criada para testar o uso de <strong>Intelig�ncia Artificial</strong> como suporte � detec��o de mensagens ofensivas.</p>
    """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Como funciona? &#128289; </font></h1> """, unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify"> Voc� digita uma frase, e o sistema verifica se ela tem <strong>caracter�sticas similares a mensagens de cyberbullying</strong> , 
    com base em modelos treinados com dados reais. Para isso, usamos aprendizado de m�quina, uma t�cnica que permite que o sistema aprenda 
    com exemplos e identifique padr�es automaticamente. </p> """, unsafe_allow_html=True)


    st.caption("""<h2><font color="ff1493"> SVM x Naive Bayes &#128202; </font></h1>""", unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify"> 
    Nesta aplica��o, utilizamos dois algoritmos de aprendizado de m�quina: Naive Bayes e SVM (Support vector machine). 
    Ambos s�o capazes de aprender com exemplos previamente classificados para identificar se uma frase pode ser considerada cyberbullying, 
    mas adotam abordagens diferentes.

    O SVM considera o padr�o geral da frase como um todo, buscando separar frases ofensivas e n�o ofensivas com base em limites definidos 
    durante o treinamento. J�, o Naive Bayes se baseia na frequ�ncia das palavras, estimando a probabilidade de uma frase ser ofensiva  
    ou n�o com base nas palavras que ela cont�m.

    Em frases curtas com termos mais agressivos, ambos os algoritmos costumam concordar. Em frases mais sutis ou com ironia, o SVM pode 
    oferecer uma an�lise um pouco mais precisa j� que considera mais o contexto. </p> """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Como usar? &#128220</font></h1>""", unsafe_allow_html=True)
    st.markdown("""
    <p>Acesse a aba <strong>App</strong>, digite uma frase no campo indicado e selecione o modelo de classifica��o desejado. 
    A resposta ser� exibida em poucos segundos.</p>

    <p>Mais informa��es sobre o conjunto de dados utilizado est�o dispon�veis no menu <strong>Recursos</strong>. </p> """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Importante </font>   <font color="ffd700"> &#9888;</font>   </h1>""", unsafe_allow_html=True)
    st.markdown("""
    Esta ferramenta � apenas um <strong>suporte � detec��o</strong>. A determina��o de um caso de cyberbullying envolve outros fatores importantes,
     como <strong>contexto</strong>, <strong>recorr�ncia</strong> e <strong>inten��o</strong>. A an�lise autom�tica n�o substitui a 
     avalia��o humana.</p> </p> """, unsafe_allow_html=True)
               
    st.caption("""<h2><font color="ff1493">Trabalhos futuros &#128679; </font></h1>""", unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify"> Em vers�es futuras, a aplica��o dever� ser aprimorada e adaptada para funcionar como uma <strong>extens�o
     de navegador</strong> ou um <strong>aplicativo m�vel</strong>, permitindo a detec��o em tempo real e envio de notifica��es aos usu�rios 
     incentivando a reflex�o antes de publicar mensagens ofensivas. </p> """, unsafe_allow_html=True)





    # home_image = Image.open('img/home.png')
    # st.image(home_image, caption="")
    
    #st.markdown("""
           # ---
            #***Credits:***
            #> *The image was taken from the Slidesgo presentation template from [here](https://slidesgo.com/theme/international-day-against-bullying-at-school-including-cyberbullying#search-cyberbullying&position-1&results-10&rs=search), with the icons created by Falticons and infographics and images by Freepik*
           
            #---
            #""")

if selected == "Recursos":
    st.title("Recursos")
    st.markdown("""
                ---
                ***C�digo fonte da aplica��o***
                >  Aqui est� o [link](vou colocar) para o Github 
                ---
                ***Dataset***
                > Aqui est� o[link](vou colocar) para o Kaggle
                ---
    """)
    
if selected =="Contatos":
    st.title("Contatos dos pesquisadores")
    st.markdown("""
                ---
                #### Professora Ma. Raquel M. M. Fernandes
                ##### ***Doutoranda em Inform�tica, Programa de P�s-Gradua��o em Inform�tica (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                > Email: raquel.fernandes@ufrj.br
                               
                ---
                #### Professor Dr. Luiz Fernando Rust da Costa Carmo
                ##### ***Programa de P�s-Gradua��o em Inform�tica (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                > Email: rust@nce.ufrj.br
         
                ---

                #### Professora Dra. Claudia Lage Rebello da Motta
                ##### ***Programa de P�s-Gradua��o em Inform�tica (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                > Email: claudiam@nce.ufrj.br
         
                ---
                
                """)

    
 


if selected == "App":  

   

# Disponibilizei o resultado do treinamento com SVM e NB, o usu�rio pode escolher aqui 

    tipo = st.radio(
        "Selecione o algoritmo de aprendizado supervisionado:",
        ["SVM", "NB"],
        captions=[
            "Support vector machine",
            "Naive bayes",
        ],
    )

# Pegando a frase que o usu�rio vai digitar para analisar..
    input_text = st.text_input('Digite uma frase para an�lise:', key="texto")

    button = st.button("Analisar")
    st.button("Limpar", on_click=clear_text)



    if input_text and button:

        # Lendo o input
        input_data = {
                        "text" : [input_text] 
                    }

    #Dependendo da escolha, vai chamar uma fun��o ou outra

        with st.spinner("Analisando..."):
            
            if tipo == "SVM":
                # Carregando o modelo e o vetor
                modelo = fun.carregarmodelo('finalized_svm_model.joblib')
                vectorizer = fun.carregarmodelo('finalized_svm_vectorizer.joblib')
                
                # Detectando se o texto � ou n�o ....
                resp, flag = fun.classificar_frase_svm(modelo,vectorizer,input_text)
                if(flag):
                    alert =st.warning(resp)
                else:
                    alert =st.success(resp)
                



            elif tipo == "NB":
                # Carregando o modelo e o vetor
                modelo_nb = fun.carregarmodelo('finalized_nb_model.joblib')
                vectorizer_nb = fun.carregarmodelo('finalized_nb_vectorizer.joblib')
                
                # Detectando se o texto � ou n�o ....
                resp, flag = fun.classificar_frase_nb(modelo_nb,vectorizer_nb,input_text)
                if(flag):
                    alert =st.warning(resp)
                else:
                    alert =st.success(resp)

            
            else:
                st.success("nada selecionado")
            

            

    st.markdown("""
                ---
                ***Disclaimer:***
                > *As informa��es contidas neste formul�rio t�m car�ter exclusivamente acad�mico e s�o destinadas a fins de pesquisa.
                 N�o constituem aconselhamento jur�dico e s�o fornecidas como prot�tipo, sem garantias de exatid�o, completude ou atualidade.
                 Os autores n�o se responsabilizam por eventuais erros ou omiss�es.*
            
                ---
                """)
