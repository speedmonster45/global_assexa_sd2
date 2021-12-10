import streamlit as st
import pandas as pd
import datetime
from PIL import Image
#import 'C:\Users\speedmonster45\Documents\school work\ui code\backend\logs_file' as lf
#image = Image.open('sunrise.jpg')
#from flask import Flask
#initialization of app flagging for flask
#flag.session()
# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	
	"""Simple Login App"""
	st.write()
	st.title("GLOBAL ASSESZA UI")
	#if 'count' not in st.session_state:
     #    st.session_state.count = 0
      #   st.session_state.last_updated = datetime.time(0,0)

	#def update_counter():
	#	st.session_state.count += st.session_state.increment_value
	#	st.session_state.last_updated = st.session_state.update_time

	#with st.form(key='my_form'):
	#	st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
	#	st.number_input('Enter a value', value=0, step=1, key='increment_value')
	#	submit = st.form_submit_button(label='Update', on_click=update_counter)

	#st.write('Current Count = ', st.session_state.count)
	#st.write('Last Updated = ', st.session_state.last_updated)
	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		menu1 = ["logs","Apps","power"]
		choice = st.selectbox("Menu",menu1)
		if choice == "logs":
			st.dataframe(pd.DataFrame(
				np.random.randn(50, 20),
                		columns=('col %d' % i for i in range(20))))
		elif choice  == "apps":
			pass
		elif choice == "power":
			pass
	elif choice == "Login":

		st.subheader("Login Section")
		menu2 = ["login","sign up"]
		choice = st.selectbox("menu",menu2)
		if choice == "SignUp":
			st.subheader("Create New Account")
			new_user = st.text_input("Username")
			new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")



if __name__ == '__main__':
	main()
