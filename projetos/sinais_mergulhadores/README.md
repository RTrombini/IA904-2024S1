# Leitor de Sinais de Mão de Mergulhadores
# Diver Hand Signal Reader

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome, RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em duplas ou trios.
> 
> | Nome                        | RA      | Curso                          |
> |-----------------------------|---------|--------------------------------|
> | Raphael Melloni Trombini    | 271322  | Aluno Especial                 |
> | Ícaro Dias dos Santos       | 245542  | Mestrado em Engenharia Mecânica|
> | José Alfredo Zapana García  | 272291  | Mestrado em Engenharia Elétrica|

## Descrição do Projeto

O objetivo deste projeto é desenvolver um sistema capaz de identificar e interpretar sinais de mão de mergulhadores, utilizando técnicas de visão computacional, para facilitar a comunicação subaquática e melhorar a segurança durante mergulhos. Este trabalho se inspira e busca contribuir para os objetivos do projeto CADDY, um projeto da União Europeia focado no desenvolvimento de tecnologias para entender e interagir com mergulhadores em ambientes subaquáticos. Os principais objetivos do CADDY incluem a compreensão do comportamento do mergulhador através da interpretação de gestos manuais simbólicos e outros indicadores não verbais, além do desenvolvimento de sistemas cognitivos de (re)planejamento de missões com base nessas interações. O projeto também explora a integração com o 'Caddian corpus', um conjunto extenso de comandos sintaticamente e semanticamente corretos dentro da linguagem hierárquica multi-AUV denominada Caddian, que foi especialmente desenvolvida para o projeto CADDY. Este corpus serve como base para o entendimento e a interpretação das interações subaquáticas, contendo desde comandos simples até sequências mais complexas de gestos.

## Metodologia

Estamos considerando duas abordagens principais para o desenvolvimento do sistema: uma envolve a detecção de mãos seguida pela classificação dos gestos a partir das regiões de interesse (ROI) detectadas; a outra explora o uso de modelos de detecção e classificação integrados, como YOLO. A escolha final dependerá de análises de viabilidade, considerando as características do dataset disponível, e a necessidade de eventualmente converter este dataset para um formato adequado como COCO para modelos como YOLO. Adicionalmente, consideraremos a necessidade de um pré-processamento das imagens para melhorar a visibilidade em condições subaquáticas desafiadoras, como baixo contraste, águas turvas e iluminação variada. Estamos abertos a explorar a abordagem que melhor se encaixe às necessidades e limitações do projeto pegando en conta que o modelo deveria ser embarcável no robô subaquático.

## Bases de Dados e Evolução

| Base de Dados                    | Endereço na Web                                                                     | Resumo Descritivo                                                                                                                                                                                                                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CADDY Underwater Gestures Dataset| [CADDY Dataset Homepage](http://www.caddian.eu//CADDY-Underwater-Gestures-Dataset.html)| Conjunto de dados composto por aproximadamente 10.000 pares de imagens estéreo coletadas em 8 cenários diferentes para interação subaquática humano-robô e contem imagens para 16 gestos da linguagem Caddian. As imagens foram capturadas durante experimentos que simulam diversas condições e tarefas subaquáticas, com o objetivo de desenvolver e testar sistemas de reconhecimento de gestos que facilitam a comunicação entre mergulhadores e veículos autônomos subaquáticos (AUVs). Cada cenário reflete um contexto específico de mergulho, variando desde ambientes com visibilidade reduzida até situações com iluminação artificial, projetados para desafiar e aprimorar a capacidade dos sistemas robóticos em entender e reagir a comandos humanos no ambiente subaquático. |

A distribuição do conjunto de dados é a seguinte:

### De acordo à presença de gestos

| Classe   | Total fotos estéreo |
|----------|---------------------|
| Positiva | 9239                |
| Negativa | 7190                |

### De acordo ao gesto realizado

| Comando        | ID de classe | Total fotos estéreo |
|----------------|--------------|---------------------|
| Start_comm     | 0            | 1820                |
| End_comm       | 1            | 1318                |
| Up             | 2            | 352                 |
| Down           | 3            | 462                 |
| Photo          | 4            | 925                 |
| Backwards      | 5            | 561                 |
| Carry          | 6            | 717                 |
| Boat           | 7            | 369                 |
| Here           | 8            | 261                 |
| Mosaic         | 9            | 226                 |
| Num_delimiter  | 10           | 992                 |
| One            | 11           | 161                 |
| Two            | 12           | 404                 |
| Three          | 13           | 388                 |
| Four           | 14           | 235                 |
| Five           | 15           | 48                  |

<details>
<summary title="Click to Expand/Collapse">Exemplos de gestos</summary>

| Comando    | Exemplo                                                        | Comando     | Exemplo                                                        |
|------------|-----------------------------------------------------------------|-------------|----------------------------------------------------------------|
| Start_comm | ![Image 1](https://github.com/RTrombini/IA904-2024S1/assets/114251488/63cb1e3e-c998-46da-9484-ba1113b858d9) | End_comm   | ![Image 2](https://github.com/RTrombini/IA904-2024S1/assets/114251488/c7a5043d-ce04-45c4-ac73-e42aeef2d768) |
| Up         | ![Image 3](https://github.com/RTrombini/IA904-2024S1/assets/114251488/43571b44-7074-4fb7-b297-711dce567490) | Down       | ![Image 4](https://github.com/RTrombini/IA904-2024S1/assets/114251488/f5f0f983-d4b3-4fc7-aa8a-2fea37aea9ea) |
| Photo      | ![Image 5](https://github.com/RTrombini/IA904-2024S1/assets/114251488/a1bec6b3-8835-4b3a-9e5b-62013569f704) | Backwards  | ![Image 6](https://github.com/RTrombini/IA904-2024S1/assets/114251488/f56b2498-95f5-4f76-9683-a3a8859f0e2b) |
| Carry      | ![Image 7](https://github.com/RTrombini/IA904-2024S1/assets/114251488/16bf799f-3a2d-4818-927e-7c498dd98068) | Boat       | ![Image 8](https://github.com/RTrombini/IA904-2024S1/assets/114251488/8d63032f-3b46-4b97-9e64-5f6b7159e666) |
| Here       | ![Image 9](https://github.com/RTrombini/IA904-2024S1/assets/114251488/42423ef1-88d0-4c36-af07-e3bdc64e8bdd) | Num_delimiter | ![Image 10](https://github.com/RTrombini/IA904-2024S1/assets/114251488/a36ced6b-ada7-4fc1-ba31-3f0f1224f334) |
| One        | ![Image 11](https://github.com/RTrombini/IA904-2024S1/assets/114251488/5607f938-dbc3-461f-96dc-6d7dd9e3d65b) | Two        | ![Image 12](https://github.com/RTrombini/IA904-2024S1/assets/114251488/b27d0738-14b2-4986-8600-9cba39e58588) |
| Three      | ![Image 13](https://github.com/RTrombini/IA904-2024S1/assets/114251488/f48fe56a-05d5-44c9-8c00-f1dfe7e7ee3d) | Four       | ![Image 14](https://github.com/RTrombini/IA904-2024S1/assets/114251488/3f394f60-9fb5-4994-bdf5-78e773c5f25f) |
| Five       | ![Image 15](https://github.com/RTrombini/IA904-2024S1/assets/114251488/d745bccd-2110-479c-b675-e4d53a7554e4) |

</details>


## Ferramentas

- Linguagem de programação principal: Python
- Bibliotecas para pré-processamento de imagens: OpenCV, Pillow (PIL), Numpy
- Bibliotecas para aumento de imagens: Torchvision
- Bibliotecas para Deep Learning: PyTorch, YOLOv8
- Biblioteca para manipulação de dados: pandas
- Bibliotecas para avaliação dos modelos: PyTorch e Sklearn (métricas), Matplotlib (visualização)

## Workflow

### Detecção com YOLO

#### 1. Preparação do Dataset

##### Dataset Inicial:

O dataset inicial consistia em imagens estéreo (esquerda e direita) de mergulhadores realizando diversos gestos. As imagens foram divididas em duas categorias principais:
- **True Positives**: Contendo gestos a serem reconhecidos.
- **True Negatives**: Sem gestos.

Cada imagem no dataset era acompanhada por um arquivo CSV com as seguintes informações:
- `index`: Índice da imagem.
- `scenario`: Cenário da imagem.
- `stereo left`: Caminho para a imagem estéreo esquerda.
- `stereo right`: Caminho para a imagem estéreo direita.
- `label name`: Nome da classe do gesto.
- `label id`: ID da classe do gesto.
- `roi left`: Região de interesse na imagem esquerda.
- `roi right`: Região de interesse na imagem direita.

##### Conversão do Dataset:

Para utilizar o YOLOv8, o dataset precisava ser convertido para um formato compatível. Este processo incluiu várias etapas:

###### Combinação dos CSVs True Positives e True Negatives:
- Os CSVs de true positives e true negatives foram combinados em um único CSV.
- Adicionamos "Negative" como uma classe e ajustamos os IDs de classe conforme necessário.

###### Filtragem de Imagens:
- Apenas imagens com anotações válidas foram mantidas.
- Imagens duplicadas (esquerda e direita) foram removidas para evitar overfitting. Apenas imagens da direita foram mantidas.

###### Criação de Arquivos de Anotação YOLO:
- Convertendo as coordenadas de ROI para o formato YOLO.
- Salvando as anotações em arquivos `.txt` no formato YOLO.

###### Divisão em Conjuntos de Treino, Validação e Teste:
- O dataset foi dividido em 80% para treino, 10% para validação e 10% para teste.
- As imagens e anotações correspondentes foram movidas para diretórios específicos.

###### Diagrama de Fluxo para `dataset_converter.ipynb`:

![dataset_converter](https://github.com/RTrombini/IA904-2024S1/assets/114251488/cc7c1d8c-361b-4658-be60-bcae8ca3f456)

#### 2. Estrutura do Dataset Final

##### Estrutura de Diretórios:

```text
Dataset/
│
├── images/
│   ├── train/
│   ├── val/
│   └── test/
│
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
│
└── dataset.yaml
```

###### Formato dos Arquivos de Anotação:

Cada arquivo .txt de anotação segue o formato YOLO:

```
<class_id> <x_center> <y_center> <width> <height>

```

### 3. Treinamento da YOLOv8 Nano

#### Configuração do Treinamento:

Utilizou-se o modelo pré-treinado YOLOv8 nano (`yolov8n.pt`).

**Parâmetros de treinamento:**
- **Épocas:** 100
- **Tamanho das imagens:** 640x640 pixels

**Diagrama de Fluxo para `yolo_training.ipynb`:**

![train](https://github.com/RTrombini/IA904-2024S1/assets/114251488/73770e7c-df2e-42ed-ad79-981c90211541)

### 4. Realizar Inferência com o Modelo Treinado

**Diagrama de Fluxo para `yolo_inference.ipynb`:**

![inference](https://github.com/RTrombini/IA904-2024S1/assets/114251488/3517f803-35f6-4b87-8cfc-7fb5b21d28c6)

### Relação entre os Três Notebooks

**Diagrama Geral de Relação entre os Três Notebooks:**

![general](https://github.com/RTrombini/IA904-2024S1/assets/114251488/55a00f0b-0506-4ec8-a7eb-49549c96aa27)

Este fluxo de trabalho mostra como os três notebooks se conectam e interagem entre si no processo completo de detecção com YOLOv8.

## Experimentos e Resultados preliminares

### Experimento com YOLOv8

Realizamos um experimento com o modelo YOLOv8 para avaliar a dificuldade de detectar as mãos dos mergulhadores nas imagens subaquáticas. Para nossa surpresa, a detecção de mãos foi muito bem-sucedida, mesmo nas imagens mais turvas e com baixa visibilidade. Motivados por esses resultados positivos, prosseguimos com o treinamento do modelo para a detecção de gestos específicos, separados em 16 classes (15 classes de gestos e uma classe sem gestos).

#### Preparação do Dataset:

- Utilizamos as classes e Regiões de Interesse (ROIs) disponíveis no arquivo CSV do dataset original.
- Para evitar overfitting, optamos por usar apenas metade das imagens, especificamente as imagens right. Como tínhamos imagens left e right devido ao uso de câmeras estéreo, essa escolha manteve a diversidade do dataset sem repetir dados.
- Não aplicamos nenhum pré-processamento nas imagens neste teste, para observar os resultados da maneira mais crua possível.

#### Treinamento:

- O modelo YOLOv8 nano foi treinado com as imagens do dataset preparado.
- O treinamento incluiu 100 épocas com imagens de 640x640 pixels.

#### Resultados:

- A detecção de gestos foi aceitável, com o modelo conseguindo identificar os diferentes gestos subaquáticos.
- Resultados detalhados, incluindo tabelas de verdade e curvas ROC, serão adicionados posteriormente para explicar os resultados em detalhes.

##### Matriz de confusão:

- Segue abaixo a matriz de confusão  com os valores absolutos da detecção no dataset de testes:

![confusion_matrix](https://github.com/RTrombini/IA904-2024S1/assets/114251488/d86f3b33-a171-418c-a452-2c01fb2466da)

- Segue abaixo a matriz de confusão  normalizada da detecção no dataset de testes:



![confusion_matrix_normalized](https://github.com/RTrombini/IA904-2024S1/assets/114251488/cad0fa07-aafa-4ec9-932e-da977fee5961)


##### Classes Corretamente Classificadas

| Classe          | Percentual de Acertos | Observação                                                          |
|-----------------|-----------------------|---------------------------------------------------------------------|
| start_comm      | 100%                  | Todas as instâncias foram corretamente classificadas como start_comm. |
| end_comm        | 100%                  | Todas as instâncias foram corretamente classificadas como end_comm.   |
| up              | 100%                  | Todas as instâncias foram corretamente classificadas como up.         |
| down            | 98%                   | 2% das instâncias foram erroneamente classificadas.                  |
| photo           | 99%                   | Todas as instâncias foram corretamente classificadas como photo.      |
| backwards       | 98%                   | 2% das instâncias foram erroneamente classificadas.                  |
| carry           | 100%                  | Todas as instâncias foram corretamente classificadas como carry.      |
| boat            | 99%                   | Todas as instâncias foram corretamente classificadas como boat.       |
| here            | 98%                   | 2% das instâncias foram erroneamente classificadas.                  |
| mosaic          | 0%                    | não houveram instancias classificadas como mosaic                  |
| num_delimiter   | 98%                   | 2% das instâncias foram erroneamente classificadas.                  |
| one             | 97%                   | 3% das instâncias foram erroneamente classificadas.                  |
| two             | 100%                  | Todas as instâncias foram corretamente classificadas como two.        |
| three           | 99%                   | 1% das instâncias foram erroneamente classificadas.                  |
| four            | 97%                   | 3% das instâncias foram erroneamente classificadas.                  |
| five            | 100%                  | Todas as instâncias foram corretamente classificadas como five.       |
| negative        | 0%                    | As instâncias não  foram classificadas como negative.   |
| background      | 100%                  | Todas as instâncias negative foram  classificadas como background. |

### Erros de Classificação

| Classe    | Percentual de Erro | Observação                                            |
|-----------|---------------------|-------------------------------------------------------|
| down      | 2%                  | 2% das instâncias de down foram erroneamente classificadas.   |
| backwards | 2%                  | 2% das instâncias de backwards foram erroneamente classificadas.|
| mosaic    | 100%                  | 3% das instâncias de mosaic foram erroneamente classificadas.   |
| three     | 1%                  | 1% das instâncias de three foram erroneamente classificadas.    |


<details>
<summary title="Click to Expand/Collapse">Exemplos de gestos</summary>

| Comando            | Exemplo                                                        | Comando            | Exemplo                                                        |
|--------------------|-----------------------------------------------------------------|--------------------|----------------------------------------------------------------|
| Start_comm         | ![Image 1](https://github.com/RTrombini/IA904-2024S1/assets/114251488/e3baf444-2248-4fd9-a685-0f0018646604) | End_comm           | ![Image 2](https://github.com/RTrombini/IA904-2024S1/assets/114251488/92a3a846-bf6f-45bd-90ec-9bb845e7303c) |
| Up                 | ![Image 3](https://github.com/RTrombini/IA904-2024S1/assets/114251488/e5fa9164-a62b-4943-88ca-97ba5a0d128e) | Down               | ![Image 4](https://github.com/RTrombini/IA904-2024S1/assets/114251488/b9bf5fd3-fca9-48ea-8d07-56c7d7625b36) |
| Photo              | ![Image 5](https://github.com/RTrombini/IA904-2024S1/assets/114251488/be407c4a-f562-459f-90a4-1c282be64c3e) | Backwards          | ![Image 6](https://github.com/RTrombini/IA904-2024S1/assets/114251488/d3db314e-8c55-4fe5-8def-ea1d64aa11ec) |
| Carry              | ![Image 7](https://github.com/RTrombini/IA904-2024S1/assets/114251488/88feb56e-8303-4f5f-a0e0-97aadcf2d816) | Boat               | ![Image 8](https://github.com/RTrombini/IA904-2024S1/assets/114251488/ecdd8bb3-418f-4fe6-91a1-28510a15b93e) |
| Here               | ![Image 9](https://github.com/RTrombini/IA904-2024S1/assets/114251488/b0d8d429-0af2-4e1b-a841-04998398659b) | Num_delimiter      | ![Image 10](https://github.com/RTrombini/IA904-2024S1/assets/114251488/6154ce84-c3bc-4276-a4cb-51e16169f317) |
| One                | ![Image 11](https://github.com/RTrombini/IA904-2024S1/assets/114251488/8e8c66a1-de9d-4035-9e93-9f5334c1203d) | Two                | ![Image 12](https://github.com/RTrombini/IA904-2024S1/assets/114251488/578c3f88-e4aa-44dc-b1f3-f354cd210616) |
| Three              | ![Image 13](https://github.com/RTrombini/IA904-2024S1/assets/114251488/90468027-68cc-45b9-8cdc-ff050c44f061) | Four               | ![Image 14](https://github.com/RTrombini/IA904-2024S1/assets/114251488/395fc8ef-3304-495e-82a8-8e8702ac7e18) |
| Five               | ![Image 15](https://github.com/RTrombini/IA904-2024S1/assets/114251488/ae38eb6f-331f-4e68-ae99-bc9a9866d01c) | Negative           | ![Image 16](https://github.com/RTrombini/IA904-2024S1/assets/114251488/9553fb1e-c831-4399-9740-7f6c0991d2f8) |

</details>

###  Detecção com Modelo Shallow U-net + CNN

Esse modelo contou com duas etapas, primeiro o treinamento de uma rede Shallow U-net para segmentar os gestos feitos pelos mergulhadores, usando só duas classes (negativo e positivo). Depois de avaliar que a segmentação é feita corretamente, se continuou com um segundo treinamento de outra rede com os outputs da Shallow U-net para classificar os gestos, nessa segunda etapa se usaram 17 classes (16 gestos na base de dados + classe negativa).

#### Segmentação com Shallow U-Net

##### Preparação Do Dataset

###### Divisão em Conjuntos de Treino, Validação e Teste:
- Se selecionou 75% do dataset original para gerar um dataset de prova.
- Se utilizou um seed 42 para fazer todo split (dataset não usado, train-test-val split).
- Esse dataset reduzido foi dividido em 72% para treino, 10% para validação e 18% para teste.
- Se escolheu só usar as imágens da esquerda.

##### Treinamento da Shallow U-Net

###### Aumentação dos Dados
As seguintes transformações são aplicadas aos dados de treinamento usando `transforms.Compose`:

1. **RandomZoomOut**: Aplica um zoom out aleatório na imagem com uma probabilidade de 20%.
2. **RandomRotation**: Rotaciona a imagem aleatoriamente dentro do intervalo de 0 a 20 graus.
3. **RandomHorizontalFlip**: Inverte a imagem horizontalmente com uma probabilidade de 50%.
4. **GaussianBlur**: Aplica um desfoque gaussiano com um tamanho de kernel de 3x3.
5. **RandomAdjustSharpness**: Ajusta a nitidez da imagem com um fator de nitidez de 1.25.
6. **Resize**: Finalmente todas as imagens foram reajustadas para ter o mesmo tamanho depois das transformações.

###### Características de Treinamento

- Batch size: 32
- Tamanho das imagens: (162,212,3)
- Número de classes: 2
- Profundidade: 3
- Filtros inicíais: 32
- Modo: Concatenação
- Épocas: 188
- Learning rate: 0.00005

#### Desempenho do Algoritmo

A continuação se apresenta as curvas de perdas nos conjuntos de treinamento e validação.

![Curva-perda](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/curva_perda.png)

No caso das métricas de avaliação por segmentação:
- Pixel Accuracy: 85.4 %
- IoU: 0.93

<details>
<summary title="Click to Expand/Collapse">Exemplos de gestos</summary>

![Example Results](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_20.png)

![Example Results](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_80.png)

![Example Results](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_120.png)

![Example Results](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_1498.png)

![Example Results](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_1378.png)

</details>

#### Classificação com rede CNN

##### Preparação Do Dataset

###### Divisão em Conjuntos de Treino, Validação e Teste:
- Se utilizou todo o dataset.
- Se utilizou um seed 42 para fazer todo split (train-test-val split).
- Esse dataset reduzido foi dividido em 76.5% para treino, 10% para validação e 13.5% para teste.
- Se escolheu só usar as imágens da esquerda.

##### Treinamento da Rede CNN

###### Aumentação dos Dados
As seguintes transformações são aplicadas aos dados de treinamento usando `transforms.Compose`:

1. **RandomZoomOut**: Aplica um zoom out aleatório na imagem com uma probabilidade de 20%.
2. **RandomRotation**: Rotaciona a imagem aleatoriamente dentro do intervalo de 0 a 20 graus.
3. **RandomHorizontalFlip**: Inverte a imagem horizontalmente com uma probabilidade de 50%.
4. **GaussianBlur**: Aplica um desfoque gaussiano com um tamanho de kernel de 3x3.
5. **RandomAdjustSharpness**: Ajusta a nitidez da imagem com um fator de nitidez de 1.25.
6. **Resize**: Finalmente todas as imagens foram reajustadas para ter o mesmo tamanho depois das transformações.

###### Características de Treinamento

- Batch size: 32
- Tamanho das imagens: (162,212,3)
- Número de classes: 17
- Épocas: 150
- Learning rate inícial: 0.00005
- Learning rate decay: 0.98, cada 5 épocas

## Avaliação


## Experimentos e Resultados

### Shallow U-net + CNN

#### Curvas de perdas e precisão

Como o treinamento da rede Shallow U-net + CNN teve duas etapas, se obtiveram duas curvas de perdas

![Curva de Perda UNet](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/curva_perda_unet.png)

![Curves Classification Gestures](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/curves_classification_gestures.png)

#### Matriz de confusão

![Confusion Matrix](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/conf_matrix.png)

#### Relátorio de classificação

![Classification Report](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/classification_report.png)

#### Métricas de classificação globais

- Matthews Correlation Coefficient: 0.94
- Precisão: 0.95
- Sensibilidade: 0.91
- F1 score: 0.92 
- Cohen Kappa score: 0.94

## Discussão

## Conclusão

## Trabalhos futuros

## Referências
- Gomez Chavez, A.; Ranieri, A.; Chiarella, D.; et al. CADDY Underwater Stereo-Vision Dataset for Human–Robot Interaction (HRI) in the Context of Diver Activities. J. Mar. Sci. Eng. 2019, 7, 16.
- Chiarella, D. Towards Multi-AUV Collaboration and Coordination: A Gesture-Based Multi-AUV Hierarchical Language and a Language Framework Comparison System. J. Mar. Sci. Eng. 2023, 11, 1208.
