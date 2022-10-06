# допустим, в среднем в году 365 дней
uslovie = 8*60/5 #исходя из условия это кол-во экспонатов, которые возможно посмотреть за 1 день
kolvoExponatov,kolvoVremeni = int(input('Количество экспонатов = ')), int(input('Количество лет = ' ))
if kolvoExponatov < 0:
    print('Ошибка, введено неверное значение экспонатов')
elif kolvoVremeni < 0:
    print('Ошибка, введено неверное значение времени')
elif kolvoVremeni==kolvoExponatov==0:
    print('Ошибка, введены неверные значение экспонатов и времени')
if kolvoExponatov > 0 & kolvoVremeni >=0:
    print('Понадобится дней чтобы осмотреть все экспонаты) = ',kolvoExponatov / uslovie)
if kolvoVremeni > 0 & kolvoExponatov>=0:
    print('Кол-во экспонатов, осмотренных по заданому времени равно = ',kolvoVremeni*365*24*uslovie )