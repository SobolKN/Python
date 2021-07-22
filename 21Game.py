import random

print('Игра Очко. Тяните карты с разным начением и наберите 21 очко. Превысив лимит в 21 очко вы проигрываете')

cards=[6,7,8,9,10,2,3,4,11,6,7,8,9,10,2,3,4,11,6,7,8,9,10,2,3,4,11,6,7,8,9,10,2,3,4,11]# колода
points = 0#счёт

while True:
    fc=input('Сыграем? да\нет')
    if fc=='y':
        while True:
            c = input('Будете тянуть карту? да\нет')
            if c == 'y':
                a = cards.pop(random.choice(cards))
                print('Вы взяли карту ', a,'очков')
                points += a
                if points > 21:
                    print('Перебор! Вы проиграли')
                    break
                elif points == 21:
                    print('Вы набрали 21! Победа!')
                    break
                else:
                    print('У вас', points,'очков.' )
            elif c == 'n':
                print('У вас', points, '. Игра окончена' )
                break
    else:
        print('Пока')
        break
