# breaks=икуфлы
# here=руку
# lunch=дгитис
# playing=здифинштип
# need=туув
# sun=ыгит
# tightly=ешпредин
# overhead=щмукруфив
# attacks=фефслы
# head=руфив
# talk=ефдил
# other=шерук
# are=фку
# with=цшер
# warm=цфык
# yoga=щпиф
# friends=акшутвы
# lines=дшитуы
# voice=мщишсу
# heavy=руфмин
# goal=пщифд
# experienced=учзукшутсув
# zones=яшты
# wake=цфлу
# many=ыфтин
# tramontane;=трамонтана
# across=фсыкщи
# engines=уптутшы
# sinner=ыштук
# orders=щквукы
# tanks=ефтлы
# answer=фтыцук
# don't=выщтэ
# camp=сфиз
# they=ерун
# requesting=куйгуштеп
# adults=вгеды
# action=фсещт
# hello=рудыщ
# ships=ыршзы
# but=иге
# drawn=вкифтиц
# children=сришдвукут
# planes=здифтуы
# advanced=фывмыфсув
# class=судфы
# clear=сдуфик
# nssa=нсса
# tasks=ефтилы
# withdrawing=цшервукциштип
# go=пшы
# afternoon=фектищит
# them=ерум
# some=ыщью
# marched=фкусрув
# the=еру
# attending=футевштип
# soft=ыщае
# steady=ыефун
# sure=ыгку
# prefer=зкаук
# everyone=умукнищту
# at=фе
# meetings=уештпы
# others=шерукы
# we=цу
# idle=швиду
# flew=адуц
# my=ыу
# will=цшид
# their=ерук
# if=ша
# 3=ерку
# up=гыз
# scanning=ысфтиштип
# loud=дыщгив
# support=ыгзыщке
# lunchtime=дгитисрешью
# guiding=пгивштип
# north=тщекр
# gave=фму
# forces=ащксы
# maneuver=фтугмук
# while=цыршду
# as=фы
# a=фа
# in=шти
# by=ин
# after=феук
# sandwich=ыфтвицшыр
# genghis=чошпош
# learning=кыщфкиштип
# words=цыщквы
# intentions=штеутещты
# drink=вкишытл
# long=дыщтип
# people=зушду
# school=ысришыд
# is=шы
# hand=ртив
# khan=штырь
# ur;=ур
# cross=сыкщи
# dropped=вкищзув
# our=щгик
# any=фтин
# might=шпре
# chingizhan=чошпоштырь
# from=акщ
# enemy=утун
# sign=ышт
# completing=сщыздештип
# did=вшыв
# ambitions=фишешты
# emperors=узущики
# and=фтив
# nssa;=нсса
# every=умукун
# come=сшью
# assurances=фыгфтусы
# roaring=кщифкшит
# new=туц
# bridge=икшпу
# you=ныщг
# soldiers=ыщвукдшы
# we've=цуэму
# live=дышму
# ur=ур
# salad=ыфдыфыв
# to=еш
# there=еруку
# toward=ещцыфкив
# tuesday=егуфын
# during=вигштип
# join=ошит
# teachers=уфсрукы
# moving=ышмыштып
# teacher=уфсрук
# coffee=сшау
# border=ищквук
# understatement=гитвукефете
# shadow=ырфивщыц
# when=црут
# commander=сфитвук
# charge=срифпу
# morning=щкитштип
# so=ыщ
# front=акщте
# field=ашдув
# things=ершпы
# city=сшен
# his=ршы
# alive=фдышму
# troops=ешзы
# boots=ищещы
# supplies=ыгздушы
# rifles=кшаду
# day=выфин
# work=цыщикл
# ordinal=щкифтшфид
# not=тще
# on=щит
# was=цфы
# hail=рфишыд
# something=ышурштип
# do=выщ
# doesn't=вщутыэ
# start=ефке
# rises=кшыу
# savien=ыфшмут
# that=ерфе
# coordinated=сщиквиштифец
# of=ща
# each=уфр
# behind=урштив
# attack=фефсыл
# be=иу
# firm=ашк
# ground=пкищгвит
# ship=ырш
# distance=вшефтысу
# afraid=факфшыв
# through=еркигпыр
# oshtro=оштро
# for=ашк
# your=ныщгик
# eyes=унуы
# held=рудив
# world=цыщдив
# what=церфе
# tramontane=трамонтана
# empire=узышку
# rumbled=кигидув
# tea=ефу
# horizon=рщикщяшт
# glory=пдыщкин
# emperor=узущик
# which=цришыр
# enjoys=утощны
# or=щик
# END
import difflib
import random
from gtts import gTTS
import pygame

pygame.init()

def say(text, lang='en', wait=False):
    gTTS(text=text, lang=lang).save('speech.ogg')
    pygame.mixer.Sound('speech.ogg').play()
    if wait:
        while pygame.mixer.get_busy():
            pass

def word_similarity(words, target_word):
    similarity_dict = {}

    for word in words:
        if word == target_word:
            continue
        # Calculate similarity score using difflib
        similarity = difflib.SequenceMatcher(None, word, target_word).ratio()
        similarity_dict[word] = similarity

    # Sort by similarity in descending order and limit to top 5
    sorted_similarity = sorted(similarity_dict.items(), key=lambda x: x[1], reverse=True)[:1][0]

    return sorted_similarity


def load_lang(path: str):
    with open(path, 'r', encoding='UTF-8') as f:
        lines = f.read().split('\n')
    return lines


def translate_to_low(text: str):
    result = []
    lines = load_lang()
    lines = lines[:lines.index('# END')]
    lines = [i[2:] for i in lines]
    dictionary = {}
    for i in lines:
        dictionary[i[:i.index('=')]] = i[i.index('=') + 1:]
    for i in text.split():
        word = ''
        is_capital = False
        is_upper = False
        endswith = ''
        if i[-1] in '.,?!:;':
            endswith = i[-1]
            i = i[:-1]
            # print(f'{i} ends with {endswith}')
        is_capital = i[0].isupper()
        is_upper = i.isupper()
        if is_capital:
            pass
            # print(f'{i} is capitalised')

        if dictionary.get(i.lower(), False):
            word = dictionary.get(i.lower())
        else:
            similar = word_similarity(dictionary.keys(), i.lower())
            if similar[1] > 0.8:
                print(f'Suggestion: {similar[0]} = {dictionary.get(similar[0], "NOT FOUND WTF EROR")}')
            new_word = input(f'? {i} = ')
            say(new_word, lang='ru')
            if new_word:
                dictionary[i.lower()] = new_word.lower()
                word = dictionary[i.lower()]
            else:
                word = i

        if is_capital:
            word = word.capitalize()
        if is_upper:
            word = word.upper()
        word += endswith
        # print(f'Appending {word}...')
        # print()
        result.append(word)
    # print(result)
    new_me = []
    for i in dictionary:
        new_me.append(f'# {i}={dictionary.get(i)}')
    random.shuffle(new_me)
    new_me.extend(load_lang()[load_lang().index('# END'):])
    with open('translator.py', 'w', encoding='UTF-8') as f:
        f.write('\n'.join(new_me))
    print(' '.join(result))
    say(' '.join(result), lang='ru', wait=True)
    return ' '.join(result)


def translate_from_low(text: str) -> str:
    result = []
    lines = load_lang()
    lines = lines[:lines.index('# END')]
    lines = [i[2:] for i in lines]
    dictionary = {}
    for i in lines:
        dictionary[i[i.index('=') + 1:]] = i[:i.index('=')]
    for i in text.split():
        word = ''
        is_capital = False
        is_upper = False
        endswith = ''
        if i[-1] in '.,?!:':
            endswith = i[-1]
            i = i[:-1]
            # print(f'{i} ends with {endswith}')
        is_capital = i[0].isupper()
        is_upper = i.isupper()
        if is_capital:
            pass
            # print(f'{i} is capitalised')

        if dictionary.get(i.lower(), False):
            word = dictionary.get(i.lower())
        else:
            word = i.lower()

        if is_capital:
            word = word.capitalize()
        if is_upper:
            word = word.upper()
        word += endswith
        # print(f'Appending {word}...')
        # print()
        result.append(word)
    # print(result)
    print(' '.join(result))
    say(' '.join(result), lang='en', wait=True)
    return ' '.join(result)


if __name__ == "__main__":
    print('Use translate_to_low or translate_from_low')