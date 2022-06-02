import random
import re


def get_word(word_length):
    dictionary_file = open('dictionary/dictionary_all.json')
    dictionary_read = dictionary_file.read()
    final_list = []
    # The Discord bot can handle this now
    # word_length = input("enter word length: ")
    final_list += re.findall(r'\b(\w{%s})\b' % word_length, dictionary_read)
    final_word = random.choice(final_list)
    # print(final_word)
    return final_word, word_length


def sanitize(input_type, length, i_min, i_max, answer):
    if input_type == "int":
        while True:
            raw_input = input("Enter Integer [between %s-%s]" % (i_min, i_max))
            try:
                test = int(raw_input)
                assert i_min < test < i_max
                break
            except ValueError:
                print("value error")
                pass
            except AssertionError:
                print("out of range")
                pass
    if input_type == "str":
        while True:
            print("answer: %s" % answer)
            raw_input = input("Enter attempt [%s characters long]" % length)
            try:
                test = raw_input
                assert len(test) == int(length)
                print(len(test))
                print(length)
                # assert cross_check(test)
                break
            except AssertionError:
                print("invalid word")
                pass
            except Exception as e:
                print("unknown exception: %s" % e)
                pass
    return test


def cross_check(word):
    dictionary_file = open('dictionary/dictionary_all.json')
    dictionary_read = dictionary_file.read()
    match = re.search(r'\b%s\b' % word, dictionary_read)
    if match:
        return True
    else:
        return False


def dissect(word):
    word_dissected = []
    for i in word:
        word_dissected.append(i)
    return word_dissected


def compare_answer(answer, word):
    answer = dissect(answer)
    word = dissect(word)

    word = word
    answer = answer
    correct_letter = []
    correct_letter_place = []
    i = 0
    for letter in word:
        try:
            assert letter in answer
            correct_letter.append(i)
            assert letter == answer[i]
            correct_letter_place.append(i)
            i += 1
            pass
        except AssertionError:
            i += 1
            pass
    return correct_letter, correct_letter_place


def round_results(correct_letters, correct_places, answer_length):
    results_background = []
    a = 0
    while a < int(answer_length):
        results_background.append(0)
        a += 1
        # this is probably a weird way to do this, but I'm assigning
        # the background here so that 0=black, 1=yellow, and >1= green
    for i in correct_letters:
        results_background[i] += 1
    for i in correct_places:
        results_background[i] += 2
    return results_background


def main():
    answer_results = get_word(5)
    answer = answer_results[0]
    answer_length = answer_results[1]

    # here is the main game loop.
    over = False
    while over is False:
        # get user input, then compare it to the answer
        user_input = sanitize("str", answer_length, 0, 0, answer)
        answers_compared = compare_answer(answer, user_input)
        correct_letters = answers_compared[0]
        correct_places = answers_compared[1]
        print("<><><><><><><><><>")
        print(correct_letters)
        print(correct_places)
        print("------------")
        print(round_results(correct_letters, correct_places, answer_length))
        print(user_input)


# get_word()
main()
print(get_word())
