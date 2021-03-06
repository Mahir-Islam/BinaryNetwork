import torch
import matplotlib.pyplot as plt
import cv2
import numpy as np
from tkinter import *

def sig(x):
	return 1/(1+torch.exp(-x))

def simple_nn(data, weights, bias):
	return sig((data@weights)+bias)

def show_image(img):
	plt.imshow(img)
	plt.xticks([])
	plt.yticks([])
	plt.show()

B = torch.tensor([[-0.7091]], requires_grad=True)
W = torch.tensor([[-5.0352e-01], [-7.2384e-01], [ 2.5644e-01], [-8.8277e-02], [-5.2236e-01], [-1.6186e+00], [-2.8558e-01], [-1.7915e+00], [ 1.9132e-01], [ 1.2192e+00], [ 1.3796e-01], [-1.0816e-01], [ 5.3258e-01], [-1.1072e+00], [-1.1900e+00], [ 4.6146e-01], [-1.2224e+00], [ 6.4878e-01], [-2.2190e+00], [-2.3820e+00], [ 4.8459e-02], [ 2.8405e-01], [-1.2463e+00], [-9.0866e-01], [ 4.9671e-01], [-5.5760e-02], [-1.6597e+00], [ 7.5880e-01], [-6.6177e-01], [ 6.3726e-01], [-7.5259e-01], [ 1.6537e+00], [ 9.2823e-01], [-6.6192e-01], [ 1.7108e-01], [-1.1798e+00], [ 8.9779e-01], [-4.6235e-01], [ 6.0125e-01], [-1.9764e-02], [ 7.6505e-02], [-8.9364e-01], [ 1.9813e-01], [ 8.6026e-01], [ 1.7700e+00], [ 9.9758e-02], [ 8.9907e-01], [-4.1829e-01], [-5.1763e-01], [ 9.5496e-01], [-4.1881e-01], [-3.4973e-01], [ 8.5183e-01], [-2.2882e+00], [ 5.8354e-03], [ 6.0865e-01], [ 2.4051e+00], [ 5.5721e-01], [ 5.4697e-01], [ 3.9291e-01], [ 1.0439e+00], [ 9.6033e-01], [ 1.7731e-01], [-1.0176e+00], [ 1.3945e+00], [ 1.0544e+00], [-3.8701e-01], [ 5.5367e-01], [-1.7920e+00], [-9.6868e-01], [ 8.2358e-01], [ 7.0274e-01], [ 8.4363e-01], [ 6.8886e-01], [-2.5274e-01], [-7.9613e-01], [ 4.2684e-01], [-7.7471e-01], [-1.0080e-01], [-1.5327e+00], [ 4.7076e-01], [-1.2210e+00], [-1.2247e+00], [-6.0815e-01], [-3.9406e-01], [ 1.1734e+00], [ 1.2412e+00], [ 2.3667e-01], [ 7.3989e-01], [-1.0415e+00], [ 2.0643e+00], [-5.9976e-01], [-2.0044e+00], [-2.3523e-01], [ 1.3028e+00], [-1.6528e+00], [ 1.2725e+00], [ 1.1018e+00], [-1.8871e-01], [ 1.8355e+00], [-4.3191e-01], [ 6.9087e-01], [ 3.2648e-02], [-1.0334e+00], [ 1.1203e-01], [-2.4357e+00], [-1.0615e+00], [-2.8616e-01], [ 7.8091e-02], [-9.4636e-02], [-4.1812e-01], [ 1.0052e+00], [-1.2080e+00], [-3.8644e-01], [ 5.5528e-01], [ 9.5455e-01], [-2.2948e+00], [-2.1784e-01], [-1.4004e+00], [-1.1717e+00], [ 1.3777e-01], [ 4.5355e-01], [-1.3831e+00], [ 1.9970e-01], [ 1.0170e+00], [-3.5519e-01], [ 4.6010e-01], [-1.3528e+00], [-2.2488e-01], [-2.1801e+00], [-9.1971e-02], [ 5.4162e-01], [ 6.9115e-01], [-4.9242e-01], [ 1.3283e+00], [ 2.1644e-01], [-1.2984e+00], [-2.0424e-01], [-4.7108e-01], [-1.0885e+00], [ 6.6226e-01], [-1.0024e+00], [-8.0406e-01], [-1.5823e-01], [ 3.1127e-01], [ 3.4781e-01], [ 2.4941e-01], [-1.1182e+00], [ 1.8499e+00], [-3.0775e-01], [-4.4587e-01], [-4.1398e-01], [ 1.7943e+00], [ 3.1548e-01], [ 1.4729e+00], [ 5.8473e-01], [-9.3713e-02], [ 1.2891e+00], [-9.9773e-02], [-6.5139e-01], [-3.1071e-01], [ 6.7849e-01], [ 1.5062e-01], [ 1.5904e+00], [ 3.1618e-01], [-9.1526e-01], [-9.6836e-01], [ 1.1466e+00], [ 8.2816e-01], [ 3.8028e-01], [-8.9699e-01], [-7.9790e-01], [ 7.0975e-01], [-1.8472e-01], [-4.6149e-01], [ 1.3620e+00], [-3.4509e-01], [-1.7686e+00], [ 1.0029e+00], [-8.7868e-01], [-1.5094e+00], [ 7.7710e-01], [-1.1232e+00], [-7.3024e-01], [ 6.2198e-01], [ 3.0140e-01], [-2.9729e-01], [-1.6801e+00], [ 1.1248e+00], [ 5.1228e-01], [-3.4800e-01], [-1.3487e-01], [ 1.1201e-01], [-1.3872e-01], [-1.0854e+00], [ 1.4770e+00], [-3.1301e-01], [ 1.4039e+00], [ 5.2688e-01], [ 3.2198e-01], [-8.8799e-01], [-1.0944e+00], [-1.4724e-01], [-1.0642e+00], [-3.9472e-01], [ 2.0651e+00], [-9.6201e-01], [-5.0435e-01], [-5.5361e-01], [ 8.1469e-01], [-5.6994e-01], [ 1.0189e+00], [ 5.7076e-01], [-6.1224e-01], [-8.5050e-01], [-8.8798e-01], [-9.2837e-02], [-6.2434e-01], [ 7.4346e-03], [ 5.0419e-01], [ 4.9420e-01], [ 1.2193e+00], [ 4.9183e-01], [ 8.8873e-01], [-6.6542e-01], [ 1.2326e+00], [-8.6736e-01], [-9.2319e-01], [-2.4576e-01], [ 1.1520e+00], [ 2.3730e-01], [-7.1893e-01], [ 4.5786e-01], [-2.5858e-02], [-8.5812e-01], [-1.9927e-01], [-8.4820e-01], [-1.3390e+00], [ 7.8105e-02], [-6.0044e-01], [-2.3023e-01], [-6.0475e-01], [ 1.9437e+00], [ 3.8868e-01], [ 1.1679e+00], [ 1.0604e+00], [ 3.7734e-01], [ 1.7257e+00], [ 8.1174e-01], [-5.7841e-01], [ 4.8592e-01], [ 1.1054e+00], [-5.2404e-02], [ 6.4715e-01], [-1.1011e+00], [-1.6213e+00], [ 3.7487e-01], [-1.7955e-03], [ 4.3632e-01], [ 1.0090e+00], [ 1.9497e+00], [-9.4379e-01], [-7.1206e-01], [ 1.1777e+00], [ 6.5688e-01], [ 3.8644e-01], [ 1.0155e-01], [ 1.2911e+00], [ 7.4525e-01], [ 7.1420e-01], [-4.6194e-01], [-1.3455e+00], [-1.0128e+00], [-2.0605e-01], [ 2.8584e-01], [-3.0989e-01], [-1.5839e+00], [ 1.3519e-01], [-1.3765e-01], [ 1.0426e+00], [-5.6456e-01], [ 1.0852e-01], [-2.6114e-01], [ 1.6528e+00], [-1.2788e+00], [ 2.0954e+00], [-7.4728e-02], [ 3.0438e-01], [ 8.5879e-01], [ 5.7712e-01], [ 4.9348e-01], [ 4.5477e-01], [-9.7997e-01], [-9.2054e-01], [ 1.0235e+00], [-1.0010e-01], [ 4.8289e-01], [-7.2675e-01], [ 5.2885e-01], [-1.4566e+00], [ 5.3245e-01], [-5.0413e-01], [ 1.2391e+00], [ 2.6425e-01], [-5.3946e-01], [-4.6192e-01], [-8.2936e-01], [ 2.0121e+00], [-4.9117e-01], [-8.9198e-01], [ 7.4968e-01], [-2.8906e-02], [-1.5743e+00], [ 2.4068e+00], [-7.6556e-01], [-1.4599e+00], [ 6.9191e-01], [-7.3754e-01], [ 4.0076e-01], [-3.6343e-01], [ 1.0326e+00], [-3.8314e-01], [ 1.0256e+00], [ 4.1700e-01], [-4.4569e-01], [ 1.4136e+00], [ 1.3802e+00], [ 3.8472e-01], [ 8.0285e-01], [-7.5973e-01], [-1.9590e+00], [-1.9670e+00], [-1.3440e+00], [ 1.9595e-01], [ 1.0816e-01], [ 1.2351e+00], [-5.2955e-01], [ 6.2780e-01], [ 1.9086e+00], [-4.1897e-01], [ 8.1871e-01], [-4.3189e-01], [ 8.3313e-01], [-6.9981e-01], [-9.4983e-01], [ 6.6233e-01], [-5.9311e-02], [ 4.8091e-01], [-1.4468e-01], [ 5.4871e-01], [ 1.2843e+00], [ 7.7903e-01], [ 1.6545e+00], [-6.7311e-01], [ 1.4454e-01], [ 5.9832e-01], [ 7.2295e-01], [ 2.7847e-01], [-4.3978e-01], [-8.7878e-01], [ 5.1047e-01], [-1.6715e+00], [-7.8423e-01], [-8.0835e-01], [-6.5520e-01], [-7.6717e-01], [ 9.4573e-01], [-6.5120e-01], [ 1.3286e+00], [-7.0250e-01], [-5.8292e-01], [-9.3617e-01], [ 9.2616e-02], [-2.8557e-01], [ 3.5078e-01], [-5.7594e-01], [-7.6700e-01], [ 2.6123e+00], [ 6.9360e-01], [ 1.6677e-01], [ 2.5471e-01], [-4.8287e-01], [ 9.3408e-01], [-2.5663e+00], [ 4.8576e-03], [-1.1302e+00], [ 1.8229e+00], [ 1.8052e-01], [ 5.2057e-01], [-3.0503e-01], [-9.6773e-02], [-4.5562e-01], [ 2.2926e+00], [ 4.4637e-01], [-4.8028e-01], [-1.9558e+00], [ 4.8028e-01], [ 9.2180e-01], [-5.6136e-01], [ 4.0806e-01], [ 4.7236e-01], [ 1.0677e+00], [ 3.6800e-01], [ 1.3039e+00], [ 1.0541e-01], [ 7.1305e-02], [ 1.7899e-01], [ 1.5595e+00], [ 4.3953e-01], [-5.3443e-01], [-1.2874e+00], [ 4.3184e-01], [ 1.7360e-01], [-1.6967e-01], [-1.8032e+00], [-9.2068e-01], [ 1.7018e-01], [-2.0146e-01], [-1.0083e+00], [ 1.5294e+00], [-3.4485e-01], [ 9.7873e-01], [-1.2726e+00], [-6.4723e-02], [ 6.1491e-02], [-2.5190e+00], [ 1.5512e+00], [ 2.4984e-01], [-1.2561e+00], [-1.4235e+00], [-5.5514e-04], [ 4.5983e-01], [-9.7964e-01], [ 1.2215e+00], [ 1.4028e+00], [ 1.7935e+00], [ 4.8086e-01], [-1.0868e+00], [ 7.6986e-01], [-1.1143e-02], [ 1.1898e-02], [-1.3696e+00], [ 3.4997e-01], [-6.2849e-01], [-7.0882e-01], [-4.1345e-01], [-6.0872e-01], [-1.2043e+00], [-2.7696e-01], [ 9.4580e-02], [ 3.1951e-01], [ 1.0986e+00], [-1.4481e+00], [ 1.0979e+00], [-8.3285e-01], [-1.4130e+00], [-7.5378e-01], [-2.4791e+00], [-7.0831e-01], [-8.2130e-02], [ 7.2534e-01], [ 6.7720e-01], [ 1.1897e+00], [ 1.3618e+00], [-3.2287e-01], [-1.5180e+00], [-5.9292e-01], [-2.1087e+00], [-1.2362e+00], [ 2.8323e-01], [-1.3821e+00], [ 1.3564e+00], [ 8.1805e-02], [-1.2687e+00], [ 5.5485e-01], [ 2.4534e-01], [ 6.6173e-01], [ 7.7259e-02], [ 6.1037e-01], [ 1.4108e+00], [ 2.2583e-01], [ 6.8469e-02], [-1.0221e+00], [ 8.7573e-01], [ 2.1355e+00], [-1.3818e+00], [-9.0577e-01], [-1.2964e+00], [ 3.6937e-01], [ 5.1130e-01], [-6.6352e-01], [ 6.5326e-03], [-1.1648e+00], [-1.6215e+00], [ 8.9543e-01], [ 1.3647e+00], [ 7.7368e-02], [ 5.4353e-02], [-1.2686e+00], [ 2.2056e+00], [ 9.9316e-01], [-2.7147e-02], [ 1.8183e-01], [ 3.6762e-01], [ 2.1818e+00], [-3.0358e-01], [-6.5282e-01], [-5.6784e-01], [-1.1497e+00], [-4.3125e-01], [-1.3024e+00], [-7.9144e-01], [-8.9041e-01], [ 3.2981e-01], [ 4.7861e-01], [-3.5164e-01], [ 4.8849e-01], [ 7.5074e-01], [ 1.2200e+00], [ 1.1046e+00], [ 4.4142e-01], [ 4.2363e-01], [-1.1359e+00], [ 1.9624e-01], [ 1.6328e+00], [-2.5954e+00], [ 1.2197e+00], [-6.7381e-01], [-1.7259e+00], [ 9.1893e-01], [ 4.4912e-01], [-3.7301e-01], [-1.0710e+00], [-1.3600e+00], [ 7.0395e-01], [ 1.8802e+00], [ 2.7809e-01], [ 1.3198e+00], [-1.6858e+00], [-9.6802e-01], [-1.0545e+00], [-6.9117e-01], [ 5.8751e-02], [-1.7705e+00], [-6.3721e-01], [-1.1417e+00], [-1.2807e-01], [ 1.2417e+00], [-4.5309e-01], [-1.7265e+00], [-1.6490e+00], [-4.4031e-02], [ 5.7473e-01], [ 8.3605e-01], [ 1.6267e+00], [-1.3698e+00], [-5.5354e-01], [ 7.9991e-01], [ 7.1961e-01], [ 1.2956e+00], [ 2.4419e-01], [-3.8490e-01], [ 4.5864e-01], [-1.5339e-01], [-3.0209e-01], [ 3.8920e-01], [-1.6081e+00], [ 1.1122e+00], [ 1.1739e-01], [ 9.2381e-01], [ 7.7702e-01], [-2.4710e+00], [-8.4313e-01], [ 9.1220e-01], [-1.3205e+00], [ 2.8892e-01], [-4.4798e-01], [-2.9371e-01], [-1.6526e-01], [-2.1821e+00], [ 6.6137e-01], [-1.1786e+00], [ 1.5112e+00], [-1.6027e-01], [ 1.6502e+00], [ 1.4823e+00], [-5.7711e-01], [ 2.2014e-01], [ 2.0202e+00], [-2.9944e-01], [ 4.8279e-01], [-1.5479e+00], [-5.0169e-01], [ 3.2711e-01], [ 2.5671e-01], [-1.7245e-01], [ 1.1632e+00], [-1.3840e+00], [ 1.7130e+00], [ 1.5292e+00], [ 1.1183e+00], [-6.8201e-01], [ 4.1692e-01], [ 2.2519e-01], [-1.0101e+00], [ 9.9491e-01], [ 5.7822e-03], [ 3.3570e-01], [-6.3217e-01], [-4.7470e-01], [-1.8950e-01], [-5.1545e-01], [ 4.8223e-01], [ 3.8886e-01], [ 1.7821e-01], [-7.9980e-01], [ 5.8597e-01], [-1.5770e+00], [ 1.2830e+00], [-7.8664e-01], [-2.6568e-01], [ 1.1172e+00], [ 5.3299e-01], [-3.0128e+00], [-2.2326e-01], [-2.3536e-01], [-1.7173e+00], [ 3.6293e-01], [ 4.0210e-01], [ 1.7391e-01], [-2.1638e-01], [ 4.5445e-01], [-1.1965e+00], [-2.8846e-02], [-2.7038e-01], [-1.9229e+00], [ 1.0275e+00], [ 5.3974e-01], [ 5.7935e-01], [-1.3251e+00], [ 9.6763e-01], [ 8.3153e-01], [-6.7049e-01], [ 1.2108e+00], [ 8.3681e-01], [ 4.7446e-01], [-5.3157e-01], [ 2.3889e-01], [-1.4434e-01], [-1.1323e+00], [ 3.3011e-01], [ 4.5489e-01], [ 8.2224e-01], [-1.0662e-01], [-4.2606e-01], [-2.3286e+00], [-1.0548e+00], [-2.7555e-01], [-1.0988e+00], [-2.1430e-01], [-1.0934e+00], [ 8.4299e-01], [ 4.7085e-01], [ 3.2663e-01], [-7.6732e-01], [-9.8195e-01], [ 7.1849e-01], [ 9.2210e-01], [ 9.9640e-01], [ 1.2318e+00], [-6.4757e-01], [ 1.5439e+00], [ 5.3334e-03], [-5.4277e-01], [-1.0520e+00], [ 6.0246e-01], [ 1.2704e+00], [ 1.0264e+00], [ 5.4846e-01], [ 1.2122e+00], [-1.0037e+00], [ 6.9361e-01], [ 2.6784e-01], [-2.0841e-02], [-4.8641e-01], [ 7.9376e-01], [-8.9735e-01], [-5.3287e-01], [-1.2708e+00], [ 5.7607e-01], [-5.1935e-01], [ 1.0408e+00], [-4.7672e-01], [-3.4561e-01], [ 9.8765e-02], [ 2.3283e-01], [ 2.0402e+00], [-6.2748e-01], [ 1.6059e+00], [ 1.8927e+00], [-5.7609e-01], [ 5.6951e-01], [-1.0101e+00], [-5.9733e-01], [-8.0784e-01], [-1.3661e+00], [-1.3430e+00], [-9.2775e-01], [ 2.9218e-01], [-1.6692e-01], [-2.1629e-01], [-7.6875e-02], [-1.2615e+00], [ 5.1216e-01], [-6.5343e-01], [-1.2162e-01], [ 1.0334e-02], [-8.6473e-02], [ 1.6614e+00], [-6.0003e-01], [ 5.6115e-01], [-4.2526e-01], [-2.9323e-01], [ 1.5954e+00], [ 9.8086e-01], [ 5.2336e-01], [-3.6982e-01], [-2.4739e-01], [-9.4165e-01], [ 1.5300e+00], [ 8.8274e-01], [ 1.0187e+00], [ 9.2537e-02], [ 1.1137e+00], [ 8.0257e-01], [ 1.0267e+00], [-9.7517e-01], [-3.0257e-01], [ 3.8448e-01], [ 6.6368e-01], [ 5.8279e-02], [ 6.7571e-01], [-6.4106e-01], [ 8.3415e-01], [-5.9818e-01], [ 4.5696e-01], [ 6.7784e-02], [-1.3342e+00], [-1.0055e-02], [-3.3840e-01], [-8.7379e-01], [-1.5867e-01], [-1.1574e-01], [ 1.1860e-01], [-2.4092e-01], [-2.0311e+00], [ 3.5406e-01], [-1.3245e+00], [ 1.0561e+00], [ 1.1473e+00], [ 9.0049e-01], [-5.4709e-01], [ 3.5719e-01], [ 3.7776e-01], [ 3.7456e-02], [ 1.2342e+00], [ 4.2318e-01], [ 1.3980e+00], [-2.0451e+00], [-8.8626e-01], [ 5.0235e-01], [-1.2885e+00], [-2.8521e-01], [-4.2658e-01], [ 9.1631e-01], [ 2.6642e+00], [ 1.1732e+00], [ 8.8438e-01], [-1.9925e-02], [-5.2078e-01], [ 2.1050e+00], [-4.0873e-01], [ 1.3301e+00], [ 3.1458e-01]], requires_grad=True)

def image(filename,w=0):
	im = cv2.imread(filename)
	a = []
	b = []
	c = []
	for line in im:
		for pixel in line:
			a.append(sum(pixel)/(len(pixel)*255.0))
			b.append(sum(pixel)/(len(pixel)*255.0))
		c.append(b)
		b = []

	a = torch.tensor(a)
	a.shape
	c = torch.tensor(c)
	c.shape
	if w==1: #returns unflattened tensor
		return c.float()

	c = torch.flatten(c)
	c.shape
	return c.float()

root = Tk()
root.title("Binary neural network")
root.minsize(600,450)

TITLE = Label(root,text="Simple neural network",fg="#161648",bg="#fff",font="Arial 32")
TITLE.place(relx=0.5,rely=0.1,anchor='center')

InfoBox = Text(root, width=46,height=10, bg="white", fg="black", font="Arial 14")
InfoBox.place(relx=0.5, rely=0.45, anchor='center')

OPEN = Button(root,text="Open file",bg="#ccc",fg='#222',font="Arial 30",borderwidth=0,command=lambda: open())
OPEN.place(relx=0.5,rely=0.825,anchor='center')

def push(rng):
	InfoBox.insert(END,rng)

def replace(rng):
    InfoBox.delete(1.0,END)
    InfoBox.insert(END,rng)

def open():
	f = filedialog.askopenfilename()
	simple_nn(image(f),W,B)
	r = simple_nn(image(f),W,B)
	p = r.detach()[0][0].item()
	q = 1-p
	MSG = """There is a %s%% certainty that this value is 1.\nThere is a %s%% certainty that this value is 0.""" % (round(p*100,3),round(q*100,3))
	replace(MSG)
	show_image(image(f,1))

push('''Welcome to my first machine learning program :D\nMade by Mahir.\nYou will need a 28x28 image.\nThe background must be black and the foreground, white.\nIt will then return a predicition as to whether the number is a 1 or a 0.''')

root.mainloop()