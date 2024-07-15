def calculosegundos (hora, minutos, segundos):
    hora = hora * 3600
    minutos = minutos * 60
    segundos = segundos
    res= hora + minutos + segundos
    print(f"O horario digitado tem o total de {res} segundos")

hora = int (input("digite as horas: "))
minutos = int (input("digite os minutos: "))
segundos = int (input("digite os segundos: "))
calculosegundos(hora,minutos,segundos)