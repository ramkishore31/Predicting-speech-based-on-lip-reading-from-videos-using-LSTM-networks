import cv2
import os

source_path = '/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_videos/'
destination_path = '/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_frames/'
speaker_list = next(os.walk(source_path))[1]
for speaker in speaker_list:
    for filename in os.listdir(source_path + str(speaker)+'/'):
        if filename.endswith('.mpg'):
            frame_count = 1
            vc = cv2.VideoCapture(source_path + str(speaker)+'/' + filename)
            if vc.isOpened():
                rval , frame = vc.read()
            else:
                rval = False

            while rval:
                rval, frame = vc.read()
                if not os.path.exists(destination_path + str(speaker)+'/'):
                    os.makedirs(destination_path + str(speaker)+'/')

                if not os.path.exists(destination_path + str(speaker)+'/'+ str(filename) +'/'):
                    os.makedirs(destination_path + str(speaker)+'/'+ str(filename) +'/')

                cv2.imwrite(destination_path + str(speaker)+'/'+ str(filename) +'/' +str(frame_count)+'.jpg',frame)
                frame_count = frame_count + 1
                cv2.waitKey(1)
            vc.release()