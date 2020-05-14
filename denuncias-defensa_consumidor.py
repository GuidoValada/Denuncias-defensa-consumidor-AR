import csv

def denuncias_rubro(denuncias):

    rubros={}
    listado = ""

    for denuncia in denuncias:
        rubro = '-'.join(denuncia['rubro'].split())
        if  rubro not in rubros:
            rubros[rubro] = 1
        else:
            rubros[rubro] += 1

    for rubro in rubros:
        listado += (' '.join(rubro.split('-')) + ': ' + str(rubros[rubro])+ '\n')

    return listado

def denuncias_rubro_motivo(denuncias):

    rubros = {}
    listado = ""

    for denuncia in denuncias:
        rubro = '-'.join(denuncia['rubro'].split())
        motivo = denuncia['motivo_denuncia']
        if  rubro not in rubros:
            rubros[rubro] = {'CANTIDAD-DENUNCIAS':0}
        else:
            rubros[rubro]['CANTIDAD-DENUNCIAS'] += 1
            if motivo not in rubros[rubro]:
                rubros[rubro][motivo] = 1
            else:
                rubros[rubro][motivo]  += 1
    
    for rubro in rubros:
        listado += (' '.join(rubro.split('-')) + '\n')
        for motivo in rubros[rubro]:
            listado += (' '.join(motivo.split('-')) + ': ' + str(rubros[rubro][motivo]) + '\n' )
        listado += ('\n')

    return listado


with open ('denuncias-defensa-del-consumidor.csv',newline='',encoding="utf8") as f:

    denuncias =list(csv.DictReader(f))


    rubros_file = open('denuncias_rubro.txt','w')
    rubros_file.write(denuncias_rubro(denuncias))
    rubros_file.close()

    motivo_file = open('denuncias_motivo.txt','w')
    motivo_file.write(denuncias_rubro_motivo(denuncias))
    motivo_file.close()
    
    f.close()




    



    

    


    

    





    
    
    
    
    
    
    
    
    
    
    