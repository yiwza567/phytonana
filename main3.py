from scipy.io import loadmat
import matplotlib.pyplot as plt
mnist_raw=loadmat("mnist-original.mat")
##print(mnist_raw)##all data
mnist={
"data":mnist_raw["data"],
"target":mnist_raw["label"][0]
}
x=mnist["data"]
y=mnist["target"]
##x,y=mnist["data"],mnist["target"]
##print(mnist["data"].shape)
number = x[15000]
number_image=number.reshape(28,28)
print(x.shape)
##print(y) number all
print(y[15000])
plt.imshow(
number_image,
cmap =plt.cm.binary,
interpolation="nearest")
plt.show()