#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import os

class Node:
    right = None
    left = None
    variavel = ""
    tipo = 0
    valor = 0

    def __init__(self,tipo,variavel,valor):
        self.tipo, self.variavel,self.valor = tipo, variavel, valor 
        self.right = None
        self.left = None 

    def insert(self,tipo,variavel,valor):
        if(self != None):
            if(valor < self.valor ):
                print ("inserindo no filho esquerdo de %d" %(self.valor))
                try:
                    self.left.insert(tipo,variavel,valor)
                except:
                    self.left = Node(tipo,variavel,valor)
            if (valor > self.valor):
                try:
                    self.right.insert(tipo,variavel,valor)
                except:
                     self.right = Node(tipo,variavel,valor)


    def run_left(self,node):

        if (node != None):
            print ("var=%s tipo = %d valor=%d" % (self.variavel,self.tipo,self.valor))
            #try:
            if (self.left != None):
                self.left.run_left(node.left)
        #        try:
            if (self.right != None):
                self.right.run_left(node.right)
#            except:
#            except: 
                


def busca(query, prop):
    index = -1
    i=0
    while i < len(prop) and (index == -1):
        if(prop[i] == query):
        #   print ('query %s encontrada' %(query))
            index = i
        i+= 1
    return index

def SilogismoHipotetico(expr, proposicoes):
    p_i,q_i, flag  =  separe(expr)
    p_i = p_i.replace(" ", "")
    q_i = q_i.replace(" ", "")
    index_expr = proposicoes.index(expr)
    p_j , q_j, flag_j =  "","",255
    index_p_j = -1
    expr_pi_qj = ""
    resp = 0
    #os.system("sleep 1")

    if ( flag  == -1):
        for  i in range ( len(proposicoes) -1):
            if (i != index_expr ) :
                p_j,q_j, flag_j = separe(proposicoes[i])
                p_j = p_j.replace(" ", "")
                q_j = q_j.replace(" ", "")    
               # print ('pi = %s  -> qi= %s\n pj  %s  -> qj = %s' % (p_i,q_i,p_j,q_j) )
             #   print ('proposicoes =', proposicoes)
 #              
                #print  ("i = %d  index_expr = %d flag_j = %d" %(i, index_expr,  flag_j))
                if ( flag_j == -1):
                    if (q_i == p_j):
                        index_p_j = i 
                        break
        if ( index_p_j > -1):        # se existe uma expressao tal que pi -> qi , pj ->qj  , qi = pj
            expr_pi_qj = p_i +  '-> ' +  q_j
            print ("SH (%d , %d)\t (%s), (%s)\n\t\t____________________ \n.:.\t\t\t%s " %(index_expr, index_p_j,proposicoes[index_expr],proposicoes[index_p_j],expr_pi_qj ))
            
            del proposicoes[index_expr]
            del proposicoes[index_p_j -1]
            proposicoes.append(expr_pi_qj)
           # print ("POS SH =" , proposicoes)
            resp = 1






    return resp

#aplica modus ponens e retorna verdadeiro se sucesso, ou falso
def NaoExpr(expr):
    p, q  = separe(expr)
    return false 
    
def modusPones(expr, proposicoes):

    p,q ="",""
    index=-2
    index_p=-2
    flag = 0
    lst=[]
    operador = -2
    tipo = 255
#    print (proposicoes)
    if ( len (proposicoes) > 0):
        p,q, tipo = separe(expr)

        lst = p.split()
        p=""
        if ( len (lst) == 1):
            p = lst[0]
        else:
            for i in range (len(lst)):
                print ("")


       # print ("pk = %sqk =%s" %(p,q))
        q = q.replace(" ","")
        #print (q)
        index = busca(q,proposicoes)
        #print ("index=", index)
        if (index > -1):
            
            index_p = busca(expr,proposicoes)
            

            if (index_p > -1):
                print ("MP (%d, %d) \t%s, %s\n\t\t____________________\n.:.\t\t%s" %(index_p,index,proposicoes[index_p],q,p))
                del proposicoes[index]
                del proposicoes[index_p -1]
                proposicoes.append(p)
                flag = 1
                


    return flag


def modusTolens(expr, proposicoes):


    p, q , tipo = "", "",255
    p1,q1,tipo1 = "","",255
    P2,q2,tipo2="","",255
    valor=1024
    nivel = 1
    arvore = None
    flag = 0
    if ( len (proposicoes) > 0):
        p,q, tipo = separe(expr)
        index_p = proposicoes.index(expr)
        # se for uma expressão do tipo p -> q
        if ( tipo == -1):
            #faça a quebra de p em p1,q1 e q em p2,q2
            index = -255 
            p1,q1,tipo1 = separe(p)
            p2,q2,tipo2 = separe(q)
            q_aux = "(" + q + ")'"
            q_aux =   q_aux.replace(" ","")
          #  print (q_aux)
            index = busca(q_aux,proposicoes)

            if ( index  > -1):
                p_aux = "(" + p.replace(" ","") + ")'"
                print ("MT (%d , %d) \t%s, %s\n\t____________________\n.:.\t\t%s" %(index_p,index,expr,q_aux,p_aux) )
                del proposicoes[proposicoes.index(expr)]
                del proposicoes[index -1 ]
                proposicoes.append(p_aux)
                print (proposicoes)
                flag = 1





        # é uma expressão do tipo p + q
        if (tipo == 0):
            p1,q1,tipo1 = separe(p)
            p2,q2,tipo2 = separe(q)

        #  é uma expressão do tipo p . q
        if (tipo == 1):
            p1,q1,tipo1 = separe(p)
            p2,q2,tipo2 = separe(q)


    return flag

def token (input):
    tokens = re.compile("[()a-z+.->']")
    teste = None
    i = 0
    #print ("input=",input)
    while  i < len(input):
        teste = tokens.match(input[i])
        if (teste == None):
            print ( "Token inválido em  i= %d input [ %s ]\n"  % (i,input[i]) )
            exit(1)
        i+=1





def separe(prop):
    p,q,flag = "","",256
    try:
        #lst = prop.split("->")
        #aux = lst[0].split(" ")
        #print aux
        p, q = prop.split("->")
        flag = -1
    except :
        try:
            p,q =  prop.split(".")
            flag = 0
        except :
            try:
                p,q =  prop.split("+")
                flag = 1
            except :
                query = re.compile("[(a-z)]'*") # expressão regular para variavel e variavel negada 
                teste = query.match(prop)
                flag = 2
                if (teste !=  None):
                    #print ("somente variavel or not variable ")
                    p = prop

    return p , q , flag 
def parse(proposicoes):
    flag = 0
    tipo = 255
    P,Q= [],[]
    p,q="",""
    for i in range(len(proposicoes)):
        #print ("parseando", i)
        p, q , tipo = separe(proposicoes[i])
        P.append(p)
        Q.append(q)

    return P,Q

def resolve(proposicoes,resp):
    i= 0
    flag = -1
    k = 0
    while (len(proposicoes) > 1):
        for i in range (0,len(proposicoes) -1):
          #  print ("restando" , proposicoes)
           # print ("tentando modus pones") 
            flag = modusPones(proposicoes[i],proposicoes)
            if(flag == 0):
            #    print ("tentando modus tolens")
                flag = modusTolens(proposicoes[i],proposicoes)
                if ( flag == 0):
             #       print ("tentando silogismo Silogismo Hipotetico")
                    flag = SilogismoHipotetico(proposicoes[i],proposicoes)
        k += 1

        if ( (k  / ( len (proposicoes) + 1 ) == 1000 ) ):
            print("Numero de iteracoes >> que len(proposicoes)\nA expressao não pode ser resolvida com as tecnicas de inferencias programadas :(")
            exit(1)
    #resp=input("Digite a proposição esperada de saída, após  a resolução por prova direta")
    if (resp == proposicoes[0] ):
        print ("\n\ncqd:",  proposicoes )
    else:
        print ("Argumento falho")
    
    #print ("prop=",proposicoes);



    return True




def main():
    str=[]

    aux = "1988"
    resp = ""
    P,Q=[],[]
    print ("Digite cada uma das proposições")
    print("Por último digite o argumento a ser provado!\nE este deve ser iniciado com @, exemplo: @ (s)'")
    while aux != "":
        try:
        
            aux = input("proposicao: \n")
            
            
            if (aux != ''):
                str.append(aux)
        except EOFError:
            aux =""

    try:
        aux,resp = str[len(str) -1].split('@ ')
        resp.replace(" ","")
        #print ("resp=%s" %(resp))
        del str[len(str) -1 ]
        #print ("__main__str=",str)
        
        
    except:
        print("Falta o argumento a ser demonstrado")
        exit(1)
        #print("main(str) =",str)

    token(str)
    P,Q = parse(str)
    resolve(str,resp)
    #print str
    #print ("P = %s" %(P))
    #print ("Q = %s" %(Q))
    #modusPones("a -> c",str)
    #modusTolens("a -> c",str)
    
    
main()