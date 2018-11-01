#Import stuff
import random

def encrypt(value):
	#Variables
	unencrypted = []
	encrypted = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	sum = 0

	#Generate the unencrypted
	for i in range(15):
		randomInt = random.randint(-100000000, 100000000)
		sum += randomInt
		unencrypted.append(randomInt)
	
	#Generate final number
	unencrypted.append(value - sum)
	
	#Encrypt stuff
	encrypted[0] = unencrypted[1] + unencrypted[2] + unencrypted[7] + unencrypted[0]
	encrypted[1] = unencrypted[0] + unencrypted[3] + unencrypted[6] + unencrypted[1]
	encrypted[2] = unencrypted[0] + unencrypted[3] + unencrypted[4] + unencrypted[2]
	encrypted[3] = unencrypted[1] + unencrypted[2] + unencrypted[5] + unencrypted[3]
	encrypted[4] = unencrypted[2] + unencrypted[7] + unencrypted[5] + unencrypted[4]
	encrypted[5] = unencrypted[3] + unencrypted[4] + unencrypted[6] + unencrypted[5]
	encrypted[6] = unencrypted[1] + unencrypted[5] + unencrypted[8] + unencrypted[6]
	encrypted[7] = unencrypted[0] + unencrypted[4] + unencrypted[9] + unencrypted[7]
	encrypted[8] = unencrypted[6] + unencrypted[11] + unencrypted[15] + unencrypted[8]
	encrypted[9] = unencrypted[7] + unencrypted[10] + unencrypted[14] + unencrypted[9]
	encrypted[10] = unencrypted[9] + unencrypted[12] + unencrypted[11] + unencrypted[10]
	encrypted[11] = unencrypted[8] + unencrypted[13] + unencrypted[10] + unencrypted[11]
	encrypted[12] = unencrypted[10] + unencrypted[14] + unencrypted[13] + unencrypted[12]
	encrypted[13] = unencrypted[11] + unencrypted[12] + unencrypted[15] + unencrypted[13]
	encrypted[14] = unencrypted[9] + unencrypted[12] + unencrypted[15] + unencrypted[14]
	encrypted[15] = unencrypted[8] + unencrypted[13] + unencrypted[14] + unencrypted[15]
	
	#Return encrypted
	return(encrypted)

def decrypt(encrypted):
	#Variables
	decrypted = 0
	key = [1, 4, 11, 14]
	
	#Decrypt it
	for value in key:
		decrypted += encrypted[value]
	
	#Return the decrypted stuff
	return(decrypted)