import sqlite3
import time
import pickle
import random
import os


def read():
	try:
		conn = sqlite3.connect('pass.db')
		c = conn.cursor()
		print("What Service?:")
		entered_text=input()
		c.execute("SELECT * FROM Info WHERE Service=?", (entered_text,))
		conn.commit()
		y = c.fetchone()
		Service = str(y[0])
		Ename = str(y[1])
		Password = str(y[2])
		print(f"Service: {Service}")
		print(f"Username/Email: {Ename}")
		print(f"Password: {Password}")
		input()
		conn.close()

	except:
		print("That Password Does Not Exist ¯\_(ツ)_/¯")
		input()

def write():
	conn = sqlite3.connect('pass.db')
	c = conn.cursor()
	print("What Service Is This For? (This Will Be Used To Search For Your Info!)")
	services_input = input()
	print("What Is You Email/Username Associated With The Account?")
	usermail_input = input()
	print("And Finally, What Is You Password? (This Is Stored Only On Your Local Drive)")
	password_input = input()
	c.execute("INSERT INTO Info (Service, Username, Password) values (?, ?, ?)", (services_input, usermail_input, password_input))
	conn.commit()
	conn.close()
	print("Write Successful!")
	input()

def change():
	initpassword = input("New Password: ")
	pickle.dump(initpassword, open( "password.p", "wb" ) )
	print("password changed!")

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


pwd = pickle.load( open( "password.p", "rb" ) )
pwd_in = input("Password?: ")
if pwd == pwd_in:
	main()

else:
	print("incorrect password!")
	while True:
		input("Incorrect Password Relaunch To Try Again")

while True:
	os.system('cls')
	main()
