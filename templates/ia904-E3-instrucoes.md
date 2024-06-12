# IA904 - Projeto - Entrega final (E3)

O objetivo desta disciplina é fazer com que os alunos tentem resolver um problema real utilizando técnicas de visão computacional.

## Entrega Final

A entrega final do projeto consiste em duas etapas:
* Apresentação do Projeto a ser realizada em sala de aula no dia 25/06, em ordem de apresentação a ser comunicada no ambiente Classroom da disciplina. A apresentação valerá 1,0 ponto da nota final do projeto.
* Atualização do repositório GitHub já criado anteriormente. A versão final do repositório será avaliada, valendo 5,0 pontos da nota final do projeto.

De maneira análoga à entrega E2, a atualização do repositório GitHub inclui:
* Atualização do arquivo README.md do projeto incluindo as seções do template fornecido ([IA904-E3-template.md](https://github.com/Disciplinas-FEEC/IA904-2024S1/blob/main/templates/ia904-E3-template.md)).
* Após a finalização da edição do conteúdo da terceira entrega, atribuição da tag de release `IA904_E3` no repositório de origem.
* **Pull request** do projeto no **branch  principal** até a data de entrega.

## Datas Importantes

* 25/06 (10:00) - Data limite para pull request do repositório do projeto (será considerada a última versão até essa data e horário).
* 25/06 (16:00) - Apresentação de grupos - 15 minutos por grupo.

**Presença obrigatória de todos os membros do grupo na data de apresentação.**

## Instruções para a Apresentação

Diretrizes para apresentação (sugestões de tópicos):
* Deve recapitular a motivação e o objetivo inicial do projeto
* Abordagem adotada
* Principais ferramentas, bibliotecas e ambientes utilizados (incluir informações úteis para que outros possam utilizá-los)
* Resultados obtidos
* Discussão dos resultados
* Conclusões / Lições aprendidas
* Trabalhos futuros

DICA: Considerem no máximo 1 slide por minuto. Portanto, uma apresentação de 15 minutos não deve ter mais de 15 slides.

## Estrutura do repositório

A fim de uniformizar os repositórios de projetos da disciplina, os diretórios de seu repositório deverão ser nomeados e utilizados segundo a estrutura sugerida a seguir.

Note que nem todos os diretórios ou arquivos serão necessários para todos os projetos. Foque em seguir o padrão para os diretórios que forem necessários. Não crie diretórios que não serão utilizados.

~~~
├── README.md          <- apresentação do projeto
│
├── data               <- deve conter o "datasheet" para os datasets utilizados
│   ├── processed      <- dados finais usados para a modelagem
│   ├── interim        <- dados intermediários, e.g., resultado de transformação
│   └── raw            <- dados originais sem modificações
│
├── notebooks          <- Jupyter notebooks ou equivalentes
│
├── src                <- fonte em linguagem de programação (e.g., C++)
│   └── README.md      <- instruções básicas de instalação/execução
│
└── assets             <- mídias usadas no projeto
~~~

## `README.md`

Para a entrega E3, o README.md do repositório deve ser formatado [segundo o modelo disponibilizado neste link](https://github.com/Disciplinas-FEEC/IA904-2024S1/blob/main/templates/ia904-E3-template.md).

> Tudo o que aparecer neste modo de citação no modelo disponibilizado se refere a algo que deve ser substituído pelo indicado. 

Caso não tenha experiência com edição em Markdown, vide referência: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).
Existem também múltiplas ferramentas para edição de Markdown como, por exemplo, [StackEdit](https://stackedit.io/).

## `data`

Dados utilizados no projeto respeitadas as possíveis implicações éticas, se você tiver licença para tal e se o volume for suportado pelo GitHub. Você pode optar por colocar um subconjunto ilustrativo dos dados.

É importante que sejam colocados os dados originais (se for possível) para garantir a reprodutibilidade do processo. Dados originais são colocados na subpasta `raw`. Dados intermediários devem ser colocados na pasta `interim`. Coloque os dados finais que serviram de entrada para as suas análises na subpasta `processed`.

Ainda, como indicado nos materiais de apoio do Classroom (Reprodutibilidade em pesquisa computacional - Dados), você deve criar um "datasheet" para os datasets utilizados e colocá-lo na pasta `data`.

## `notebooks`

Código do seu projeto que pode ser executado online sem instalação de software, tal como um notebook em Jupyter ou equivalente.

## `src`

Código em alguma linguagem ou projeto em Orange, Weka e similares.

Se for código em linguagem de programação, tente organizá-lo de forma que seja simples a sua execução por terceiros, por exemplo, acrescente as bibliotecas necessárias etc. Acrescente na raiz um arquivo `README.md` com as instruções básicas de instalação e execução.

## `assets`

Qualquer mídia usada no seu projeto: vídeo, ilustrações, arquivos PDF etc.


