import difflib
import sys
from gtts import gTTS
import pygame

pygame.init()

debug = 'debug' in sys.argv

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


def load_lang(path: str, backwards: bool = False) -> dict:
    with open(path, 'r', encoding='UTF-8') as f:
        lines = f.read().split('\n')
    dictionary = {}
    for i in lines:
        if backwards:
            dictionary[i[i.index('=') + 1:]] = i[:i.index('=')]
        else:
            dictionary[i[:i.index('=')]] = i[i.index('=') + 1:]
    return dictionary


def update_lang(path: str, new_dict: dict, backwards: bool = False):
    new_me = []
    for i in new_dict:
        if backwards:
            new_me.append(f'{new_dict.get(i)}={i}')
        else:
            new_me.append(f'{i}={new_dict.get(i)}')
    with open(path, 'w', encoding='UTF-8') as f:
        f.write('\n'.join(new_me))


def translate_to_low(text: str):
    result = []
    dictionary = load_lang('low.lingua')

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
            if debug:
                word = i.lower()
            else:
                similar = word_similarity(dictionary.keys(), i.lower())
                if similar[1] > 0.8:
                    print(f'Suggestion: {similar[0]} = {dictionary.get(similar[0], "NOT FOUND WTF EROR")}')
                new_word = input(f'? {i} = ')
                say(new_word, lang='it')
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


    update_lang('low.lingua', dictionary)
    print(' '.join(result))
    say(' '.join(result), lang='it', wait=True)
    return ' '.join(result)


def translate_from_low(text: str) -> str:
    result = []
    dictionary = load_lang('low.lingua', backwards=True)
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