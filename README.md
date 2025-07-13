
# Detectando Cyberbullying em Português do Brasil  


Esta aplicação tem como objetivo auxiliar na **detecção automática de mensagens com potencial de cyberbullying** em português brasileiro, utilizando
  **técnicas de aprendizado de máquina (machine learning)** . Você pode analisar frases com dois classificadores diferentes: **SVM (Support Vector Machine)** e **Naive Bayes**.

  Ela foi desenvolvida como parte de uma **tese de doutorado** que investiga a exposição de crianças e adolescentes a ameaças nos ambientes digitais. A pesquisa busca apoiar o trabalho pedagógico em conformidade com a **BNCC** (Base Nacional Comum Curricular), a **PNED** (Política Nacional de Educação Digital) e a **E-Ciber** (Estratégia Nacional de Segurança Cibernética).

  A hipótese central considera que uma **taxonomia organizada de ameaças digitais** pode facilitar sua identificação e servir como ferramenta prática em Computação e Educação. Como parte dessa investigação, esta aplicação foi criada para testar o uso de **Inteligência Artificial** como suporte à detecção de mensagens ofensivas.


## Como funciona? &#128289;
  
  Você digita uma frase, e o sistema verifica se ela tem **características similares a mensagens de cyberbullying** , 
  com base em modelos treinados com dados reais. Para isso, usamos aprendizado de máquina, uma técnica que permite que o sistema aprenda 
  com exemplos e identifique padrões automaticamente. 


##  SVM x Naive Bayes  &#128202;
  
  
 Nesta aplicação, utilizamos dois algoritmos de aprendizado de máquina: Naive Bayes e SVM (Support vector machine). 
 Ambos são capazes de aprender com exemplos previamente classificados para identificar se uma frase pode ser considerada cyberbullying, 
 mas adotam abordagens diferentes.

 O SVM considera o padrão geral da frase como um todo, buscando separar frases ofensivas e não ofensivas com base em limites definidos 
 durante o treinamento. Já, o Naive Bayes se baseia na frequência das palavras, estimando a probabilidade de uma frase ser ofensiva  
 ou não com base nas palavras que ela contém.

 Em frases curtas com termos mais agressivos, ambos os algoritmos costumam concordar. Em frases mais sutis ou com ironia, o SVM pode 
 oferecer uma análise um pouco mais precisa já que considera mais o contexto. 

### Como usar? &#128220
  
 Acesse a aba **App**, digite uma frase no campo indicado e selecione o modelo de classificação desejado. 
 A resposta será exíbida em poucos segundos.

 Mais informações sobre o conjunto de dados utilizado estão disponíveis no menu **Recursos**. 

### Importante   &#9888;
  
 Esta ferramenta é apenas um **suporte à detecção** . A determinação de um caso de cyberbullying envolve outros fatores importantes,
  como **contexto**, **recorrência** e **intenção** . A análise automática não substitui a 
  avaliação humana. 

### Trabalhos futuros &#128679;
  
Em versões futuras, a aplicação deverá ser aprimorada e adaptada para funcionar como uma **extensão de navegador** ou um **aplicativo móvel**, permitindo a detecção em tempo real e envio de notificações aos usuários 
incentivando a reflexão antes de publicar mensagens ofensivas. 



## Como executar o código via container

### Aqui estamos usando container 

 O código está em um container para garantir isolamento e execução do ambiente, incluindo todas as dependências do Python. As bibliotecas, como o Pandas, por exemplo, tiveram suas versões definidas para que futuras execuções utilizem exatamente as mesmas versões, evitando erros por mudanças ou incompatibilidades.


```bash

    # Criando a imagem de um container
    docker image build  -t tese  .
    
    # ter aceso ao shell e ser mais iterativo
    docker  run -it --rm  -v $(pwd)/:/scripts tese sh 

    cd scripts/

    # execute o código
    streamlit run inicial.py

```

### Licença pra uso do código

 Este programa é software livre: você pode redistribuí-lo e/ou modificá-lo
 sob os termos da Licença Pública Geral GNU conforme publicada pela Free Software Foundation,
 tanto na versão 3 da Licença como (a seu critério) qualquer versão posterior.

 Este programa é distribuído na esperança de que seja útil,
 mas SEM NENHUMA GARANTIA; sem mesmo a garantia implícita de
 COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO.
 Consulte a Licença Pública Geral GNU para mais detalhes.

 Você deve ter recebido uma cópia da Licença Pública Geral GNU
 junto com este programa. Caso contrário, veja <https://www.gnu.org/licenses/>.

Raquel M. M. Fernandes, 2025  
 
