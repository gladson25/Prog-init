def main():
    dados = {}
    with open("apache_logs.txt") as l:
        for linha in l:
            linhalist = linha.split()
            #print(linhalist[0], linhalist[9])
            if linhalist[0] in dados:
                dados[linhalist[0]].append(linhalist[9])
            else:
                dados[linhalist[0]] = [linhalist[9]]
    print(dados)

if __name__ == "_main_":
    main()


#l = open(apache_logs.txt, 'r')
#lines = l.readlines()
#for i in lines:
#    s = i.split()
#        print([0:9])