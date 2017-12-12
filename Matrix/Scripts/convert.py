import binascii
import numpy as np
import h5py


basefilePath = "/home/shreya/anaconda2/lib/python2.7/site-packages/acoular/-35,75/mic_16000_s16le_channel_"

L =  [[0 for n in range(160000)] for m in range(8)]

for i in range(8):
	filePath = basefilePath + str(i) + ".raw"
	file = open(filePath, "rb")
	count = 0
	

	with file:
		while count<160000:
		    byte = file.read(1)
		    
		    hexadecimal = binascii.hexlify(byte)
		    decimal = int(hexadecimal, 16)
#		    binary = bin(decimal)[2:].zfill(8)
                  
		    L[i][count]=decimal
                    count+=1

I = np.matrix(L)

I = (I-255)/25.6

I_trans = I.transpose()
#print(I_trans)

hf= h5py.File('-35,75.h5','w')
hf.create_dataset('time_data',data=I_trans)

hf.close()

