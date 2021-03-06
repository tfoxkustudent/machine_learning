import string
import numpy as np
import csv
import re
import os

# Get Data
training_data = open('alllines.txt')
lineOne = open('lineOne.txt')
lineTwo = open('lineTwo.txt')
lineThree = open('lineThree.txt')

# Remove Commas
def remove_commas(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))


# form dictionary to be able to compare two given states (markov)
def form_dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)


# We need to keep track of probabilities from each two pairs of words
def probabilities(list):
    probability_list = {}
    length_of_list = len(list)
    for i in list:
        probability_list[i] = probability_list.get(i, 0) + 1
    for key, value in probability_list.items():
        probability_list[key] = value / length_of_list
    return probability_list


# We have to have a place for the first and second words because they will not have a key value pair
# aLso need to have a place when we transition to next line

first_word = {}
second_word = {}
transition = {}

actorMM = {}
actorList = []
trainingFile = 'Shakespeare_data.csv'


def actSceneLine(strASL):
    strASL = strASL.split('.')
    scene = int(strASL[1])
    return scene


def returnLine(strLine):
    return re.findall(r"[\w]+|[.,!?:]", strLine)

"""
def actorTrain(trainingFile):
    with open(trainingFile) as csvfile:  # open up Shakespeare
        reader = csv.DictReader(csvfile)
        prvScene = 0
        previousActor = 'START SCENE'
        for row in reader:
            if row['ActSceneLine'] != '':  # Lines only delivered

                # Update check for new play scene
                scene = actSceneLine(row['ActSceneLine'])
                if scene != prvScene:
                    if previousActor != 'START SCENE':  # Exception only at beginning of file
                        form_dict(actorMM, previousActor, 'END SCENE')
                        form_dict(actorMM, 'START SCENE', 'END SCENE')
                        previousActor = 'START SCENE'  # No previous actor at start of scene
                prvScene = scene

                # Forming model for actors
                currentActor = row['Player']
                currentLine = returnLine(row['PlayerLine'])

                form_dict(actorList, previousActor, currentActor)
                previousActor = currentActor

                for word

"""
# Train our model
def train():
    # we need to grab our our words to process, remove commas and make lowercase
    for line in training_data:

        words = remove_commas(line.rstrip().lower()).strip()
        words = words.split()
        # Create indexes for words
        num_words = len(words)
        for i in range(num_words):
            word = words[i]
            # if index is zero, that means it is the first word
            if i == 0:
                first_word[word] = first_word.get(word, 0) + 1
            else:
                # create index for previous word
                previous_word = words[i - 1]
                # if index is last word then we need to mark it with 'Next Line' in the dictionary
                if i == num_words - 1:
                    form_dict(transition, (previous_word, word), 'NEXT LINE')
                # if index is 1 then it is the second word,  need to add to dictionary
                if i == 1:
                    form_dict(second_word, previous_word, word)
                else:
                    two_words_ago = words[i - 2]
                    form_dict(transition, (two_words_ago, previous_word), word)

    # We have to Normalize the distributions
    first_word_total = sum(first_word.values())
    for key, value in first_word.items():
        first_word[key] = value / first_word_total

    for previous_word, next_word in second_word.items():
        second_word[previous_word] = probabilities(next_word)

    for two_words, next_word in transition.items():
        transition[two_words] = probabilities(next_word)

    print("training finished")


# We Have to get a random word to generate our text
def random_word(dictionary):
    p0 = np.random.random()
    cumulative = 0
    for key, value in dictionary.items():
        cumulative += value
        if p0 < cumulative:
            return key
    assert (False)


num_lines = 10


def generate_text():
    spaceDeliminator = " "
    for i in range(num_lines):
        sentence = []
        # Fist word
        word0 = random_word(first_word)
        sentence.append(word0)
        # Second word
        word1 = random_word(second_word[word0])
        sentence.append(spaceDeliminator)
        sentence.append(word1)
        # Remaining words until NEW LINE
        while True:
            word2 = random_word(transition[(word0, word1)])
            if word2 == "NEXT LINE":
                break
            sentence.append(spaceDeliminator)
            sentence.append(word2)
            word0 = word1
            word1 = word2
        print(''.join(sentence))

def predict_text(x):
    for line in x:
        words = remove_commas(line.rstrip().lower()).strip()
        words = words.split()
        num_words = len(words)

        word0 = words[0]
        word1 = words[1]
        spaceDeliminator = " "
        for i in range(1):
            sentence = []
            # Fist word
            sentence.append(word0)
            # Second word

            sentence.append(spaceDeliminator)
            sentence.append(word1)
            # Remaining words until NEW LINE
            while True:
                word2 = random_word(transition[(word0, word1)])
                if word2 == "NEXT LINE":
                    break
                sentence.append(spaceDeliminator)
                sentence.append(word2)
                word0 = word1
                word1 = word2
            print(''.join(sentence))

#actorTrain(trainingFile)
train()
print("Randomly Generated Text:\n")
generate_text()
print('\n')
print("True Text: To be commenced in strands afar remote")
print('\n')
print("Predicted Text:")
predict_text(lineOne)
print('\n')
print("True Text: hostess of the tavern a most sweet wench")
print('\n')
print("Predicted Text:")
predict_text(lineTwo)
print('\n')
print("True Text: your purses full of crowns, if you will not, tarry")
print('\n')
print("Predicted Text:")
predict_text(lineThree)





