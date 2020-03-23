#22.Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
#hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
#máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
#seguinte.

def main():
    print('Digite as horas e comfirme, em seguida digite os minutos de início e fim do jogo\n')

    hora_inicio = int(input('Digite a hora de início do jogo:'))
    min_inicio = int(input('Digite os minutos de início do jogo:'))
    print(f'O jogo iníciou às {hora_inicio}:{min_inicio}.\n')

    hora_fim = int(input('Digite a hora de fim do jogo:'))
    min_fim = int(input('Digite os minutos de fim do jogo:'))
    print(f'O jogo acabou às {hora_fim}:{min_fim}.')

    print(duração_jogo(hora_inicio, min_inicio, hora_fim, min_fim))


def duração_jogo(hora_inicio, min_inicio, hora_fim, min_fim):
    hora_inicio += min_inicio // 60
    hora_fim += min_fim // 60

    total_horas = hora_fim - hora_inicio
    total_min = min_fim - min_inicio

    if hora_inicio >= 0  and hora_inicio < 24 and hora_fim >= 0 and hora_fim < 24:
        if total_min >= 0:
            print(f'\nO jogo durou: {total_horas}:{total_min} ')

        else:
            total_horas -= 1
            total_min += 60

            if total_horas >= 0:
                print(f'\nO jogo durou: {total_horas}:{total_min} ')

    else:
        print('\nO jogo ultrapasou seu tempo limite!!!')

main()




