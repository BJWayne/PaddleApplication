# 导入依赖包
import paddlehub as hub
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# 导入预训练模型
stylepro_artistic = hub.Module(name="stylepro_artistic")

# 使用opencv对视频进行切分，并记录fps和尺寸，将所得图片保存至pic_data中
video_name='data/data38254/hkdg.mp4'
cap=cv2.VideoCapture(video_name)
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_count=1
success=True
while success:
    success,frame=cap.read()
    if success:
        cv2.imwrite('pic_data'+'/'+'%d.jpg'%frame_count,frame)
    frame_count+=1
cap.release()

# 对切分后的图片做风格迁移
# 用法与第一部分相同，这里使用的是temp2.jpg作为模板
imgs=os.listdir('pic_data')
index=[i.split('.')[0] for i in imgs]
index=[int(i) for i in index]
index.sort()
imgs=[str(i)+'.jpg' for i in index]
for img in imgs:
    if img[0]=='.':
        continue
    image=os.path.join('pic_data',img)
    result=stylepro_artistic.style_transfer(
        paths=[{
            'content':image,
            'styles':['temp2.jpg']
        }],
        visualization=True
    )

# 得到所有风格转换之后的图片，使用opencv将这些图片重新合成视频
videowrite=cv2.VideoWriter('result.avi',cv2.VideoWriter_fourcc('D','I','V','X'), fps, size)
pics=os.listdir('transfer_result')
# idx=[i.split('.')[0] if len(i)>1 else continue for i in pics]
idx=[i.split('.')[0]+'.'+i.split('.')[1] for i in pics]
idx=[float(i[8:]) for i in idx]
idx.sort()
pics=['ndarray_'+str(i)+'.jpg' for i in idx]
for i in pics:
    pic=cv2.imread('transfer_result/'+i)
    videowrite.write(pic)