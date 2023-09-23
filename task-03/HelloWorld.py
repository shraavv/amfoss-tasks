#Python program to print all the prime numbers upto n

def prime(n):
	if(n==1 or n==0):
		return False
	for i in range(2,n):
		if(n%i==0):
			return False

n=int(input("Enter a number- "))
for i in range(1,n+1):
	if(prime(i)!=False):
		print(i)
		
