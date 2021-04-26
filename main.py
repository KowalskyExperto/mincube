import numpy as np
import pandas as pd

def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]


def IndicesLaticce(cubo):
    """ 
    Genera una lista con los indices de la lattice del cubo
    """
    indices=list(cubo.columns.values)
    no_deseados=['Cuboid','M']
    
    for i in no_deseados:
        indices.remove(i)
    
    lattice= potencia(indices)
    lattice.remove([])
    return lattice

def GenerarCuboide(lst,cubo):
    indice= "".join(lst)
    
    cuboide=cubo.loc[cubo.loc[:, 'Cuboid'] == indice]
    print('\n Cuboide Generado: \n',cuboide)
    cuboide=cuboide.reset_index()
    return cuboide
        

def AgregarBSTIndex(cubo):
    ceros=[1]*(cubo.shape[0])
    cubo = cubo.assign(BSTi = ceros)
    return cubo

def IndicesHijos(indices):
    indices=potencia(indices)
    indices.remove([])
    indices.pop()
    return indices

# def IdentificarBST(p):
#     for (colname,colval) in p.iteritems():
#         print(colname, colval.values)
        


def GenerarCTIndex(q,R,indices,cubo):
    
    hijos=IndicesHijos(indices)
    cuboideBST = pd.DataFrame(columns=cubo.columns)
    
    
    print('hijos=', hijos)
    if hijos != []:
        for i in hijos:
            p=GenerarCuboide(i, cubo)
            ceros=[0]*(p.shape[0])
            p = p.assign(CTi = ceros)
            #p = p.assign(BSTi = ceros)
            #IdentificarBST(p)
            print("******************Cuboide hijo****************************")
            print(p)
            print (cuboideBST)
            print("**********************************************")
    
    return cubo
    
    

    
    

    
def main():
    #/////////////////////////////////////////////////////////////////////////////
    cubo = pd.read_excel('CuboEjemplo.xlsx')

    print('\n Cubo: \n', cubo)
    indices=IndicesLaticce(cubo)
    print("\n Indices de la lattice: \n",indices)
    cubo.groupby(['Cuboid'])


    R=GenerarCuboide(indices[len(indices)-1],cubo)
    R=AgregarBSTIndex(R)
    print ('\n R: \n', R)

    for i in indices: #Itera en forma Buttom Up
        q=GenerarCuboide(i,cubo)#Genera el cuboide de dimensiones i
        CTI=GenerarCTIndex(q,R,i,cubo)


if __name__ == '__main__':
    main()
    



