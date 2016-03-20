import numpy

word_index = 0
dict = {}
path = '/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_wordalignment'
word_list = numpy.load(path + '/speaker_output_test1')
for word in word_list:
    if word not in dict:
        if word != "sil":
            dict[word] = word_index
            word_index +=1

for i in range(1,33):
    output_vector = []
    word_list = numpy.load(path + '/speaker_output_test'+str(i))
    for j in range(len(word_list)):
        cur_vector = [0] * len(dict)
        cur_vector[dict[word_list[j]]] = 1
        output_vector.append(cur_vector)
    output_vector = numpy.asarray(output_vector)
    numpy.save(path + '/speaker_final_output_test'+str(i),output_vector)


for i in range(1,33):
    output_vector = []
    word_list = numpy.load(path +'/speaker_output_train'+str(i))
    for j in range(len(word_list)):
        cur_vector = [0] * len(dict)
        cur_vector[dict[word_list[j]]] = 1
        output_vector.append(cur_vector)
    output_vector = numpy.asarray(output_vector)
    numpy.save(path + '/speaker_final_output_train'+str(i),output_vector)
