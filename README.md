# Explicando o Algoritmo
Itera sobre a lista de candidatos, classificados em ordem de convocação, do primeiro ao último colocado. Para cada candidato, itera sobre a lista de lotações em ordem de preferência (da mais preferida a menos preferida), se a lotação tiver vaga disponível, preenche o candidato nessa lotação e passa-se ao próximo candidato.

# Formato dos Arquivos de Entrada
## Arquivo de Lotações e Vagas
O arquivo que contém as lotações e suas respectivas vagas deve ser formatado com o seguinte padrão:
* Cada linha corresponde a uma lotação
* Em cada linha deve-se preencher o nome da lotação, seguida do símbolo de vírgula e da quantidade de vagas daquela lotação

Exemplo:
```
Florianópolis,10
Vitória,8
Recife,5
Salvador,9
João Pessoa,12
Coordenação de Administração,1
```

No exemplo acima, tem-se 10 vagas em Florianópolis, 8 vagas em Vitória, 5 vagas em Recife, etc.

## Arquivo de Candidatos e Opções de Vagas
O arquivo que contém a lista de candidatos e suas opções de vagas (ordem de preferência) deve ser formatado com o seguinte padrão:
* Cada linha corresponde a um candidato
* Em cada linha deve-se preencher com a seguinte ordem de informações, separadas por vírgula (sem espaço): ordem de convocação,nome do candidato,opção 1,opção 2,opção n

Exemplo:
```
1,João,João Pessoa,Vitória,Recife,Salvador,Florianópolis,Coordenação de Administração
2,Maria,João Pessoa,Coordenação de Administração,Vitória,Salvador,Florianópolis,Recife
3,José,Florianópolis,João Pessoa,Recife,Vitória,Coordenação de Administração,Salvador
```

No exemplo acima, o candidato João será o 1º convocado e sua ordem de preferência de lotações é a seguinte: 1º) João Pessoa; 2º) Vitória; 3º) Recife; 4º) Salvador; 5º) Florianópolis; 6º) Coordenação de Administração.
