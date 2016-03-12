import numpy

word_index = 0
dict = {}
word_list = numpy.load('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_wordalignment/speaker_output1')
for word in word_list:
    if word not in dict:
        dict[word] = word_index
        word_index += 1

for i in range(1,15):
    output_vector = []
    word_list = numpy.load('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_wordalignment/speaker_output'+str(i))
    for j in range(len(word_list)):
        cur_vector = [0] * len(dict)
        cur_vector[dict[word_list[j]]] = 1
        output_vector.append(cur_vector)
    output_vector = numpy.asarray(output_vector)
    numpy.save('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_wordalignment/speaker_final_output'+str(i),output_vector)




