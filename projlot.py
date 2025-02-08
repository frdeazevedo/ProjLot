import argparse

parser = argparse.ArgumentParser()
parser.add_argument("vagas", help="Arquivo .txt com as lotacoes e a quantidade de vagas disponíveis")
parser.add_argument("opcoes", help="Arquivo .txt com a ordem de preferência dos candidatos")
args = parser.parse_args()

def getIndiceLotacao(lotacoes, nome):
    i = 0
    for l in lotacoes:
        if(l.nome == nome):
            return i
        i += 1
    raise Exception("Lotacao nao encontrada")

class Lotacao:
    def __init__(self, nome, vagas):
        self.nome = nome
        self.vagas = vagas
        self.vagas_disponiveis = vagas

    def temVaga(self):
        return self.vagas_disponiveis > 0

    def preencherVaga(self):
        if(self.vagas_disponiveis > 0):
            self.vagas_disponiveis -= 1
            return self.vagas_disponiveis
        else:
            return -1
    
    def liberarVaga(self):
        if(self.vagas_disponiveis+1 <= self.vagas):
            self.vagas_disponiveis += 1
            return self.vagas_disponiveis
        else:
            return -1

class Candidato:
    def __init__(self, nome, posicao, ranking_lotacoes):
        self.nome = nome
        self.posicao = posicao
        self.ranking_lotacoes = ranking_lotacoes
        self.lotacao = Lotacao("Nenhuma", 0)
        self.prioridade_lotacao = 0

vagas_lotacoes = []

with open(args.vagas, encoding="UTF-8") as f_vagas:
    for v in f_vagas:
        vsplit = v.rstrip("\n")
        vsplit = vsplit.split(",")
        vagas_lotacoes.append(Lotacao(vsplit[0], int(vsplit[1])))

candidatos = []

with open(args.opcoes, encoding="UTF-8") as f_opcoes:
    for o in f_opcoes:
        osplit = o.rstrip("\n")
        osplit = osplit.split(",")
        pos = osplit[0]
        nome = osplit[1]
        ordem_pref = []

        for ordem in range(2, len(osplit)):
            ordem_pref.append(osplit[ordem])

        candidatos.append(Candidato(nome, int(pos), ordem_pref))

ranking = sorted(candidatos, key=lambda candidato: candidato.posicao)

for candidato in ranking:
    num_opcao = 0
    for opcao in candidato.ranking_lotacoes:
        try:
            num_opcao += 1
            ind_lot = getIndiceLotacao(vagas_lotacoes, opcao)
            if(vagas_lotacoes[ind_lot].temVaga()):
                candidato.lotacao = vagas_lotacoes[ind_lot]
                candidato.prioridade_lotacao = num_opcao
                vagas_lotacoes[ind_lot].preencherVaga()
                break
        except:
            candidato.lotacao = Lotacao("Nenhuma", 0)
            break

for c in ranking:
    print(str(c.posicao) + ") " + c.nome + " lotado(a) em " + c.lotacao.nome + ", sua lotacao de prioridade " + str(c.prioridade_lotacao))
