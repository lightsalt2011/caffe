from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


img=np.array(Image.open('/home/lvfeng/trunk/caffe-refs/caffe/examples/images/cat.jpg'))
#img=Image.open('/home/lvfeng/trunk/caffe-refs/caffe/examples/images/cat.jpg')

rows,cols,dims=img.shape
for i in range(5000):
        x=np.random.randint(0,rows)
        y=np.random.randint(0,cols)
        img[x,y,:]=255
                    
plt.figure("beauty")
plt.imshow(img)
plt.axis('off')
plt.show()



