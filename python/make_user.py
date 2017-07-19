import string
import random as rd

def gen_names(seed, dictionary, output):
	rd.seed(seed)
	f=open(dictionary, 'r')
	o=open(output, 'w')
	words=f.readlines()
	for i in range(0,10):#number of username/password combinations to be generated
		num_words=rd.randint(1,3)
		user=""
		for j in range(0, num_words): #make username with random words from dictionary
			part=words[rd.randint(0,len(words))]
			if (j<num_words-1):
				user+=part.replace("\n","_")
			else:
				user+=part.replace("\n", "")
		add_num=rd.randint(0,1)
		while(add_num): #add random number of digits to end of username
			user+=str(rd.randint(0,10))
			add_num=rd.randint(0,1)
		#next, make a password
		num_chars=rd.randint(10,20)
		passw=""
		alphabet = string.ascii_letters+string.digits
		for j in range(0, num_chars):
			passw+=(rd.choice(alphabet))
		user_pass=user+":"+passw+"\n"
		o.write(user_pass)