import os
import copy


class WordsQueue:
    def __init__(self, word, count):
        self.name = word
        self.word_count = count
        self.sum_count = 0
        self.effective_count = 0


def file_process(file_class):
    file_class_words = []
    final = []

    for file in file_class:
        file_class_words = file.split()
        for words in file_class_words:
            if words.__len__() < 3:
                file_class_words.remove(words)
            try:
                if int(words):
                    file_class_words.remove(words)
            except ValueError:
                pass
        for words in file_class_words:
            new_word = words.replace(".", "")
            new_word = new_word.replace(":", "")
            new_word = new_word.replace(";", "")
            new_word = new_word.replace("(", "")
            new_word = new_word.replace(")", "")
            new_word = new_word.replace(",", "")
            new_word = new_word.replace("!", "")
            new_word = new_word.replace("`", "")
            new_word = new_word.replace("?", "")
            new_word = new_word.replace("<", "")
            new_word = new_word.replace(">", "")
            new_word = new_word.replace("|", "")
            new_word = new_word.replace("$", "")
            final.append(new_word.upper())
        for words in final:
            if words.__len__() < 3:
                final.remove(words)

    return final


def effective_counter(class_list):
    for class1 in class_list:
        for obj1 in class1:
            for class2 in class_list:
                if class2 != class1:
                    for obj2 in class2:
                        if obj1.name == obj2.name:
                            obj1.sum_count += obj2.word_count
    for class3 in class_list:
        for obj in class3:
            obj.effective_count = obj.word_count - obj.sum_count


files_class1 = []
files_class_1_final = []
files_class2 = []
files_class_2_final = []
files_class3 = []
files_class_3_final = []
files_class4 = []
files_class_4_final = []
files_class5 = []
files_class_5_final = []
files_class6 = []
files_class_6_final = []

for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/1/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/1/Train/' + '{0}'.format(
        filename)
    f = open(path)
    files_class1.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/2/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/2/Train/' + '{0}'.format(
        filename)
    f = open(path)
    files_class2.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/3/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/3/Train/' + '{0}'.format(
        filename)
    f = open(path)
    files_class3.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/4/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/4/Train/' + '{0}'.format(
        filename)
    f = open(path)
    files_class4.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/5/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/5/Train/' + '{0}'.format(
        filename)
    f = open(path)
    files_class5.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/6/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/6/Train/' + '{0}'.format(
        filename)
    f = open(path)
    files_class6.append(f.read())

files_class1 = file_process(files_class1)
files_class2 = file_process(files_class2)
files_class3 = file_process(files_class3)
files_class4 = file_process(files_class4)
files_class5 = file_process(files_class5)
files_class6 = file_process(files_class6)

for words in files_class1:
    word_count = 0
    for word in files_class1:
        if words == word:
            word_count += 1
            files_class1.remove(word)
    word_obj = WordsQueue(words, word_count)
    files_class_1_final.append(word_obj)

for words in files_class2:
    word_count = 0
    for word in files_class2:
        if words == word:
            word_count += 1
            files_class2.remove(word)
    word_obj = WordsQueue(words, word_count)
    files_class_2_final.append(word_obj)

for words in files_class3:
    word_count = 0
    for word in files_class3:
        if words == word:
            word_count += 1
            files_class3.remove(word)
    word_obj = WordsQueue(words, word_count)
    files_class_3_final.append(word_obj)

for words in files_class4:
    word_count = 0
    for word in files_class4:
        if words == word:
            word_count += 1
            files_class4.remove(word)
    word_obj = WordsQueue(words, word_count)
    files_class_4_final.append(word_obj)

for words in files_class5:
    word_count = 0
    for word in files_class5:
        if words == word:
            word_count += 1
            files_class5.remove(word)
    word_obj = WordsQueue(words, word_count)
    files_class_5_final.append(word_obj)

for words in files_class6:
    word_count = 0
    for word in files_class6:
        if words == word:
            word_count += 1
            files_class6.remove(word)
    word_obj = WordsQueue(words, word_count)
    files_class_6_final.append(word_obj)

class_list = [files_class_1_final, files_class_2_final, files_class_3_final, files_class_4_final, files_class_5_final,
              files_class_6_final]
effective_counter(class_list)

f = open("Word Frequency_Class 1.txt", "w+")
for obj in files_class_1_final:
    f.write("{0} {1}\n".format(obj.name, obj.word_count))
f.close()

f = open("Word Frequency_Class 2.txt", "w+")
for obj in files_class_2_final:
    f.write("{0} {1}\n".format(obj.name, obj.word_count))
f.close()

f = open("Word Frequency_Class 3.txt", "w+")
for obj in files_class_3_final:
    f.write("{0} {1}\n".format(obj.name, obj.word_count))
f.close()

f = open("Word Frequency_Class 4.txt", "w+")
for obj in files_class_4_final:
    f.write("{0} {1}\n".format(obj.name, obj.word_count))
f.close()

f = open("Word Frequency_Class 5.txt", "w+")
for obj in files_class_5_final:
    f.write("{0} {1}\n".format(obj.name, obj.word_count))
f.close()

f = open("Word Frequency_Class 6.txt", "w+")
for obj in files_class_6_final:
    f.write("{0} {1}\n".format(obj.name, obj.word_count))
f.close()

files_class_1_final.sort(key=lambda x: x.effective_count, reverse=True)
f = open("Best Attribute_Class 1.txt", "w+")
for i in range(0, 20):
    f.write("{0}\n".format(files_class_1_final[i].name))
f.close()

files_class_2_final.sort(key=lambda x: x.effective_count, reverse=True)
f = open("Best Attribute_Class 2.txt", "w+")
for i in range(0, 20):
    f.write("{0}\n".format(files_class_2_final[i].name))
f.close()

files_class_3_final.sort(key=lambda x: x.effective_count, reverse=True)
f = open("Best Attribute_Class 3.txt", "w+")
for i in range(0, 20):
    f.write("{0}\n".format(files_class_3_final[i].name))
f.close()

files_class_4_final.sort(key=lambda x: x.effective_count, reverse=True)
f = open("Best Attribute_Class 4.txt", "w+")
for i in range(0, 20):
    f.write("{0}\n".format(files_class_4_final[i].name))
f.close()

files_class_5_final.sort(key=lambda x: x.effective_count, reverse=True)
f = open("Best Attribute_Class 5.txt", "w+")
for i in range(0, 20):
    f.write("{0}\n".format(files_class_5_final[i].name))
f.close()

files_class_6_final.sort(key=lambda x: x.effective_count, reverse=True)
f = open("Best Attribute_Class 6.txt", "w+")
for i in range(0, 20):
    f.write("{0}\n".format(files_class_6_final[i].name))
f.close()
