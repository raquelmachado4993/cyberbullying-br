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

#Função pra limpar o que o usuário digitou da primeira vez
def clear_text():
    st.session_state["texto"] = '' 
    alert.empty()

#Isso aqui mostra o menu com as opções
selected = option_menu(
    menu_title=None,
    options = ["Home", "App", "Recursos","Contatos","Ref"],
    icons = ["house-heart-fill","code-slash","folder-fill","person-lines-fill","bookmark-heart"],
    default_index=0,
    orientation="horizontal",
    )

#Cada if é o conteúdo de um menu 
if selected =="Ref":
    st.title("Pagina de referências")
    st.markdown(""" Vou colocar referências aqui nessa página. """)



if selected == "Home":
    st.title("Detecção de cyberbullying em Português Brasileiro &#128187;")

    
    st.markdown("""   
    
    <p style="text-align:justify">Esta aplicação tem como objetivo auxiliar na <strong>detecção automática de mensagens com potencial de cyberbullying</strong> em português brasileiro, utilizando <strong>técnicas de aprendizado de máquina (machine learning)</strong>. Você pode analisar frases com dois classificadores diferentes: <strong>SVM (Support Vector Machine)</strong> e <strong>Naive Bayes</strong>.</p>

    <p style="text-align:justify">Ela foi desenvolvida como parte de uma <strong>tese de doutorado</strong> que investiga a exposição de crianças e adolescentes a ameaças nos ambientes digitais. A pesquisa busca apoiar o trabalho pedagógico em conformidade com a <strong>BNCC</strong> (Base Nacional Comum Curricular), a <strong>PNED</strong> (Política Nacional de Educação Digital) e a <strong>E-Ciber</strong> (Estratégia Nacional de Segurança Cibernética).</p>

    <p style="text-align:justify">A hipótese central considera que uma <strong>taxonomia organizada de ameaças digitais</strong> pode facilitar sua identificação e servir como ferramenta prática em Computação e Educação. Como parte dessa investigação, esta aplicação foi criada para testar o uso de <strong>Inteligência Artificial</strong> como suporte à detecção de mensagens ofensivas.</p>
    """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Como funciona? &#128289; </font></h1> """, unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify"> Você digita uma frase, e o sistema verifica se ela tem <strong>características similares a mensagens de cyberbullying</strong> , 
    com base em modelos treinados com dados reais. Para isso, usamos aprendizado de máquina, uma técnica que permite que o sistema aprenda 
    com exemplos e identifique padrões automaticamente. </p> """, unsafe_allow_html=True)


    st.caption("""<h2><font color="ff1493"> SVM x Naive Bayes &#128202; </font></h1>""", unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify"> 
    Nesta aplicação, utilizamos dois algoritmos de aprendizado de máquina: Naive Bayes e SVM (Support vector machine). 
    Ambos são capazes de aprender com exemplos previamente classificados para identificar se uma frase pode ser considerada cyberbullying, 
    mas adotam abordagens diferentes.

    O SVM considera o padrão geral da frase como um todo, buscando separar frases ofensivas e não ofensivas com base em limites definidos 
    durante o treinamento. Já, o Naive Bayes se baseia na frequência das palavras, estimando a probabilidade de uma frase ser ofensiva  
    ou não com base nas palavras que ela contém.

    Em frases curtas com termos mais agressivos, ambos os algoritmos costumam concordar. Em frases mais sutis ou com ironia, o SVM pode 
    oferecer uma análise um pouco mais precisa já que considera mais o contexto. </p> """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Como usar? &#128220</font></h1>""", unsafe_allow_html=True)
    st.markdown("""
    <p>Acesse a aba <strong>App</strong>, digite uma frase no campo indicado e selecione o modelo de classificação desejado. 
    A resposta será exibida em poucos segundos.</p>

    <p>Mais informações sobre o conjunto de dados utilizado estão disponíveis no menu <strong>Recursos</strong>. </p> """, unsafe_allow_html=True)

    st.caption("""<h2><font color="ff1493">Importante </font>   <font color="ffd700"> &#9888;</font>   </h1>""", unsafe_allow_html=True)
    st.markdown("""
    Esta ferramenta é apenas um <strong>suporte à detecção</strong>. A determinação de um caso de cyberbullying envolve outros fatores importantes,
     como <strong>contexto</strong>, <strong>recorrência</strong> e <strong>intenção</strong>. A análise automática não substitui a 
     avaliação humana.</p> </p> """, unsafe_allow_html=True)
               
    st.caption("""<h2><font color="ff1493">Trabalhos futuros &#128679; </font></h1>""", unsafe_allow_html=True)
    st.markdown("""   
    <p style="text-align:justify"> Em versões futuras, a aplicação deverá ser aprimorada e adaptada para funcionar como uma <strong>extensão
     de navegador</strong> ou um <strong>aplicativo móvel</strong>, permitindo a detecção em tempo real e envio de notificações aos usuários 
     incentivando a reflexão antes de publicar mensagens ofensivas. </p> """, unsafe_allow_html=True)





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
                ***Código fonte da aplicação***
                >  Aqui está o [link](vou colocar) para o Github 
                ---
                ***Dataset***
                > Aqui está o[link](vou colocar) para o Kaggle
                ---
    """)
    
if selected =="Contatos":
    st.title("Contatos dos pesquisadores")
    st.markdown("""
                ---
                #### Professora Ma. Raquel M. M. Fernandes
                ##### ***Doutoranda em Informática, Programa de Pós-Graduação em Informática (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                > Email: raquel.fernandes@ufrj.br
                               
                ---
                #### Professor Dr. Luiz Fernando Rust da Costa Carmo
                ##### ***Programa de Pós-Graduação em Informática (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                > Email: rust@nce.ufrj.br
         
                ---

                #### Professora Dra. Claudia Lage Rebello da Motta
                ##### ***Programa de Pós-Graduação em Informática (PPGI) da Universidade Federal do Rio de Janeiro (UFRJ)***
                
                > Email: claudiam@nce.ufrj.br
         
                ---
                
                """)

    
 


if selected == "App":  

   

# Disponibilizei o resultado do treinamento com SVM e NB, o usuário pode escolher aqui 

    tipo = st.radio(
        "Selecione o algoritmo de aprendizado supervisionado:",
        ["SVM", "NB"],
        captions=[
            "Support vector machine",
            "Naive bayes",
        ],
    )

# Pegando a frase que o usuário vai digitar para analisar..
    input_text = st.text_input('Digite uma frase para análise:', key="texto")

    button = st.button("Analisar")
    st.button("Limpar", on_click=clear_text)



    if input_text and button:

        # Lendo o input
        input_data = {
                        "text" : [input_text] 
                    }

    #Dependendo da escolha, vai chamar uma função ou outra

        with st.spinner("Analisando..."):
            
            if tipo == "SVM":
                # Carregando o modelo e o vetor
                modelo = fun.carregarmodelo('finalized_svm_model.joblib')
                vectorizer = fun.carregarmodelo('finalized_svm_vectorizer.joblib')
                
                # Detectando se o texto é ou não ....
                resp, flag = fun.classificar_frase_svm(modelo,vectorizer,input_text)
                if(flag):
                    alert =st.warning(resp)
                else:
                    alert =st.success(resp)
                



            elif tipo == "NB":
                # Carregando o modelo e o vetor
                modelo_nb = fun.carregarmodelo('finalized_nb_model.joblib')
                vectorizer_nb = fun.carregarmodelo('finalized_nb_vectorizer.joblib')
                
                # Detectando se o texto é ou não ....
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
                > *As informações contidas neste formulário têm caráter exclusivamente acadêmico e são destinadas a fins de pesquisa.
                 Não constituem aconselhamento jurídico e são fornecidas como protótipo, sem garantias de exatidão, completude ou atualidade.
                 Os autores não se responsabilizam por eventuais erros ou omissões.*
            
                ---
                """)
