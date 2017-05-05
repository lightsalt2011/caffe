from PIL import Image
import matplotlib.pyplot as plt

img=Image.open('/home/lvfeng/trunk/caffe-refs/caffe/examples/images/cat.jpg')
plt.figure("cat")
plt.axis('on')
plt.imshow(img)

print img.size
print img.mode
print img.format
img.save('cat2.png')

plt.show()

