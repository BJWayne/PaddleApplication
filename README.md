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

下面展示一个图像风格转换的示例。
原图：

模板1：

模板2：

模板1转换之后：

模板2转换之后：

同时用模板1和模板2转换（等权重）：
