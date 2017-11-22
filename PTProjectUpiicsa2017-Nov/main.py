from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

fp = Image.open('neu.jpg')
iar = np.asarray(fp)
plt.imshow(iar)
print (iar)
plt.show()
