# PaddleApplication
All the models here are based on PaddlePaddle

## PaddleHub是百度Paddle系列中的预训练模型库，包括很多主流模型，可以直接使用并快捷部署，同时也可以用来做迁移学习，是一个非常实用高效的深度学习工具
这次的项目是使用paddlehub中的style_artistic（全卷积风格迁移网络）对图像和视频做风格转换
导入预训练模型很简单，只需要安装paddlehub之后，运行以下代码即可
stylepro_artistic = paddelhub.Module(name="stylepro_artistic")
