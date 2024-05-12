# `Estimação Estéreo de Pose Corporal 3D`
# `3D Stereo Body Pose Estimation`

-[]Escrever com menos abstração. Para alguém do primeiro ano de graduação  

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, 
oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em duplas ou trios.
> |Nome  | RA | Curso|
> |--|--|--|
> | Nome1  | 123456  | Mestrado em xxxx|
> | Nome2  | 123456  | Graduação em xxx|
> | Nome3  | 123456  | xxxx|

Nome|RA|Curso
-|-|-
Elton Cardoso do Nascimento|233840|Mestrado em Engenharia Elétrica - Área de Concentração AE: Engenharia de Computação
Leonardo Rener de Oliveira|201270|Mestrado em Engenharia Elétrica - Área de Concentração AE: Engenharia de Computação


## Descrição do Projeto
> Descrição resumida do projeto.
> Qual problema vocês pretendem solucionar?

Estimação de pose corporal é uma técnica amplamente utilizada em diversas indústrias como cinema e jogos, e se baseia na detecção de keypoints específicos no corpo de uma pessoa. Pode ser realizada desde utilizando equipamentos mais complexos e custosos como sistemas de mocap (motion capture), quanto por sensores mais simples como IMU (unidades de medição inercial), ou, utilizando IA (inteligência artificial), usando imagens de câmeras. [REFERÊNCIAS]

O objetivo deste projeto é estimar a posição corporal no espaço 3D de uma pessoa, utilizando uma câmera estéreo (dipositivo com várias câmeras). Mais especificamente, este projeto utilizará uma "OAK-D", dipositivo desenvolvido para aplicações de visão computacional que possui três câmeras, duas laterais monocromáticas, global shutter e 720p; e uma central colorida, rolling shutter e 4K. A câmera se comunica com o computador através de um cabo USB-C, e também possui integrado processadores para execução de pipelines de processamento visual e IA [1].


## Metodologia
> Proposta de metodologia informando quais técnicas pretende-se explorar, como por exemplo: aprendizado supervisionado, geração de dados sintéticos, clusterização, etc. Para a primeira entrega, descreva de maneira mais genérica que tipo de abordagem seu grupo pretende realizar.

Nossa proposta é utilizar um modelo detector de keypoints 2D pronto e utilizá-lo como um extrator de features, removendo as últimas camadas, executando-o uma vez em cada entrada e concatenado as features obtidas, que serão usadas de entrada para uma rede treinável que deverá estimar as posições dos pontos no espaço 3D. O treino será realizado de forma supervisionada. Serão exploradas arquiteturas densas e CNNs.

A avaliação será quantitativa com os dados sintéticos, comparando a solução obtida com o ground truth e a triangularização. A avaliação será no espaço métrico 3D, visto que desejamos estimar de fato a posição absoluta de cada junta, e utilizando como métrica a soma do erro quadrático médio (MSE) de cada keypoint. Entre aspectos não determinados, keypoints não disponíveis em nenhuma das 3 imagens poderão ser mascarado; e como métrica alternativa pensamos em explorar o erro absoluto médio (MAM), para diminuir problemas com outliers. Para comparação, utilizaremos uma triangularização não-linear.

Também será realizada uma avaliação qualitativa do modelo com dados reais da câmera, procurando irregularidades visuais entre o movimento obtido e gravado.

## Bases de Dados e Evolução
> Elencar bases de dados candidatas a serem utilizadas no projeto.

Os dados serão sintetizados utilizando o motor de jogos Unity, que possui desenvolvido o pacote "Perception" para a geração de dados sintéticos [2]. Ela permitirá simular a configuração do dispositivo real e aplicando randomizações que julgarmos necessárias, tentando mitigar os efeitos da mudança do domínio virtual para real. Para a geração de "pessoas virtuais" utilizaremos o pacote "SyntheticHumans" [3].

São planejadas as randomizações: 
- Geração procedural de "pessoas virtuais"
- Pose da ‘pessoa virtual’
- Ruído aditivo na pose dos sensores
- Motion blur
- Texturas de fundo
- Oclusão 
- Luz
- Parâmetros intrínsecos das câmeras (foco)


Cada entrada no conjunto de dados será composto de três imagens, uma para cada câmera, com apenas uma pessoa em cena e keypoints no espaço 2D e 3D anotados para cada câmera. Outros metadados para análise poderão ser obtidos. Poderemos gerar quantos dados forem necessários, mas iremos começar gerando um dataset de por volta de 10000 entradas. As imagens serão salvas em formato PNG, enquanto que outros dados serão em arquivo JSON. 

Em adição a este conjunto, coletaremos também para avaliação um dataset de imagens reais não anotadas com a OAK-D, também com uma pessoa em cena em diferentes posições.

## Ferramentas
> Ferramentas e/ou bibliotecas a serem utilizadas (com base na visão atual do grupo sobre o projeto).

- ![Unity](https://img.shields.io/badge/Unity-100000?style=for-the-badge&logo=unity&logoColor=white) Unity para geração de dados sintéticos 
- ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) PyTorch para treino de modelos.

## Principais desafios
> Principais desafios que se espera encontrar ao longo do desenvolvimento do projeto.

O maior problema a ser enfrentado será a transferência do modelo do domínio sintético para o real, o que poderá levar a necessidade iterativa de diversificação das imagens geradas. A avaliação do modelo no domínio real também será um desafio. Um terceiro problema será a arquitetura exata do modelo que iremos criar.

## Cronograma
> Proposta de cronograma. Procure estimar quantas semanas serão gastas para cada etapa do projeto.

O projeto está dividido em 7 etapas distribuídas nas 9 semanas da disciplina:

Etapa|1|2|3|4|5|6|7|8|9
-|-|-|-|-|-|-|-|-|-
1-Geração de dados||![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)|![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)
2-Modelo pré-treinado||||![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)
3-Modelo||||![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)|![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)
4-Apresentação Preliminar||||||![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)
5-Métricas e Baseline||||||![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)
6-Refinamento|||||||![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)|![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)
7-Documentação e Apresentação||||||||![](https://img.shields.io/badge/-a?style=for-the-badge&logoColor=green)|

1. Geração de dados: geração de dados sintéticos utilizando a Unity.
2. Modelo pré-treinado: busca e preparo do modelo pré-treinado que será utilizado.
3. Modelo: exploração arquitetural e hiperparamétrica do modelo que será treinado.
4. Apresentação Preliminar: preparação da apresentação preliminar para a disciplina.
5. Métricas e Baseline: implementação de métricas e baseline para comparação.
6. Refinamento: refinamento do modelo e dados.
7. Documentação e apresentação: documentação do projeto e preparação da apresentação para a disciplina.



## Referências
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.

[1] “OAK-D — DepthAI Hardware Documentation 1.0.0 documentation.” Acesso em: 12 de maio de 2024. [Online]. Disponível em: https://docs.luxonis.com/projects/hardware/en/latest/pages/BW1098OAK/
[2] S. Borkman et al., “Unity Perception: Generate Synthetic Data for Computer Vision”. arXiv, 19 de julho de 2021. doi: 10.48550/arXiv.2107.04259.
[3] “Unity-Technologies/com.unity.cv.synthetichumans: A package for creating Unity Perception compatible synthetic people.” Acesso em: 12 de maio de 2024. [Online]. Disponível em: https://github.com/Unity-Technologies/com.unity.cv.synthetichumans