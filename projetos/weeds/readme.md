# `Detecção de ervas daninhas usando visão computacional`
# `Weed detection using computer vision`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, 
oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> |Nome  | RA | Curso|
> |--|--|--|
> | Miguel Angelo Mena Póvoa | 016954  | Aluno especial|
> | Erick Aparecido Escagion | 249095  | Graduação em xxx|
> | Víctor Manuel Villegas Salabarria  | 27259  | xxxx|


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


## Principais desafios
> Principais desafios que se espera encontrar ao longo do desenvolvimento do projeto.

## Cronograma

> |Atividades  | Semana 1 | Semana 2| Semana 3| Semana 4| Semana 5| 
> |--|:--:|:--:|:--:|:--:|:--:|
> | Aquisição de dados | X | | | | |
> | Pré-processamento |  X | X | | | |
> | Modelo linha de base |   | X |  |  | |
> | Apresentação de resultados preliminares |   |  | X |  | |
> | Experimentação |   |  | X | X | X |
> | Avaliação |   |  |  |  | X |
> | Apresentação final |   |  |  |  | X |

## Referências
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.
