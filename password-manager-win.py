import sqlite3
import time
import pickle
import random
import os
from cryptography.fernet import Fernet, MultiFernet

def initial():
	from cryptography.fernet import Fernet, MultiFernet
	import pickle

	key = Fernet.generate_key()
	key2 = Fernet.generate_key()

	pickle.dump(key, open( "1.p", "wb" ) )
	pickle.dump(key2, open( "2.p", "wb" ) )

	key = pickle.load( open( "1.p", "rb" ) )
	key2 = pickle.load( open( "2.p", "rb" ) )

	pickle.dump(False, open( "init.p", "wb" ) )
	print("Keys Generated Successfully!")

	fernet = Fernet(key)
	default = "root"
	endefault = fernet.encrypt(default.encode())
	pickle.dump(endefault, open( "password.p", "wb" ) )

	pickle.dump(True, open( "init.p", "wb" ) )
	print("Password Created (Default: root)")
	print("Please Restart This Program")
	input()


def read():
	try:
		key2 = pickle.load( open( "2.p", "rb" ) )
		fernet = Fernet(key2)
		conn = sqlite3.connect('pass.db')
		c = conn.cursor()
		print("What Service?:")
		entered_text=input()
		c.execute("SELECT * FROM Info WHERE Service=?", (entered_text,))
		conn.commit()
		y = c.fetchone()
		Service = str(y[0])
		Ename = fernet.decrypt(y[1]).decode()
		Password = fernet.decrypt(y[2]).decode()
		print(f"Service: {Service}")
		print(f"Username/Email: {Ename}")
		print(f"Password: {Password}")
		input()
		conn.close()

	except:
		print("That Password Does Not Exist ¯\_(ツ)_/¯")
		input()

def write():
	key2 = pickle.load( open( "2.p", "rb" ) )
	fernet = Fernet(key2)
	conn = sqlite3.connect('pass.db')
	c = conn.cursor()
	print("What Service Is This For? (This Will Be Used To Search For Your Info!)")
	services_input = input()
	print("What Is You Email/Username Associated With The Account?")
	usermail_input = input()
	print("And Finally, What Is You Password? (This Is Stored Only On Your Local Drive)")
	password_input = input()
	c.execute("INSERT INTO Info (Service, Username, Password) values (?, ?, ?)", (services_input, fernet.encrypt(usermail_input.encode()), fernet.encrypt(password_input.encode())))
	conn.commit()
	conn.close()
	print("Write Successful!")
	input()

def change():
	key = pickle.load( open("1.p", "rb") )
	fernet = Fernet(key)
	initpassword = input("New Password: ")
	pickle.dump(fernet.encrypt(initpassword.encode()), open( "password.p", "wb" ) )
	print("Password changed!")

def gen():
	adj = ["Crunchy", "Sweet", "Sexy", "Drugged", "Disgusting", "Mega", "Fat", "Skinny", "Fast", "Ripoff", "Intentional", "Illegal", "Brave", "Bad", "Good", "Awesome", "Uncool", "Cool", "Dying", "Dark", "Evil", "Dictating", "Rusty", "Big", "Sleepy", "Loser", "Ugly", "Flying", "Poopy", "Useless", "Hopeless", "Secure", "Unsecure", "Funny", "Slow", "Wonderful", "Disturbing", "Kool", "Happy", "Depressing", "Upset", "Sad", "Highest", "Fearful", "Lunatic", "Brilliant"]
	nou = ["Alligator", "Ant", "Bear", "Bee", "Bird", "Camel", "Cheetah", "Cat", "Chicken", "Chickn", "Chimpanzee", "Cow", "Crocodile", "Dear", "Dog", "Dolphin", "Duck", "Eagle", "Elephant", "Fish", "Fly", "Fox", "Frog", "Giraffe", "Goat", "Goldfish", "Hamster", "Hippopotamus", "Horse", "Kangaroo", "Kitten", "Lion", "Lobster", "Monkey", "Octopus", "Owl", "Panda", "Pig", "Puppy", "Rabbit", "Rat", "Scorpion", "Seal", "Shark", "Sheep", "Snail", "Snake", "Spider", "Squirrel", "Tiger", "Turtle", "Wolf", "Zebra"]
	sym = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "()", "|", ",", ".", "/", "<", ">", "?", ":", ";", "~"]
	print("New Password:")
	print(f"{random.choice(adj)}{random.choice(nou)}{random.randint(1, 101)}{random.choice(sym)}")
	input()

def delete():
	conn = sqlite3.connect('pass.db')
	c = conn.cursor()
	print("Enter The Service Your Password You Want To Delete Is Associated With")
	delet = input()
	try:
		sql_update_query = """DELETE from Info where Service = ?"""
		c.execute(sql_update_query, (delet, ))
		conn.commit()
		print("Password Deleted!")
		c.close()
		input()

	except:
		print("Deletion Failed! This May Occur If The Password Does Not Exist Or Just An Error Made By The Dev.")
		input()

def main():
	conn = sqlite3.connect('pass.db')
	c = conn.cursor()
	print("LockUrPasswords")
	print("Mode?")
	print("Read: 1")
	print("Write: 2")
	print("Delete: 3")
	print("Change Password: 4")
	print("Password Generator: 5")
	mode = input()
	if mode == "1":
		read()

	elif mode == "2":
		write()

	elif mode == "3":
		delete()

	elif mode == "4":
		change()

	elif mode == "5":
		gen()

	else:
		print("Invalid Input!")
		input()


#Execution

init = pickle.load( open( "init.p", "rb" ) )
if init == True:
	key = pickle.load( open( "1.p", "rb" ) )
	fernet = Fernet(key)
	pwd = fernet.decrypt(pickle.load( open( "password.p", "rb" ) )).decode()
	pwd_in = input("Password?: ")
	if pwd == pwd_in:
		os.system('cls')
		main()

	else:
		print("incorrect password!")
		while True:
			input("Incorrect Password Relaunch To Try Again")

	while True:
		os.system('cls')
		main()
else:
	initial()
