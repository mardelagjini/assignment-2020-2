from sys import argv

#diabasma orismatwn
#exei dosei -c
if argv[1] == "-c":
        cc = True
        rr = False
        RADIUS = -1
        num_nodes = argv[2]
        input_file = argv[3]
#den exei dosei -c
else:
        cc = False
        rr = True
        RADIUS = argv[2]
        num_nodes = argv[3]
        input_file = argv[4]

#metetrepse to keimeno se arithmo
num_nodes = int(num_nodes)
RADIUS = int(RADIUS)

#bres tous kombous
#kenos grafos
G={}
arxeio = open(input_file)
for grammi in arxeio:
        noymera = grammi.split() #pare ta noumera apo ti grammi
        proto = noymera[0] #to proto noumero
        proto = int(proto)
        deutero = noymera[1] #to deutero noumero
        deutero = int(deutero)
        G[proto] = []
        G[deutero] = []
arxeio.close()

arxeio = open(input_file)
komboi = set()
for grammi in arxeio:
        noymera = grammi.split() #pare ta noumera apo ti grammi
        proto = noymera[0] #to proto noumero
        proto = int(proto)
        komboi.add(proto)
        deutero = noymera[1] #to deutero noumero
        deutero = int(deutero)
        komboi.add(deutero)
        G[proto].append(deutero)
        G[deutero].append(proto)
arxeio.close()
#print(G)

#tropopoiimeni prota kata bathos anazitisi ksekinontas apo ton kombo s
def bfs(s):
        q = [] #oura me tous kombous pou exoume parei
        q.append(s) #prosthese ton s, ton pairnoume proto
        makria = {}
        visited = {}
        for kombos in komboi: #oloi oi komboi den exoun epilexthei
                visited[kombos] = False
        makria[s] = 0 #o s einai 0 makria apo ton eauto tou
        visited[s] = True #epileksame proto ton s
        while not len(q) == 0: #oso exei akoma i oura
                protos = q.pop(0) #pare ton proto apo tin oura
                AdjacencyList = G[protos] #pare tous geitones tou
                #print(protos,AdjacencyList)
                for v in AdjacencyList: #gia kathe geitona
                        if visited[v] == False: #den ton exoume epileksei
                                makria[v] = makria[protos] + 1 #apexei 1 parapanw
                                q.append(v) #balton stin oura
                                visited[v] = True #min ton ksanaepileksoume
        return makria

if rr:
        done = [] #poioi komboi exoun bgei
        for i in range(num_nodes):
                CIir = {}
                for i in komboi:
                        makria = bfs(i)
                        #print(makria)
                        sum = 0
                        for j in komboi:
                                if makria[j] == RADIUS: #pare autous stin aktina
                                        kj = len(G[j])
                                        sum = sum + kj - 1
                        ki = len(G[i])
                        CIir[i] = (ki - 1) * sum
                max = -1
                for kombos in komboi:
                        if kombos not in done and max < CIir[kombos]: #den exei bgei kai einai max
                                max = CIir[kombos]
                                max_kombos = kombos
                print(max_kombos, max)
                done.append(max_kombos) #bgike
if cc:
        done = [] #poioi komboi exoun bgei
        for i in range(num_nodes):
                k = {}
                for i in komboi:
                        k[i] = len(G[i])
                max = -1
                for kombos in komboi:
                        if kombos not in done and max < k[kombos]: #den exei bgei kai einai max
                                max = k[kombos]
                                max_kombos = kombos
                        if kombos not in done and max == k[kombos]: #einai mikroteros katonoma
                                if kombos < max_kombos:
                                        max = k[kombos]
                                        max_kombos = kombos
                print(max_kombos, max)
                done.append(max_kombos) #bgike
