from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('/home/lvfeng/trunk/caffe-refs/caffe/examples/images/cat.jpg')

plt.figure("beauty")
plt.subplot(1,2,2), plt.title('origin')
plt.imshow(img),plt.axis('off')

box=(80,100,260,300)
roi=img.crop(box)
plt.subplot(1,2,1), plt.title('roi')
plt.imshow(roi),plt.axis('off')
plt.show()
