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

    #Transform dict into key-value pair list
    rubros_list = list(rubros.items())
    #sort list using quantity as sorting key parameter/lambda takes each tuple with key-value pair, using indexing to get the value.
    rubros_list.sort(key=lambda cantidad: cantidad[1],reverse=True)
    #returning to dict for printing
    rubros = dict(rubros_list)

    for rubro in rubros:
        listado += (' '.join(rubro.split('-')) + ': ' + str(rubros[rubro])+ '\n')

    return listado

def denuncias_comuna(denuncias):

    comunas={}
    listado = ""

    for denuncia in denuncias:
        comuna = str(denuncia['comuna'])
        if  comuna not in comunas:
            comunas[comuna] = 1
        else:
            comunas[comuna] += 1

    #Transform dict into key-value pair list
    comunas_list = list(comunas.items())
    #sort list using quantity as sorting key parameter/lambda takes each tuple with key-value pair, using indexing to get the value.
    comunas_list.sort(key=lambda cantidad: cantidad[1],reverse=True)
    #returning to dict for printing
    comunas = dict(comunas_list)
    
    for comuna in comunas:
        listado += ('Comuna Nº ' + str(comuna) + ': ' + str(comunas[comuna])+ '\n')

    return listado

def denuncias_comuna_rubro(denuncias):

    comunas = {}
    listado = ""

    for denuncia in denuncias:
        rubro = '-'.join(denuncia['rubro'].split())
        comuna = str(denuncia['comuna'])
        if  comuna not in comunas:
            comunas[comuna] = {}
            comunas[comuna]['CANTIDAD-DENUNCIAS'] = 1
            comunas[comuna][rubro] = 1
        else:
            comunas[comuna]['CANTIDAD-DENUNCIAS'] += 1
            if rubro not in comunas[comuna]:
                comunas[comuna][rubro] = 1
            else:
                comunas[comuna][rubro]  += 1
    
    sorted_comunas = {}

    #Transform dict into key-value pair list
    comunas_list = [list(elem)for elem in list(comunas.items())]

    for comuna in comunas_list:
        rubros_list = list(comuna[1].items())
        #sort list using quantity as sorting key parameter/lambda takes each tuple with key-value pair, using indexing to get the value.
        rubros_list.sort(key=lambda cantidad: cantidad[1],reverse=True)
        #Addin to sorted comunas dict, in original form.
        sorted_comunas[comuna[0]] = dict(rubros_list)
        

    sorted_comunas = list(sorted_comunas.items())
    #Sorting comunas by most complaints
    sorted_comunas.sort(key=lambda cantidad: cantidad[1]['CANTIDAD-DENUNCIAS'],reverse=True)
    sorted_comunas =dict(sorted_comunas)


    for comuna in sorted_comunas:
        listado += ('Comuna Nº: '+ comuna + '\n')
        for rubro in sorted_comunas[comuna]:
            listado += (' '.join(rubro.split('-')) + ': ' + str(sorted_comunas[comuna][rubro]) + '\n' )
        listado += ('\n')

    return listado

def denuncias_rubro_motivo(denuncias):

    rubros = {}
    listado = ""

    for denuncia in denuncias:
        rubro = '-'.join(denuncia['rubro'].split())
        motivo = denuncia['motivo_denuncia']
        if  rubro not in rubros:
            rubros[rubro] = {}
            rubros[rubro]['CANTIDAD-DENUNCIAS'] = 1
            rubros[rubro][motivo] = 1
        else:
            rubros[rubro]['CANTIDAD-DENUNCIAS'] += 1
            if motivo not in rubros[rubro]:
                rubros[rubro][motivo] = 1
            else:
                rubros[rubro][motivo]  += 1
    
    sorted_rubros = {}

    #Transform dict into key-value pair list
    rubros_list = [list(elem)for elem in list(rubros.items())]

    for rubro in rubros_list:
        motivos_list = list(rubro[1].items())
        #sort list using quantity as sorting key parameter/lambda takes each tuple with key-value pair, using indexing to get the value.
        motivos_list.sort(key=lambda cantidad: cantidad[1],reverse=True)
        #Addin to sorted comunas dict, in original form.
        sorted_rubros[rubro[0]] = dict(motivos_list)
        

    sorted_rubros = list(sorted_rubros.items())
    #Sorting rubros by most complaints
    sorted_rubros.sort(key=lambda cantidad: cantidad[1]['CANTIDAD-DENUNCIAS'],reverse=True)
    sorted_rubros =dict(sorted_rubros)



    for rubro in sorted_rubros:
        listado += (' '.join(rubro.split('-')) + '\n')
        for motivo in sorted_rubros[rubro]:
            listado += (' '.join(motivo.split('-')) + ': ' + str(sorted_rubros[rubro][motivo]) + '\n' )
        listado += ('\n')

    return listado


with open ('denuncias-defensa-del-consumidor.csv',newline='',encoding="utf8") as f:

    denuncias =list(csv.DictReader(f))


    rubros_file = open('denuncias_rubro.txt','w')
    rubros_file.write(denuncias_rubro(denuncias))
    rubros_file.close()

    motivo_file = open('denuncias_rubro_motivo.txt','w')
    motivo_file.write(denuncias_rubro_motivo(denuncias))
    motivo_file.close()

    motivo_file = open('denuncias_comuna.txt','w')
    motivo_file.write(denuncias_comuna(denuncias))
    motivo_file.close()

    motivo_file = open('denuncias_comuna_rubro.txt','w')
    motivo_file.write(denuncias_comuna_rubro(denuncias))
    motivo_file.close()
    
    f.close()




    



    

    


    

    





    
    
    
    
    
    
    
    
    
    
    