# `Detecção de ervas daninhas usando visão computacional`
# `Weed detection using computer vision`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, 
oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> |Nome  | RA | Curso|
> |--|--|--|
> | Erick Aparecido Escagion | 249095  | Aluno de mestrado em Engenharia Elétrica na área de Engenharia de Computação|
> | Víctor Manuel Villegas Salabarria  | 272594  | Aluno de mestrado em Engenharia Mecânica|


## Descrição do Projeto
As ervas daninhas são uma das pragas agrícolas mais prejudiciais que tem um grande impacto sobre as plantações. As ervas daninhas são responsáveis pelo aumento dos custos de produção devido ao desperdício de culturas, o que tem um impacto significativo na economia agrícola global. Neste sentido, o objetivo geral deste projeto é detectar ervas daninhas em lavouras utilizando imagens de campos de cultivo para auxiliar o engenheiro-agrônomo a tomar decisões quanto à aplicação adequada de herbicidas, eliminando a necessidade de pulverização em massa, prática predominante na agricultura de grande escala, bem como reduzindo custos e tornando os produtos mais atrativos para os consumidores. 

## Metodologia
O método a ser utilizado neste trabalho é composto por: aquisição de dados, pré-processamento, experimentação de modelos e avaliação. Esse método será cíclico, para que, a cada avaliação de um modelo, sejam identificadas novas técnicas visando obter melhores resultados. Além disso, será estabelecida uma linha de base, que é um modelo de aprendizado de máquina simples para a criação de previsões rápidas para o conjunto de dados em questão. Somado a isso, durante a fase de experimentação, pretende-se utilizar alguns métodos recentes de aprendizado profundo que têm demonstrado um bom desempenho na deteccção de objetos; são eles: a família de métodos R-CNN - *Regions with CNN Features*; e a família de modelos YOLO - *You Only Look Once*. Além disso, estão previstas outras técnicas que auxiliam no aprendizado de redes profundas, como a aumentação de dados, a otimização de hiperparâmetros, o fine-tunning, entre outras. Após uma primeira análise dos dados, alguns pré-processamentos podem ser necessários, como a eliminação de ruídos e o recorte dos píxeis de borda indesejados. Por fim, na etapa de avaliação, para determinar se um objeto foi localizado corretamente, será usada a métrica quantitativa IoU (Intersecção sobre a União) como medida de similaridade. Essa medida é calculada pela área de sobreposição, dividida pelo tamanho da união das duas caixas delimitadoras. 

## Bases de Dados e Evolução

> |Base de Dados | Endereço na Web | Resumo descritivo
> |----- | ----- | -----
> *Weeds Computer Vision Project* | https://universe.roboflow.com/augmented-startups/weeds-nxe1w | Um conjunto de imagens de plantações com ervas daninhas que pode facilmente confundir os modelos de detecção de objetos devido à semelhança das ervas daninhas em relação aos seus arredores [5]. Esse conjunto contém 3664 imagens de treinamento (87%), 359 de validação (9%) e 180 imagens de teste (4%). As imagens estão disponíveis em formato JPEG, coloridas e com resolução de 416x416 píxeis.

## Ferramentas
No contexto do projeto delineado, várias ferramentas foram identificadas como fundamentais. Para a aquisição e pré-processamento de dados, o OpenCV e o Pillow (PIL) serão fundamentais para o processamento de imagens, juntamente com o NumPy e o Pandas para a manipulação e análise de dados tabulares. Na fase de experimentação de modelos, os frameworks TensorFlow ou PyTorch desempenharão um papel fundamental. Além disso,  bibliotecas especializadas em aumentação de dados e otimização de hiperparâmetros poderão ser testadas para tentar melhorar o desempenho dos modelos. Para a avaliação dos modelos, a utilização do Scikit-learn para métricas de desempenho, aliado ao Matplotlib ou Seaborn para a visualização de dados e gráficos, será crucial. Adicionalmente, considerando a detecção de objetos, a família de modelos Faster R-CNN (Regions with CNN Features) será uma opção relevante a ser explorada. Além das ferramentas específicas para cada etapa do processo, ferramentas de suporte como Git para controle de versão, Jupyter Notebook ou Google Colab para desenvolvimento interativo, e plataformas de comunicação como Slack ou Discord para colaboração em equipe serão altamente recomendadas.

## Principais desafios
Detectar ervas daninhas usando visão computacional apresenta desafios significativos devido à complexidade de distinguir as ervas daninhas em ambientes com tons de grama semelhantes, o que pode resultar em falsos positivos ou negativos [1]. Para superar essa dificuldade, é essencial empregar técnicas avançadas de processamento de imagem, como segmentação por cor, textura e forma, para aprimorar a precisão da detecção de ervas daninhas em imagens de campo. Além disso, o pré-processamento desempenha um papel crucial, simplificando a detecção e preparando as imagens para análise [2]. A utilização de técnicas avançadas de processamento de imagem se mostra promissora nesse contexto, contribuindo para a eficácia da detecção e classificação das ervas daninhas com maior precisão e eficiência [3]. Do mesmo jeito a utilização de algoritmos de deteção como Faster R-CNN permitiriam melhorar a precisão e eficiencia por meio de arquiteturas de aprendizado profundo como a Resnet e Mobilenet [4]. Por fim, o processo de inferência do modelo poderia ter um tempo reduzido de processamento computacional, tendo em vista a viabilidade de aplicação em uma solução embarcada em um drone com pulverizador, por exemplo.

## Cronograma

O cronogrma abaixo corresponde ao perído de 13/05/2024 a 23/06/2024 equivalente a seis semanas.

> |Atividades  | Semana 1 | Semana 2| Semana 3| Semana 4| Semana 5| Semana 6|
> |--|:--:|:--:|:--:|:--:|:--:|:--:|
> | Aquisição de dados | X | | | | | |
> | Pré-processamento |  X | X | | | | |
> | Modelo linha de base |   | X |  |  | | |
> | Apresentação dos resultados preliminares |   |  | X |  | | |
> | Experimentação |   |  | | X | X | X |
> | Avaliação |   |  |  |  | X | X |
> | Apresentação final |   |  |  |  |  | X|

## Workflow

![Workflow](projetos/weeds/assets/wf.jpg)

## Experimentos e Resultados preliminares

Após a escolha do dataset a ser utilizado, foi considerado importante explorar seus dados. Para isso, foi criado um notebook denominado exploratory_data_analysis.ipynb. Nele, foram desenvolvidas diversas funções com o objetivo principal de responder a algumas perguntas específicas: todas as imagens estão rotuladas? Qual é o número máximo e mínimo de boundboxes presentes em uma imagem? Qual é a média de boundboxes por imagem?

As análises realizadas confirmaram que todas as imagens estão rotuladas. Observou-se que cada imagem contém de 1 a 16 boundboxes, com uma média de aproximadamente 2,6 boundboxes por imagem.

Também foi confirmado que as imagens não apresentam variação de tamanho, sendo todas de 416x416 pixels, e que todas estão no formato RGB.

Foi plotado um histograma que mostra a frequência das cores para os dados de treino, teste e validação. Nele, é possível observar que o histograma apresenta picos nas cores preto e branco, mas que o restante da distribuição se assemelha a uma distribuição normal.

A rede Faster R-CNN do PyTorch foi utilizada para resolver o problema de detecção. Foram realizados três testes, todos com os mesmos hiperparâmetros, mas com diferentes quantidades de dados de treino em cada teste. No primeiro experimento, a rede foi treinada por 3 épocas utilizando 1000 bounding boxes, num total de 367 imagens. No segundo experimento, foram usadas 10 épocas e  739 imagens. No terceiro e último experimento, a rede foi treinada com 3000 bounding boxes, num total de 1079 imagens, o que representa apenas um terço dos dados coletados no dataset original devido ao alto custo computacional envolvido.

Dos resultados obtidos na avaliação destes modelos, foram geradas as curvas de Precisão vs Recall, além da precisão média (AP) e da Área sob a curva (AUC) para cada modelo, considerando o limiar de interseção sobre a união (IoU) de 0.5. Para este caso, conduzindo testes com 7, 75 e 120 imagens, os resultados sugerem que o número de dados de treino influencia na precisão da rede utilizada[6], algo que se tentará confirmar com futuros testes.

## Próximos passos

- Melhorar as métricas de avaliação dos modelos.
- Explorar mais arquiteturas de Redes Neurais.
- Modificar parâmetros e realizar comparações entre os resultados obtidos.
- Explorar distintos préprocessamentos nas redes a serem empleadas.
- Explorar variantes de redes da mesma familia Faster R-CNN
- Criar um mini dataset de imagens próprias e usá-lo para avaliar o comportamento da melhor rede treinada.

## Referências

> 1. Wang, Aichen, Wen Zhang, and Xinhua Wei. "A review on weed detection using ground-based machine vision and image processing techniques." Computers and electronics in agriculture 158 (2019): 226-240.
> 2. Molina-Villa, Manuel Alejandro, and Leonardo Enrique Solaque-Guzmán. "Machine vision system for weed detection using image filtering in vegetables crops." Revista Facultad de Ingeniería Universidad de Antioquia 80 (2016): 124-130.
> 3. Wu, Zhangnan, et al. "Review of weed detection methods based on computer vision." Sensors 21.11 (2021): 3647.
> 4. Sportelli, Mino, et al. "Evaluation of YOLO object detectors for weed detection in different turfgrass scenarios." Applied Sciences 13.14 (2023): 8502.
> 5. Startups, A. Weeds Dataset. [S.l.]: Roboflow, nov. 2021. https://universe.roboflow.com/augmented-startups/weeds-nxe1w. visited on 2024-05-05 Disponível em: <https://universe.roboflow.com/augmented-startups/weeds-nxe1w> 
> 6. Fromm, Michael, et al. "Automated detection of conifer seedlings in drone imagery using convolutional neural networks." Remote Sensing 11.21 (2019): 2585.