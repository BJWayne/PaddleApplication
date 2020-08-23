# PaddleApplication
All the models here are based on PaddlePaddle

## PaddleHub是百度Paddle系列中的预训练模型库，包括很多主流模型，可以直接使用并快捷部署，同时也可以用来做迁移学习，是一个非常实用高效的深度学习工具
这次的项目是使用paddlehub中的style_artistic（全卷积风格迁移网络）对图像和视频做风格转换
导入预训练模型很简单，只需要安装paddlehub之后，运行以下代码即可：
```python
    stylepro_artistic = paddelhub.Module(name="stylepro_artistic")
```
该模型的使用方法如下：
```python
    result=stylepro_artistic.style_transfer(paths=[{'content':'example.jpg','styles':['temp1.jpg']}])
```
其中，'content'对应要转换的原图像，'styles'对应风格模板，这里的模板是一个list，可以传入多个模板，并且可以设置不同模板的权重以达到不同的风格融合效果。模型调用中默认是不会保存转换之后的图像的，需要设置visualization=True。不过对于一张图像，其结果记录在result[0]['data']中，可以直接绘制。

视频的处理要稍微麻烦一点，需要先使用opencv将视频切分成图片，再对图片做风格转换，最后将转换好的图片合成为视频。

```python
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
```

```python
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
```

下面展示一个图像风格转换的示例。
原图：

![example](https://github.com/BJWayne/PaddleApplication/blob/PaddleHub/example.jpg)

模板1：

![temp1](https://github.com/BJWayne/PaddleApplication/blob/PaddleHub/temp1.jpg)

模板2：

![temp2](https://github.com/BJWayne/PaddleApplication/blob/PaddleHub/temp2.jpg)

模板1转换之后：

![transfer1](https://github.com/BJWayne/PaddleApplication/blob/PaddleHub/transfer1.png)

模板2转换之后：

![transfer2](https://github.com/BJWayne/PaddleApplication/blob/PaddleHub/transfer2.png)

同时用模板1和模板2转换（等权重）：

![transfer12](https://github.com/BJWayne/PaddleApplication/blob/PaddleHub/transfer12.png)

图像转换的代码和视频转换的代码已上传

百度AI Studio的项目地址为：https://aistudio.baidu.com/aistudio/projectdetail/444491
