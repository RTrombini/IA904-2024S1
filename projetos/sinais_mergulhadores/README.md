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

Estamos considerando duas abordagens principais para o desenvolvimento do sistema: uma envolve a detecção de mãos seguida pela classificação dos gestos a partir das regiões de interesse (ROI) detectadas; a outra explora o uso de modelos de detecção e classificação integrados, como YOLO. A escolha final dependerá de análises de viabilidade, considerando as características do dataset disponível, que atualmente está no formato CSV, e a necessidade de eventualmente converter este dataset para um formato adequado como COCO para modelos como YOLO. Adicionalmente, consideraremos a necessidade de um pré-processamento das imagens para melhorar a visibilidade em condições subaquáticas desafiadoras, como baixo contraste, águas turvas e iluminação variada. Estamos abertos a explorar a abordagem que melhor se encaixe às necessidades e limitações do projeto.

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
<summary>Exemplos de gestos</summary>

| Comando    | Exemplo                                                        | Comando     | Exemplo                                                        |
|------------|-----------------------------------------------------------------|-------------|----------------------------------------------------------------|
| Start_comm | ![Image 1](./data/raw/brodarski-C/true_positives/raw/brodarski-C_00637_left.jpg) | End_comm   | ![Image 2](./data/raw/biograd-A/true_positives/raw/biograd-A_00571_left.jpg) |
| Up         | ![Image 3](./data/raw/genova-A/true_positives/raw/genova-A_02906_left.jpg)     | Down       | ![Image 4](./data/raw/genova-A/true_positives/raw/genova-A_01058_left.jpg)   |
| Photo      | ![Image 5](./data/raw/genova-A/true_positives/raw/genova-A_01540_left.jpg)     | Backwards  | ![Image 6](./data/raw//biograd-C/true_positives/raw/biograd-C_01587_left.jpg)|
| Carry      | ![Image 7](./data/raw/genova-A/true_positives/raw/genova-A_01132_left.jpg)     | Boat       | ![Image 8](./data/raw/biograd-A/true_positives/raw/biograd-A_01004_left.jpg) |
| Here       | ![Image 9](./data/raw/brodarski-C/true_positives/raw/brodarski-C_00487_left.jpg) | Mosaic    | ![Image 10](./data/raw/biograd-C/true_positives/raw/biograd-C_00820_left.jpg)|
| Num_delimiter | ![Image 11](./data/raw/biograd-A/true_positives/raw/biograd-A_00564_left.jpg)| One        | ![Image 12](./data/raw/biograd-B/true_positives/raw/biograd-B_00429_left.jpg)|
| Two        | ![Image 13](./data/raw/brodarski-D/true_positives/raw/brodarski-D_00087_left.jpg) | Three    | ![Image 14](./data/raw/genova-A/true_positives/raw/genova-A_02156_left.jpg)  |
| Four       | ![Image 15](./data/raw/biograd-C/true_positives/raw/biograd-C_00844_left.jpg)    | Five     | ![Image 16](./data/raw/biograd-A/true_positives/raw/biograd-A_00106_left.jpg)|

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
![Diagrama Dataset_converter](./projetos/sinais_mergulhadores/assets/worflows/dataset_converter.png)

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

![Diagrama YOLO train](./projetos/sinais_mergulhadores/assets/worflows/train.png)

### 4. Realizar Inferência com o Modelo Treinado

**Diagrama de Fluxo para `yolo_inference.ipynb`:**

![Diagrama YOLO Inference](./projetos/sinais_mergulhadores/assets/worflows/inference.png)

### Relação entre os Três Notebooks

**Diagrama Geral de Relação entre os Três Notebooks:**

![Diagrama Geral](./projetos/sinais_mergulhadores/assets/worflows/general.png)

Este fluxo de trabalho mostra como os três notebooks se conectam e interagem entre si no processo completo de detecção com YOLOv8.

### Experimentos e Resultados Preliminares

> Descreva de forma sucinta e organizada os experimentos realizados.
> Para cada experimento, apresente os principais resultados obtidos.
> Aponte os problemas encontrados nas soluções testadas até aqui.

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

 ![matriz de confusão  com os valores absolutos](./projetos/sinais_mergulhadores/notebook/yolo_test/runs/detect/train/confusion_matrix.png)

- Segue abaixo a matriz de confusão  normalizada da detecção no dataset de testes:

 ![matriz de confusão  normalizada](./projetos/sinais_mergulhadores/notebook/yolo_test/runs/detect/train/confusion_matrix_normalized.png)



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

| Comando            | Exemplo               | Comando            | Exemplo               |
|-------------------------|-------------------------|-------------------------|-------------------------|
| Start_comm | ![Image 1](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00286_right.jpg) | End_comm | ![Image 2](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00027_right.jpg) |
| Up | ![Image 3](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00257_right.jpg) | Down | ![Image 4](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00339_right.jpg) |
| Photo | ![Image 5](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/genova-A_01528_right.jpg) | Backwards | ![Image 6](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00409_right.jpg) |
| Carry | ![Image 7](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/genova-A_01614_right.jpg) | Boat | ![Image 8](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-B_00605_right.jpg) |
| Here | ![Image 9](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-B_00651_right.jpg) | Num_delimiter | ![Image 10](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00019_right.jpg) |
| One | ![Image 11](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00041_right.jpg) | Two | ![Image 12](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00373_right.jpg) |
| Three | ![Image 13](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00176_right.jpg) | Four | ![Image 14](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00088_right.jpg) |
| Five | ![Image 15](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/biograd-A_00259_right.jpg) | Negative | ![Image 16](projetos/sinais_mergulhadores/notebook/yolo_test/inference_results/neg_biograd-C_00280_right.jpg) |
</details>



#### Problemas Encontrados:

- As imagens estavam no formato RGB, mas todo o treinamento foi feito com as imagens em BGR, resultando em inferências com cores distorcidas, deixando as imagens amareladas. É necessário retreinar o modelo corrigindo o dataset para o formato de cor correto.
- A susceptibilidade ao overfitting foi uma dificuldade encontrada, mesmo após a remoção das imagens duplicadas.
- Aparentemente, todas as imagens da classe negative foram detectadas como background.


## Próximos passos
> Liste as próximas etapas planejadas para conclusão do projeto, com uma estimativa de tempo para cada etapa.


## Referências
- Gomez Chavez, A.; Ranieri, A.; Chiarella, D.; et al. CADDY Underwater Stereo-Vision Dataset for Human–Robot Interaction (HRI) in the Context of Diver Activities. J. Mar. Sci. Eng. 2019, 7, 16.
- Chiarella, D. Towards Multi-AUV Collaboration and Coordination: A Gesture-Based Multi-AUV Hierarchical Language and a Language Framework Comparison System. J. Mar. Sci. Eng. 2023, 11, 1208.
