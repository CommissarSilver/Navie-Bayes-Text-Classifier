import os


def train_this_boy(train_matrix, keyword_list):
    independent_probabilities = []
    for j in range(0, 120):
        keyword_count = 0
        temp = []
        for i in range(0, 100):
            if train_matrix[i][j] == 1:
                keyword_count += 1
        ind_prob_text = keyword_list[j]
        ind_prob_num = keyword_count / 100
        temp.append(ind_prob_text)
        temp.append('class1')
        temp.append(ind_prob_num)
        independent_probabilities.append(temp)

        keyword_count = 0
        temp = []
        for i in range(100, 200):
            if train_matrix[i][j] == 1:
                keyword_count += 1
        ind_prob_text = keyword_list[j]
        ind_prob_num = keyword_count / 100
        temp.append(ind_prob_text)
        temp.append('class2')
        temp.append(ind_prob_num)
        independent_probabilities.append(temp)

        keyword_count = 0
        temp = []
        for i in range(200, 300):
            if train_matrix[i][j] == 1:
                keyword_count += 1
        ind_prob_text = keyword_list[j]
        ind_prob_num = keyword_count / 100
        temp.append(ind_prob_text)
        temp.append('class3')
        temp.append(ind_prob_num)
        independent_probabilities.append(temp)

        keyword_count = 0
        temp = []
        for i in range(300, 400):
            if train_matrix[i][j] == 1:
                keyword_count += 1
        ind_prob_text = keyword_list[j]
        ind_prob_num = keyword_count / 100
        temp.append(ind_prob_text)
        temp.append('class4')
        temp.append(ind_prob_num)
        independent_probabilities.append(temp)

        keyword_count = 0
        temp = []
        for i in range(400, 500):
            if train_matrix[i][j] == 1:
                keyword_count += 1
        ind_prob_text = keyword_list[j]
        ind_prob_num = keyword_count / 100
        temp.append(ind_prob_text)
        temp.append('class5')
        temp.append(ind_prob_num)
        independent_probabilities.append(temp)

        keyword_count = 0
        temp = []
        for i in range(500, 600):
            if train_matrix[i][j] == 1:
                keyword_count += 1
        ind_prob_text = keyword_list[j]
        ind_prob_num = keyword_count / 100
        temp.append(ind_prob_text)
        temp.append('class6')
        temp.append(ind_prob_num)
        independent_probabilities.append(temp)

    return independent_probabilities


all_them_articles_train = []
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/1/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/1/Train/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_train.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/2/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/2/Train/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_train.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/3/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/3/Train/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_train.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/4/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/4/Train/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_train.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/5/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/5/Train/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_train.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/6/Train'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/6/Train/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_train.append(f.read())

all_them_articles_test = []
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/1/Test'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/1/Test/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_test.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/2/Test'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/2/Test/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_test.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/3/Test'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/3/Test/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_test.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/4/Test'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/4/Test/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_test.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/5/Test'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/5/Test/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_test.append(f.read())
for filename in os.listdir('C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/6/Test'):
    path = 'C:/University/Machine Learning/Projects/Naive Bayes Text Processing/Data Set/6/Test/' + '{0}'.format(
        filename)
    f = open(path)
    all_them_articles_test.append(f.read())

all_them_attributes = []
f = open("Best Attribute_Class 1.txt", "r")
for keyword in f:
    keyword = keyword.replace("\n", "")
    all_them_attributes.append(keyword)
f.close()
f = open("Best Attribute_Class 2.txt", "r")
for keyword in f:
    keyword = keyword.replace("\n", "")
    all_them_attributes.append(keyword)
f.close()
f = open("Best Attribute_Class 3.txt", "r")
for keyword in f:
    keyword = keyword.replace("\n", "")
    all_them_attributes.append(keyword)
f.close()
f = open("Best Attribute_Class 4.txt", "r")
for keyword in f:
    keyword = keyword.replace("\n", "")
    all_them_attributes.append(keyword)
f.close()
f = open("Best Attribute_Class 5.txt", "r")
for keyword in f:
    keyword = keyword.replace("\n", "")
    all_them_attributes.append(keyword)
f.close()
f = open("Best Attribute_Class 6.txt", "r")
for keyword in f:
    keyword = keyword.replace("\n", "")
    all_them_attributes.append(keyword)
f.close()

train_matrix = []
for i in range(0, 600):
    temp = []
    for j in range(0, 120):
        temp.append(0)
    train_matrix.append(temp)
for i in range(0, 600):
    all_them_words_train = []
    all_them_words_train = all_them_articles_train[i].split()
    all_them_words_train_final = []
    for words in all_them_words_train:
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
        all_them_words_train_final.append(new_word.upper())
    for word in all_them_words_train_final:
        for j in range(0, 120):
            if all_them_attributes[j] == word:
                train_matrix[i][j] = 1

for i in range(0, 600):
    if i < 100:
        train_matrix[i].append('class 1')
    if 100 <= i < 200:
        train_matrix[i].append('class 2')
    if 200 <= i < 300:
        train_matrix[i].append('class 3')
    if 300 <= i < 400:
        train_matrix[i].append('class 4')
    if 400 <= i < 500:
        train_matrix[i].append('class 5')
    if 500 <= i:
        train_matrix[i].append('class 6')
ind_probs = train_this_boy(train_matrix, all_them_attributes)
test_matrix = []
for i in range(0, 90):
    temp = []
    for j in range(0, 120):
        temp.append(0)
    test_matrix.append(temp)
for i in range(0, 90):
    all_them_words_test = []
    all_them_words_test = all_them_articles_test[i].split()
    all_them_words_test_final = []
    for words in all_them_words_test:
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
        all_them_words_test_final.append(new_word.upper())
    for word in all_them_words_test_final:
        for j in range(0, 120):
            if all_them_attributes[j] == word:
                test_matrix[i][j] = 1
for i in range(0, 90):
    if i < 15:
        test_matrix[i].append('class 1')
    if 15 <= i < 30:
        test_matrix[i].append('class 2')
    if 30 <= i < 45:
        test_matrix[i].append('class 3')
    if 45 <= i < 60:
        test_matrix[i].append('class 4')
    if 60 <= i < 75:
        test_matrix[i].append('class 5')
    if 75 <= i:
        test_matrix[i].append('class 6')
for i in range(0, 90):
    file_keywords = []
    for j in range(0, 120):
        if test_matrix[i][j] == 1:
            file_keywords.append(all_them_attributes[j])
    class_prob = []
    for keyword in file_keywords:
        for probability in ind_probs:
            if keyword == probability[0]:
                class_prob.append(probability)
    total_prob = []
    for k in range(0, 6):
        file_class = 'class{0}'.format(k + 1)
        proba = 1
        for prob in class_prob:
            if prob[1] == file_class:
                proba *= prob[2]
        total_prob.append(proba)
    assigned_class = 'class {0}'.format(total_prob.index(max(total_prob)) + 1)
    test_matrix[i].append(assigned_class)
error = 0
for i in range(0, 90):
    if test_matrix[i][120] != test_matrix[i][121]:
        error += 1
print(error / 90)
f = open("Train_Weka.arff", "w+")
f.write("@RELATION train\n")
for i in range(0, 120):
    f.write("@attribute {0} ".format(all_them_attributes[i].lower()) + "{0,1}\n")
f.write("@DATA\n")
for i in range(0, 600):
    for j in range(0, 120):
        if j != 119:
            f.write("{0},".format(train_matrix[i][j]))
        else:
            f.write("{0}".format(train_matrix[i][j]))
    f.write("\n")
f.close()

f = open("Test_Weka.arff", "w+")
f.write("@RELATION test\n")
for i in range(0, 120):
    f.write("@attribute {0} ".format(all_them_attributes[i].lower()) + "{0,1}\n")
f.write("@DATA\n")
for i in range(0, 90):
    for j in range(0, 120):
        if j != 119:
            f.write("{0},".format(test_matrix[i][j]))
        else:
            f.write("{0}".format(test_matrix[i][j]))
    f.write("\n")
f.close()
