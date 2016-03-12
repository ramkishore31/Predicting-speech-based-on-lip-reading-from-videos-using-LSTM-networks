import numpy
import cv2
import os
cnt1 = 1
speaker_list = next(os.walk('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'))[1]
print

while cnt1 < 35:
    videoname_list = next(os.walk('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthsegmentation/speaker'+str(cnt1)+'/'))[1]
    print cnt1,videoname_list
    cnt1 += 1
    '''
    for video_name in videoname_list:
        cnt2 += 1
        print "Video number ",cnt2
        frame_list = next(os.walk('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthsegmentation/'+str(speaker)+'/' + str(video_name) + '/'))[2]
        for frame in frame_list:
            if frame.endswith('.jpg') and not frame.endswith('75.jpg'):
                imagePath = '/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthsegmentation/'+str(speaker)+'/'+str(video_name)+'/'+str(frame)
                image = cv2.imread(imagePath,0)
                image = numpy.asarray(image)
                image_min = image[image>0].min()
                image_max = image[image>0].max()
                image = (image - image_min) / (float(image_max - image_min))

                if not os.path.exists('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'):
                    os.makedirs('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/')

                if not os.path.exists('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'+str(speaker)+'/'):
                    os.makedirs('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'+str(speaker)+'/')

                if not os.path.exists('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'+str(speaker)+'/'+ str(video_name) +'/'):
                    os.makedirs('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'+str(speaker)+'/'+ str(video_name) +'/')


                cv2.imwrite('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'+str(speaker)+'/'+ str(video_name) +'/' +str(frame),image)
                cv2.destroyAllWindows()
    cnt1 += 1
'''
