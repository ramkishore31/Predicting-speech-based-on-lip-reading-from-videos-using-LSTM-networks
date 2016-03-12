import numpy
import cv2
import os
import scipy
cnt1 = 0
cnt2 = 0
#speaker_list = next(os.walk('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'))[1]
#print speaker_list
for cnt1 in range(7,35):
    print "Speaker",cnt1
    if cnt1 != 8 and cnt1 != 21:
        videoname_list = next(os.walk('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization3/speaker'+str(cnt1)+'/'))[1]
        cnt2 = 0
        speaker_input =[]
        speaker_output = []
        for video_name in videoname_list:
            if cnt2 % 100 == 0:
                print cnt2
            cnt2 += 1
            align_filename = video_name.split('.', 1)[0] + ".align"
            fileptr = open('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization3/align'+ str(cnt1)+'/'+align_filename, "r+")
            sentence_framesdata = fileptr.read().splitlines()
            for word_framedata in sentence_framesdata:
                 word_array = numpy.zeros((50,2800))
                 starting_frame = word_framedata.split()[0]
                 starting_frame = int(starting_frame) / 1000
                 starting_frame += 1
                 ending_frame = word_framedata.split()[1]
                 ending_frame = int(ending_frame) / 1000
                 word = word_framedata.split()[2]
                 word_index = 0
                 while starting_frame <= ending_frame:
                    f = file('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization3/speaker'+str(cnt1)+'/'+video_name+'/'+str(starting_frame),"rb")
                    image = numpy.load(f)
                    image = numpy.resize(image,2800)
                    word_array[word_index] = image
                    word_index += 1
                    starting_frame += 1
                 speaker_input.append(word_array)
                 speaker_output.append(word)
        speaker_input = numpy.asarray(speaker_input)
    print speaker_input.shape,len(speaker_output)
    if not os.path.exists('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_wordalignment/'):
        os.makedirs('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_wordalignment/')
    f = file('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_wordalignment/speaker_input'+str(cnt1),"wb")
    numpy.savez_compressed(f,speaker_input)
    f = file('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_wordalignment/speaker_output'+str(cnt1),"wb")
    numpy.save(f,speaker_output)