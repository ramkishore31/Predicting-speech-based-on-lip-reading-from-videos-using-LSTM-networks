import numpy
import cv2
import os

source_path = '/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthsegmentation/'
destination_path = '/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_mouthnormalization/'
speaker_list = next(os.walk(source_path))[1]
print len(speaker_list)
for i in range(1,33):
    videoname_list = next(os.walk(source_path + str(speaker_list[i])+'/'))[1]
    for video_name in videoname_list:
        frame_list = next(os.walk(source_path + str(speaker_list[i])+'/' + str(video_name) + '/'))[2]
        for frame in frame_list:
            if frame.endswith('.jpg') and not frame.endswith('75.jpg'):
                imagePath = source_path + str(speaker_list[i])+'/'+str(video_name)+'/'+str(frame)
                image = cv2.imread(imagePath,0)
                image = cv2.resize(image,(40, 40))
                image = numpy.asarray(image)
                image_min = image[image>0].min()
                image_max = image[image>0].max()
                image = (image - image_min) / (float(image_max - image_min))
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                if not os.path.exists(destination_path + str(speaker_list[i])+'/'):
                    os.makedirs(destination_path + str(speaker_list[i])+'/')

                if not os.path.exists(destination_path + str(speaker_list[i])+'/'+ str(video_name) +'/'):
                    os.makedirs(destination_path + str(speaker_list[i])+'/'+ str(video_name) +'/')

                f = file(destination_path + str(speaker_list[i])+'/'+ str(video_name) +'/' +str(frame.split('.', 1)[0]),"wb")
                numpy.save(f,image)
                cv2.destroyAllWindows()

