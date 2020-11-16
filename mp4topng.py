import cv2
import os
# video_path='test_video/'
# videos=os.listdir(video_path)
# videos.sort(key=lambda x:int(x.split('.')[0]))
# i=0
# for video in videos:
#     i=i+10000
#     name=video.split('.')[0]
#     if not os.path.exists('exp/'+name):
#         os.mkdir('exp/'+name)
#     cap = cv2.VideoCapture(video_path+video)
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     fps =cap.get(cv2.CAP_PROP_FPS)
#     #fps=30
#     size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#     #size=(960,544)
#     while(cap.isOpened()):
#         i=i+1
#         ret, frame = cap.read()
#         if ret==True:
#             cv2.imwrite('exp/{}/'.format(name)+'in%06d.jpg'%i,frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         else:
#             break
#     cap.release()
#
#     cv2.destroyAllWindows()

fps = 10    #保存视频的FPS，可以适当调整
optical_flow_dir= 's1/'

files = os.listdir(optical_flow_dir)
#files.sort(key=lambda k: int(k.split('.')[0]))
size=cv2.imread(optical_flow_dir+files[0]).shape[:2]
#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*"MPEG")
videoWriter = cv2.VideoWriter(optical_flow_dir+'s1.mp4',fourcc,fps,(size[1],size[0]),True)#最后一个是保存图片的尺寸

#for(i=1;i<471;++i)
for file in files:
    frame = cv2.imread(optical_flow_dir+file)
    videoWriter.write(frame)
videoWriter.release()