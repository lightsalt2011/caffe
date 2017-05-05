from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('/home/lvfeng/trunk/caffe-refs/caffe/examples/images/cat.jpg')
gray=img.convert('L')
plt.figure("beauty")
plt.imshow(gray,cmap='gray')
plt.axis('off')
plt.show()


from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('/home/lvfeng/trunk/caffe-refs/caffe/examples/images/cat.jpg')
gray=img.convert('L')
r,g,b=img.split()
pic=Image.merge('RGB',(r,g,b))
plt.figure("beauty")
plt.subplot(2,3,1), plt.title('origin')
plt.imshow(img),plt.axis('off')
plt.subplot(2,3,2), plt.title('gray')
plt.imshow(gray,cmap='gray'),plt.axis('off')
plt.subplot(2,3,3), plt.title('merge')
plt.imshow(pic),plt.axis('off')
plt.subplot(2,3,4), plt.title('r')
plt.imshow(r),plt.axis('off')
plt.subplot(2,3,5), plt.title('g')
plt.imshow(g),plt.axis('off')
plt.subplot(2,3,6), plt.title('b')
plt.imshow(b),plt.axis('off')
plt.show()
