
# Detectando Cyberbullying em Português do Brasil  


Esta aplicação tem como objetivo auxiliar na ampliação dos estudos em **detecção automática de mensagens com potencial de cyberbullying** em português brasileiro investigando o uso de técnicas de **aprendizado de máquina (machine learning)**.

A aplicação é um protótipo, isto é, uma pequena amostra como parte de uma pesquisa de Doutorado em Informática que investiga a exposição de crianças e adolescentes a ameaças nos ambientes digitais e propõe o uso de Inteligência Artificial para detectá-las e mitigá-las.


## Como funciona? &#128289;
  
  Ao digitar uma frase e enviá-la para análise, o sistema verifica se ela tem **características similares a mensagens de cyberbullying**, com base em modelos treinados com dados reais.


##  SVM x Naive Bayes  &#128202;
  
  
Nesta aplicação, utilizamos dois algoritmos de aprendizado de máquina: **Naive Bayes** e **SVM (Support vector machine)**. Ambos são capazes de aprender com exemplos previamente classificados para identificar se uma frase pode ser considerada cyberbullying ou não, mas adotam abordagens diferentes.

O SVM considera o padrão geral da frase, buscando separar frases ofensivas e não ofensivas com base em limites definidos durante o treinamento. Já, o Naive Bayes se baseia na frequência das palavras e estima a probabilidade de uma frase ser ofensiva ou não com base nas palavras que ela contém.

Em frases curtas com termos mais agressivos, ambos os algoritmos costumam concordar. Em frases mais sutis ou com ironia, o SVM pode oferecer uma análise um pouco mais precisa.

### Como usar? &#128220
  
Acesse a aba **App**, digite uma frase no campo indicado e selecione o modelo de classificação desejado. Clique no botão **Analisar**. A resposta será exibida em poucos segundos.

Mais informações sobre o conjunto de dados utilizado na etapa de treinamento do modelo estão disponíveis no menu Recursos.

### Importante   &#9888;
  
Esta ferramenta é apenas um **suporte à detecção**. A determinação de um caso de cyberbullying envolve outros fatores importantes, como contexto, recorrência e intenção. A análise automática não substitui a avaliação humana.

### Trabalhos futuros &#128679;
  
Em versões futuras, a aplicação deverá ser aprimorada e adaptada para funcionar como uma extensão de navegador e/ou um aplicativo, permitindo a detecção em tempo real e envio de notificações aos usuários incentivando a reflexão antes de publicar mensagens ofensivas. Além disso, o dataset também deve ser aprimorado para incluir exemplos mais diversos e representativos, incluindo textos advindos de outras plataformas.


## Disponível em: 

https://cyberbullying-br.streamlit.app/

https://github.com/raquelmachado4993/cyberbullying-br 




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
 
