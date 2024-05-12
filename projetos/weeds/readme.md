# `Detecção de ervas daninhas usando visão computacional`
# `Weed detection using computer vision`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, 
oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> |Nome  | RA | Curso|
> |--|--|--|
> | Miguel Angelo Mena Póvoa | 016954  | Aluno especial|
> | Erick Aparecido Escagion | 249095  | Graduação em xxx|
> | Víctor Manuel Villegas Salabarria  | 27259  | Aluno de mestrado em Engenharia Mecânica|


## Descrição do Projeto
As ervas daninhas são uma das pragas agrícolas mais prejudiciais que tem um grande impacto sobre as plantações. As ervas daninhas são responsáveis pelo aumento dos custos de produção devido ao desperdício de culturas, o que tem um impacto significativo na economia agrícola global. Neste sentido, o objetivo geral deste projeto é detectar ervas daninhas em lavouras utilizando imagens de campos de cultivo para auxiliar o engenheiro-agrônomo a tomar decisões quanto à aplicação adequada de herbicidas, eliminando a necessidade de pulverização em massa, prática predominante na agricultura de grande escala, bem como reduzindo custos e tornando os produtos mais atrativos para os consumidores. 

## Metodologia
O método a ser utilizado neste trabalho é composto por: aquisição de dados, pré-processamento, experimentação de modelos e avaliação. Esse método será cíclico, para que, a cada avaliação de um modelo, sejam identificadas novas técnicas visando obter melhores resultados. Além disso, será estabelecida uma linha de base, que é um modelo de aprendizado de máquina simples para a criação de previsões rápidas para o conjunto de dados em questão. Somado a isso, durante a fase de experimentação, pretende-se utilizar alguns métodos recentes de aprendizado profundo que têm demonstrado um bom desempenho na deteccção de objetos; são eles: a família de métodos R-CNN - *Regions with CNN Features*; a família de modelos YOLO - *You Only Look Once*; e uma abordagem *Visual Transformer*, que tem sido uma alternativa às redes convolucionais para a detecção de objetos. Além disso, estão previstas outras técnicas que auxiliam no aprendizado de redes profundas, como a aumentação de dados, a otimização de hiperparâmetros, o fine-tunning, entre outras. Por fim, após uma primeira análise dos dados, alguns pré-processamentos podem ser necessários, como a eliminação de ruídos e o recorte dos píxeis de borda indesejados. 

## Bases de Dados e Evolução

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
*Weeds Computer Vision Project* | https://universe.roboflow.com/augmented-startups/weeds-nxe1w | Um conjunto de imagens de plantações com ervas daninhas que pode facilmente confundir os modelos de detecção de objetos devido à semelhança das ervas daninhas em relação aos seus arredores. Esse conjunto contém 3664 imagens de treinamento (87%), 359 de validação (9%) e 180 imagens de teste (4%). As imagens estão disponíveis em formato JPEG, coloridas e com resolução de 416x416 píxeis.

## Ferramentas
> Ferramentas e/ou bibliotecas a serem utilizadas (com base na visão atual do grupo sobre o projeto).
No contexto do projeto delineado, várias ferramentas foram identificadas como fundamentais. Para a aquisição e pré-processamento de dados, o OpenCV e o Pillow (PIL) serão fundamentais para o processamento de imagens, juntamente com o NumPy e o Pandas para a manipulação e análise de dados tabulares. Na fase de experimentação de modelos, os frameworks TensorFlow ou PyTorch desempenharão um papel fundamental. Além disso, a biblioteca Albumentations será recomendada para a aumentação de dados, enquanto o Optuna ou Ray Tune poderão ser empregados para a otimização de hiperparâmetros. Para a avaliação dos modelos, a utilização do Scikit-learn para métricas de desempenho, aliado ao Matplotlib ou Seaborn para a visualização de dados e gráficos, será crucial. Adicionalmente, considerando a detecção de objetos, a família de modelos YOLO (You Only Look Once) será uma opção relevante a ser explorada, juntamente com a família de métodos R-CNN (Regions with CNN Features) e a abordagem Visual Transformer. Além das ferramentas específicas para cada etapa do processo, ferramentas de suporte como Git para controle de versão, Jupyter Notebook ou Google Colab para desenvolvimento interativo, e plataformas de comunicação como Slack ou Discord para colaboração em equipe serão altamente recomendadas.

## Principais desafios
> Principais desafios que se espera encontrar ao longo do desenvolvimento do projeto.
Detectar ervas daninhas usando visão computacional apresenta desafios significativos devido à complexidade de distinguir as ervas daninhas em ambientes com tons de grama semelhantes, o que pode resultar em falsos positivos ou negativos. Para superar essa dificuldade, é essencial empregar técnicas avançadas de processamento de imagem, como segmentação por cor, textura e forma, para aprimorar a precisão da detecção de ervas daninhas em imagens de campo. Além disso, o pré-processamento desempenha um papel crucial, simplificando a detecção e preparando as imagens para análise. A utilização de técnicas avançadas de processamento de imagem se mostra promissora nesse contexto, contribuindo para a eficácia da detecção e classificação das ervas daninhas com maior precisão e eficiência.

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

## Referências
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.
1.Sportelli, Mino, et al. "Evaluation of YOLO object detectors for weed detection in different turfgrass scenarios." Applied Sciences 13.14 (2023): 8502.
2.Wang, Aichen, Wen Zhang, and Xinhua Wei. "A review on weed detection using ground-based machine vision and image processing techniques." Computers and electronics in agriculture 158 (2019): 226-240.
3.Molina-Villa, Manuel Alejandro, and Leonardo Enrique Solaque-Guzmán. "Machine vision system for weed detection using image filtering in vegetables crops." Revista Facultad de Ingeniería Universidad de Antioquia 80 (2016): 124-130.
4.Wu, Zhangnan, et al. "Review of weed detection methods based on computer vision." Sensors 21.11 (2021): 3647.

