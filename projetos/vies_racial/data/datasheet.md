# Datasheet

Este documento tem como objetivo fornecer informações sobre a base de dados FairFace.

## Motivação

O conjunto de dados FairFace foi criado com o objetivo de aumentar a representatividade de etnias em conjuntos de dados de imagens faciais. A maioria dos conjuntos existentes possui uma predominância de dados de pessoas brancas, o que dificulta a construção de modelos não enviesados. Dessa forma, o objetivo da base de dados é a inclusão racial, incluindo grupos raciais sub-representados, como latinos e pessoas do Oriente Médio.

Além disso, o conjunto de dados foi organizado por Kimmo Kaarkkainen e Jungseock Joo da Universidade da Califórnia, Los Angeles (UCLA). A criação do FairFace foi financiada pela National Science Foundation da SBE-SMA (Social, Behavioral and Economic Sciences - Office of Multidisciplinary Activities).

## Composição

O conjunto de dados FairFace é composto por instâncias que representam imagens faciais. Ele inclui 108.501 imagens faciais, equilibradas em termos de raça, definindo sete grupos raciais: Branco, Negro, Indiano, Asiático Oriental, Asiático do Sudeste, Oriente Médio e Latino. Além disso, o conjunto de dados é rotulado em nove faixas etárias: 0 a 2, 3 a 9, 10 a 19, 20 a 29, 30 a 39, 40 a 49, 50 a 59, 60 a 69 e maiores de 70 anos, e também por gênero: feminino e masculino.

O conjunto de dados é organizado em sete raças e nove faixas etárias. Embora tenha sido criado para mitigar o viés racial em conjuntos de dados de reconhecimento facial existentes, ele é uma amostra de algumas das etnias existentes no mundo. Existem autores que informam até 20 raças diferentes, além de diversas miscigenações que não foram consideradas. A subjetividade dos anotadores também deve ser levada em conta.

Cada instância no conjunto consiste em imagens faciais brutas e é acompanhada de rótulos que identificam raça, idade e gênero. Não há dados faltantes no conjunto de dados, e as relações entre as instâncias não são explicitadas. As divisões de dados recomendadas incluem um conjunto de treinamento com 86.744 imagens e um conjunto de validação com 10.954 imagens.

Não foram observados erros no conjunto de dados, e ele é autossuficiente, não dependendo de recursos externos. Este conjunto de dados foi derivado do Yahoo YFCC100m, utilizando imagens com Licenças Creative Commons por Atribuição e Compartilhamento pela Mesma Licença, que permitem uso acadêmico e comercial. O conjunto pode ser usado para treinar novos modelos e verificar a precisão balanceada de classificadores existentes.

O FairFace não contém informações confidenciais como dados protegidos por privilégio legal ou confidencialidade médico-paciente. As imagens faciais foram coletadas de fontes públicas como Flickr e Twitter. Não há indicação de que o conteúdo seja ofensivo ou insultante.

O conjunto de dados identifica subpopulações por etnia, idade e gênero. A distribuição das imagens por raça é a seguinte:

|Etnia  | Treino | Validação |
|--|--|--|
| White | 16527 | 2085 |
| Latino Hispanic | 13367 | 1623 |
| Indian | 12319 | 1556 |
| East Asian | 12287 | 1550 |
| Black | 12233 | 1516 |
| Southeast Asian | 10795 | 1415 |
| Middle Eastern | 9216 | 1209 |

E divisão de faixa etária, a quantidade de imagens por faixa segue na tabela:

|Faixa Etária  | Treino | Validação|
|--|--|--|
|0-2 | 1792 | 199|
|3-9 | 10408 | 1356|
|10-19 | 9103 | 1181|
|20-29 | 25598 | 3300|
|30-39 | 19250 | 2330|
|40-49 | 10744 | 1353|
|50-59 | 6228 | 796|
|60-69 | 2779 | 321|
|maior que 70| 842 | 118|

Já a seguinte tabela informa o número de imagens por gênero: 

|Gênero | Treino | Validação |
| -- | -- | -- |
|Masculino | 45986 | 5792 |
|Feminino | 40758 | 5162 |

Já em relação a exposição das pessoas no conjunto de dados, é possível a identificação, já que são fotos dos rostos. Além disso, o conjunto de dados inclui categorias raciais, como Latino e Oriente Médio, e diferencia entre Asiáticos do Leste e do Sudeste, brancos, negros, etc. Essas categorias podem ser consideradas sensíveis, pois revelam origens raciais ou étnicas.

## Processo de Coleta

Os dados do conjunto de dados FairFace foram adquiridos através do Amazon Mechanical Turk, onde trabalhadores anotaram raça, gênero e grupo etário de cada rosto. Para cada imagem, três trabalhadores foram designados. Se dois ou três concordassem, esses valores eram tomados como verdadeiros. Em casos de discordância entre os três, a imagem era republicada para mais três trabalhadores e descartada se ainda houvesse discordância. As anotações iniciais, ainda ruidosas, foram refinadas treinando um modelo a partir dessas anotações iniciais e aplicando-o de volta ao conjunto de dados. Posteriormente, as anotações divergentes das previsões do modelo foram verificadas manualmente.

Os dados foram coletados principalmente do conjunto de dados YFCC-100M do Flickr, que é compartilhado livremente para fins de pesquisa. Outras fontes incluem Twitter e veículos de comunicação online. A estratégia de amostragem inicial envolveu a detecção e anotação de 7.125 faces amostradas aleatoriamente do YFCC-100M. Para evitar a dominância de imagens de pessoas brancas, o número de imagens de cada país foi ajustado, excluindo países dos EUA e da Europa após alcançar um número suficiente de faces brancas.

O artigo que descreve a base de dados foi publicado em 2021, mas as fotos possivelmente foram capturadas em diferentes anos, o que não foi especificado. Não há informações sobre a realização de processos de revisão ética por um comitê de ética institucional. As imagens foram coletadas de fontes públicas, portanto, não houve notificação direta ou consentimento específico dos indivíduos, embora o compartilhamento seja permitido para fins de pesquisa pelo conjunto de dados do Flickr YFCC100M.

Não foi fornecido um mecanismo para os indivíduos revogarem seu consentimento no futuro, e não há menção a uma análise de impacto potencial do conjunto de dados em relação aos sujeitos dos dados, o que é uma preocupação, especialmente por incluir fotos de crianças e adolescentes.

## Pré-processamento/limpeza/rotulagem

O conjunto de dados FairFace passou por um processo de rotulagem, onde cada imagem foi anotada de acordo com a raça, idade e gênero da pessoa. Essa anotação foi realizada através do Amazon Mechanical Turk, onde trabalhadores de crowdsourcing forneceram os rótulos necessários. Não houve pré-processamento adicional, como discretização, tokenização ou extração de características.

Os dados brutos, ou seja, as imagens originais, estão disponíveis e não foram submetidos a pré-processamento antes da rotulagem. Isso permite suporte a usos futuros não previstos, mantendo a integridade das imagens originais.

O software utilizado para a rotulagem inicial foi o Amazon Mechanical Turk, que facilitou a anotação das imagens pelos trabalhadores. O primeiro modelo de anotação utilizado está disponível no site da [Amazon Mechanical Turk](https://www.mturk.com/). No entanto, o segundo modelo utilizado para refinar as anotações não foi publicado ou detalhado na documentação disponível.

## Usos

O conjunto de dados FairFace já foi utilizado para diversas tarefas. Um dos usos foi a comparação do desempenho de modelos treinados a partir de diferentes conjuntos de dados, utilizando a arquitetura ResNet-34. Apesar de haver diversos trabalhos que utilizam o FairFace, não foi encontrado um repositório específico que vincule todos os artigos e sistemas que utilizam esta base de dados.

Além de suas aplicações existentes, o conjunto de dados FairFace poderia ser utilizado para estudar o viés de faixa etária. No entanto, é importante notar que ele é desbalanceado em relação a esta categoria, exigindo ajustes para que os resultados sejam válidos e justos.

Não há elementos específicos sobre a composição do conjunto de dados ou o modo como foi coletado e rotulado que possam comprometer seu uso futuro. No entanto, consumidores de dados devem estar atentos ao potencial desbalanceamento em faixas etárias e tomar medidas adequadas para mitigar qualquer viés que possa surgir.

Por fim, a base de dados não é recomendada para tarefas que requerem um balanceamento preciso de faixas etárias, pois pode introduzir viés nos modelos construídos para classificar essa categoria.

## Distribuição


O conjunto de dados FairFace foi distribuído para terceiros sob a licença Creative Commons de Atribuição e Compartilhamento. Esta licença permite sua utilização tanto para fins acadêmicos quanto comerciais.

A distribuição do conjunto de dados é feita através de um repositório no GitHub, onde ele está disponível para download. Embora o conjunto de dados em si não possua um Identificador de Objeto Digital (DOI), o artigo que o descreve possui um DOI. A base de dados foi disponibilizada publicamente em 2021.

O texto da licença, que pode ser acessado no site associado ao repositório GitHub, detalha os termos de uso e as permissões concedidas para o uso do conjunto de dados. Não foram encontradas restrições impostas por terceiros ou quaisquer taxas associadas a essas restrições para o uso do conjunto de dados.

Além disso, não há controle de exportação ou outras restrições regulatórias aplicáveis ao conjunto de dados ou a instâncias individuais. Assim, os usuários podem acessar e utilizar o conjunto de dados sem preocupações adicionais relacionadas a regulamentos de exportação.

## Manutenção

O conjunto de dados FairFace está hospedado no GitHub, e o responsável por manter e suportar os dados é o Jungseock Joo. Pode-se contatar os responsáveis pelo conjunto de dados através dos e-mails kimmo@cs.ucla.edu, pertencente a Kimmo Karkkainen, e jjoo@comm.ucla.edu, pertencente a Jungseock Joo.

Atualmente, não existe um erratum para a base de dados. O conjunto de dados não será atualizado, portanto, não haverá a necessidade de comunicar atualizações aos consumidores. Também não existem limites aplicáveis à retenção dos dados associados às instâncias, uma vez que não há uma previsão de exclusão dos dados após um período fixo de tempo.

Versões anteriores do conjunto de dados não serão suportadas ou mantidas, visto que não haverá atualizações futuras. Caso outros pesquisadores ou desenvolvedores desejem estender, aumentar, construir sobre ou contribuir para o conjunto de dados, devem solicitar autorização dos responsáveis através dos e-mails fornecidos anteriormente.