# PaddleApplication
All the models here are based on PaddlePaddle

## PaddleHub是百度Paddle系列中的预训练模型库，包括很多主流模型，可以直接使用并快捷部署，同时也可以用来做迁移学习，是一个非常实用高效的深度学习工具
这次的项目是使用paddlehub中的style_artistic（全卷积风格迁移网络）对图像和视频做风格转换
导入预训练模型很简单，只需要安装paddlehub之后，运行以下代码即可：
''
stylepro_artistic = paddelhub.Module(name="stylepro_artistic")
''
该模型的使用方法如下：

result=stylepro_artistic.style_transfer(paths=[{'content':'example.jpg','styles':['temp1.jpg']}])

其中，'content'对应要转换的原图像，'styles'对应风格模板，这里的模板是一个list，可以传入多个模板，并且可以设置不同模板的权重以达到不同的风格融合效果。
