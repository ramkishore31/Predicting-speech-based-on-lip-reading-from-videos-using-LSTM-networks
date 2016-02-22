import cv2
import os

speaker_list = next(os.walk('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_videos/'))[1]
for speaker in speaker_list:
    print "Extracting frames for speaker ",cnt1
    for filename in os.listdir('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_videos/'+str(speaker)+'/'):
        if filename.endswith('.mpg'):
            frame_count = 1
            vc = cv2.VideoCapture('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_videos/'+str(speaker)+'/' + filename)
            if vc.isOpened():
                rval , frame = vc.read()
            else:
                rval = False

            while rval:
                rval, frame = vc.read()
                if not os.path.exists('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_frames/'+str(speaker)+'/'):
                    os.makedirs('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_frames/'+str(speaker)+'/')

                if not os.path.exists('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_frames/'+str(speaker)+'/'+ str(filename) +'/'):
                    os.makedirs('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_frames/'+str(speaker)+'/'+ str(filename) +'/')

                cv2.imwrite('/Users/ramkishore31/Neural Networks/final_project/dataset/lowquality_frames/'+str(speaker)+'/'+ str(filename) +'/' +str(frame_count)+'.jpg',frame)
                frame_count = frame_count + 1
                cv2.waitKey(1)
            vc.release()
