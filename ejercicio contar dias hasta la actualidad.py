dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def dia_del_año(ano, mes, dia):
    dias = sum(dias_mes[0:mes - 1]) + dia
    if mes > 2 or (mes == 2 and dia > 28):
        if ((ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0))):
            dias += 1
        return dias
    print(dias)   
    
dia_del_año(2020,2,28)
    