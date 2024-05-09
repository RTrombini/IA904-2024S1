# Leitor de Sinais de Mão de Mergulhadores
# Diver Hand Signal Reader

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em duplas ou trios.
> |Nome  | RA | Curso|
> |--|--|--|
> | Raphael Melloni Trombini  | 271322 | Aluno Especial|
> | Ícaro Dias dos Santos   | 245542  | Doutorado em yyyy|
> | Nome3  | 345678  | Graduação em zzzz|

## Descrição do Projeto
O objetivo deste projeto é desenvolver um sistema capaz de identificar e interpretar sinais de mão de mergulhadores, utilizando técnicas de visão computacional, para facilitar a comunicação subaquática e melhorar a segurança durante mergulhos. Este trabalho se inspira e busca contribuir para os objetivos do projeto CADDY, um projeto da União Europeia focado no desenvolvimento de tecnologias para entender e interagir com mergulhadores em ambientes subaquáticos. Os principais objetivos do CADDY incluem a compreensão do comportamento do mergulhador através da interpretação de gestos manuais simbólicos e outros indicadores não verbais, além do desenvolvimento de sistemas cognitivos de (re)planejamento de missões com base nessas interações. O projeto também explora a integração com o 'Caddian corpus', um conjunto extenso de comandos sintaticamente e semanticamente corretos dentro da linguagem hierárquica multi-AUV denominada Caddian, que foi especialmente desenvolvida para o projeto CADDY. Este corpus serve como base para o entendimento e a interpretação das interações subaquáticas, contendo desde comandos simples até sequências mais complexas de gestos.

## Metodologia
Estamos considerando duas abordagens principais para o desenvolvimento do sistema: uma envolve a detecção de mãos seguida pela classificação dos gestos a partir das regiões de interesse (ROI) detectadas; a outra explora o uso de modelos de detecção e classificação integrados, como YOLO. A escolha final dependerá de análises de viabilidade, considerando as características do dataset disponível, que atualmente está no formato CSV, e a necessidade de eventualmente converter este dataset para um formato adequado como COCO para modelos como YOLO. Adicionalmente, consideraremos a necessidade de um pré-processamento das imagens para melhorar a visibilidade em condições subaquáticas desafiadoras, como baixo contraste, águas turvas e iluminação variada. Estamos abertos a explorar a abordagem que melhor se encaixe às necessidades e limitações do projeto.

## Bases de Dados e Evolução
Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
CADDY Underwater Gestures Dataset | [CADDY Dataset Homepage](http://caddy-dataset.org) | Conjunto de dados composto por 10.000 pares de imagens estéreo coletadas em 8 cenários diferentes para interação subaquática humano-robô. As imagens foram capturadas durante experimentos que simulam diversas condições e tarefas subaquáticas, com o objetivo de desenvolver e testar sistemas de reconhecimento de gestos que facilitam a comunicação entre mergulhadores e veículos autônomos subaquáticos (AUVs). Cada cenário reflete um contexto específico de mergulho, variando desde ambientes com visibilidade reduzida até situações com iluminação artificial, projetados para desafiar e aprimorar a capacidade dos sistemas robóticos em entender e reagir a comandos humanos no ambiente subaquático.

## Ferramentas
As principais ferramentas a serem utilizadas incluem Python, PyTorch, OpenCV para processamento de imagens, e possivelmente TensorFlow/Keras.

## Principais desafios
Os principais desafios incluem a variação das condições de iluminação subaquática, a qualidade das imagens e a precisão na detecção dos gestos em ambientes complexos. Além disso, as luvas Caddian, usadas nos testes do projeto CADDY, apresentam um design customizado com símbolos e cores para facilitar a detecção por Veículos Autônomos Subaquáticos (AUVs). Este design pode aumentar o risco de overfitting do modelo, limitando sua aplicabilidade em condições normais, sem luvas especiais. Será crucial avaliar a generalidade do modelo e explorar estratégias para adaptá-lo a um uso mais amplo, sem depender dessas características específicas das luvas.

## Cronograma
- Semanas 1-2: Revisão de literatura e definição das ferramentas.
- Semanas 3-4: Preparação dos dados e desenvolvimento do modelo inicial.
- Semanas 5-6: Treinamento e ajustes do modelo.
- Semanas 7-8: Testes finais e preparação da apresentação.

## Referências
- Gomez Chavez, A.; Ranieri, A.; Chiarella, D.; et al. CADDY Underwater Stereo-Vision Dataset for Human–Robot Interaction (HRI) in the Context of Diver Activities. J. Mar. Sci. Eng. 2019, 7, 16.
- Chiarella, D. Towards Multi-AUV Collaboration and Coordination: A Gesture-Based Multi-AUV Hierarchical Language and a Language Framework Comparison System. J. Mar. Sci. Eng. 2023, 11, 1208.
