#Import stuff
import random

#Variables
def keygen():
	unencrypted = []
	encrypted = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	key = []
	sum = 0
	value = random.randint(-100000000, 100000000)

	#Generate the unencrypted
	for i in range(16):
		randomInt = random.randint(-100000000, 100000000)
		sum += randomInt
		unencrypted.append(randomInt)
	
	#Generate final number
	unencrypted.append(value - sum)
	
	#Encrypt stuff
	encrypted[0] = unencrypted[1] + unencrypted[2] + unencrypted[7]
	encrypted[1] = unencrypted[0] + unencrypted[3] + unencrypted[3]
	encrypted[2] = unencrypted[0] + unencrypted[3] + unencrypted[4]
	encrypted[3] = unencrypted[1] + unencrypted[2] + unencrypted[5]
	encrypted[4] = unencrypted[2] + unencrypted[7] + unencrypted[5]
	encrypted[5] = unencrypted[3] + unencrypted[4] + unencrypted[6]
	encrypted[6] = unencrypted[1] + unencrypted[5] + unencrypted[8]
	encrypted[7] = unencrypted[0] + unencrypted[4] + unencrypted[9]
	encrypted[8] = unencrypted[6] + unencrypted[11] + unencrypted[15]
	encrypted[9] = unencrypted[7] + unencrypted[10] + unencrypted[14]
	encrypted[10] = unencrypted[9] + unencrypted[12] + unencrypted[11]
	encrypted[11] = unencrypted[8] + unencrypted[13] + unencrypted[10]
	encrypted[12] = unencrypted[10] + unencrypted[14] + unencrypted[13]
	encrypted[13] = unencrypted[11] + unencrypted[12] + unencrypted[15]
	encrypted[14] = unencrypted[9] + unencrypted[12] + unencrypted[15]
	encrypted[15] = unencrypted[8] + unencrypted[13] + unencrypted[14]
	
	#Generate a key
	for i in range(16):
		key.append(encrypted[i] - unencrypted[i])
	
	#Return encrypted
	return(key)

def encrypt(value, key):
	#Generate unencrypted
	sum = 0
	unencrypted = []
	for i in range(15):
		randomInt = random.randint(-100000000, 100000000)
		sum += randomInt
		unencrypted.append(randomInt)
	unencrypted.append(value - sum)
	
	#Encrypt it
	encrypted = []
	for i in range(16):
		encrypted.append(unencrypted[i] + key[i])
	
	#Return a tuple
	return((encrypted, key))

def decrypt(encrypted, key):
	#Decrypt stuff
	decrypted = 0
	for i in range(16):
		decrypted += encrypted[i] - key[i]
	
	#Return the decrypted value
	return(decrypted)
