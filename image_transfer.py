import paddlehub as hub
import os
import numpy as np
import matplotlib.pyplot as plt

# 导入预训练模型
stylepro_artistic = hub.Module(name="stylepro_artistic")

# 查看原图像和风格模板图像
plt.figure()
plt.imshow(plt.imread('example.jpg'))
plt.title('original')
plt.figure()
plt.imshow(plt.imread('temp1.jpg'))
plt.title('template 1')
plt.figure()
plt.imshow(plt.imread('temp2.jpg'))
plt.title('template 2')
plt.show()

# 使用stylepro_artistic进行风格转换
result=stylepro_artistic.style_transfer(paths=[{'content':'example.jpg','styles':['temp1.jpg']}])
plt.figure()
plt.imshow(result[0]['data'])
plt.title('transfer via template 1')
result=stylepro_artistic.style_transfer(paths=[{'content':'example.jpg','styles':['temp2.jpg']}])
plt.figure()
plt.imshow(result[0]['data'])
plt.title('transfer via template 2')
result=stylepro_artistic.style_transfer(paths=[{'content':'example.jpg','styles':['temp1.jpg','temp2.jpg']}])
plt.figure()
plt.imshow(result[0]['data'])
plt.title('transfer via template 1 & 2')
plt.show()