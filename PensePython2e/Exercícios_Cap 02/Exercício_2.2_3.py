#03.Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro),
# então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo
# usado em primeiro lugar, que horas chego em casa para o café da manhã?

#Entrada

tempo_passo_medio = (8 * 60 + 15) * 2
tempo_passo_rapido = (7 * 60 + 12) * 3
tempo_saída = (6 * 3600) + (52 * 60)

#Processamento

tempo_de_corrida = tempo_passo_medio + tempo_passo_rapido
tempo_chegada = tempo_saída + tempo_de_corrida
transformar_hora = tempo_chegada // 3600
transformar_minuto = (tempo_chegada % 3600) // 60

#Saída

print('A hora de chegada foi as {}:{}'.format(transformar_hora,transformar_minuto))
