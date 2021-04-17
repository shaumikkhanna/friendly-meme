from tkinter import *
import numpy as np


root = Tk()
root.title('Simple Calculator')
root.iconbitmap('calculator_23810.icns')


# Command functions

def insert_command(character):
	"""This function inserts a character into the main entry field. """
	current = e.get()
	ac_command()
	e.insert(0, current + character)

def ac_command():
	"""This function clears the main entry field. """
	e.delete(0, END)

def del_command():
	"""This function removes one character from the end of the main entry field. """
	current = e.get()
	ac_command()
	e.insert(0, current[:-1])

def equals_command():
	"""This function computes the result and puts it in the main entry field, only applicable in the basic mode. """
	
	# Gets the current equation from the main entry field and clears it. 
	current = e.get()
	ac_command()
	
	# Tries to solve the current equation
	try:
		answer = eval(current)
	except Exception as msg:
		e.insert(0, msg)

	# Displays answer on the main entry field
	e.insert(0, answer)

def frequency_checkbox_command():
	"""This function adds/removes the frequency field in the stats mode depending on the state of the freq_checkbox checkbox. """
	if freq_checkbox_bool.get():
		
		label_freq.grid(row=3, column=0)
		entry_freq.grid(row=3, column=1, columnspan=4)

	else:
		label_freq.grid_forget()
		entry_freq.grid_forget()

def stats_calculations(v1, v2, f):

	try:
		v1 = np.array(v1.split(','), dtype=float)
	except ValueError:
		v1 = None

	try:
		v2 = np.array(v2.split(','), dtype=float)
	except ValueError:
		v2 = None

	try:
		f = np.array(f.split(','), dtype=int)
	except ValueError:
		f = None

	
	if v1 is not None:

		if f is not None:
			new_v1 = []
			for x_value, freq in zip(v1, f):
				new_v1 += [x_value] * freq
			v1 = np.array(new_v1)

		stats_answers = [
			f'Mean of x: {v1.mean()}',
			f'Sum of x: {v1.sum()}',
			f'Sum of squared x: {(v1**2).sum()}',
			f'Population Variance of x: {v1.var()}',
			f'Population Standard deviation of x: {v1.std()}',
			f'Sample Variance of x: {v1.var(ddof=1)}',
			f'Sample Standard deviation of x: {v1.std(ddof=1)}',
			f'Number of elements of x: {len(v1)}\n'
			f'Minimum of x: {min(v1)}',
			f'First Quartile of x: {np.quantile(v1, 0.25)}',
			f'Median of x: {np.quantile(v1, 0.5)}',
			f'Third Quartile of x: {np.quantile(v1, 0.75)}',
			f'Interquartile range of x: {np.quantile(v1, 0.75) - np.quantile(v1, 0.25)}',
			f'Maximum of x: {max(v1)}'
		]

		if v2 is not None:
			stats_answers += [
				f'Mean of y: {v2.mean()}',
				f'Sum of y: {v2.sum()}',
				f'Sum of squared y: {(v2**2).sum()}',
				f'Population Variance of y: {v2.var()}',
				f'Population Standard deviation of y: {v2.std()}',
				f'Sample Variance of y: {v2.var(ddof=1)}',
				f'Sample Standard deviation of y: {v2.std(ddof=1)}',
				f'Number of elements of y: {len(v2)}\n'
				f'Minimum of y: {min(v2)}',
				f'First Quartile of y: {np.quantile(v2, 0.25)}',
				f'Median of y: {np.quantile(v2, 0.5)}',
				f'Third Quartile of y: {np.quantile(v2, 0.75)}',
				f'Interquartile range of y: {np.quantile(v2, 0.75) - np.quantile(v2, 0.25)}',
				f'Maximum of y: {max(v2)}',
				f'Sum of x * y: {sum(v1 * v2)}',
				f'Sample covariance: {np.cov(v1, v2)[0, 1]}',
				f'Population covariance: {np.cov(v1, v2, bias=True)[0, 1]}',
				f"Pearson's Correlation: {np.corrcoef(v1, v2)[0, 1]}"
			]


	toplevel = Toplevel()
	stats_answers_label = Label(toplevel, text='\n'.join(stats_answers))
	stats_answers_label.pack()


# Functions for handling flow

def ClearScreen():
	"""This functions clears the entire window except for the main entry field named e and the main mode menu named mode_menu. """
	
	for l in root.grid_slaves(): # Destroying all widgets
		l.destroy()

	# Creating main entry field and main mode menu.

	global e	
	e = Entry(root, width=70, borderwidth=5)
	e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
	
	mode_menu = OptionMenu(root, MODE, 'Basic', 'Statistics', 'Distribution')
	mode_menu.grid(row=0, column=4)


def BasicFlow():

	# Creating buttons

	button_number1 = Button(root, text='1', width=18, height=10, command=lambda: insert_command('1'))
	button_number2 = Button(root, text='2', width=18, height=10, command=lambda: insert_command('2'))
	button_number3 = Button(root, text='3', width=18, height=10, command=lambda: insert_command('3'))
	button_number4 = Button(root, text='4', width=18, height=10, command=lambda: insert_command('4'))
	button_number5 = Button(root, text='5', width=18, height=10, command=lambda: insert_command('5'))
	button_number6 = Button(root, text='6', width=18, height=10, command=lambda: insert_command('6'))
	button_number7 = Button(root, text='7', width=18, height=10, command=lambda: insert_command('7'))
	button_number8 = Button(root, text='8', width=18, height=10, command=lambda: insert_command('8'))
	button_number9 = Button(root, text='9', width=18, height=10, command=lambda: insert_command('9'))
	button_number0 = Button(root, text='0', width=18, height=10, command=lambda: insert_command('0'))

	button_plus = Button(root, text='+', width=18, height=10, command=lambda: insert_command('+'))
	button_minus = Button(root, text='-', width=18, height=10, command=lambda: insert_command('-'))
	button_asterisk = Button(root, text='*', width=18, height=10, command=lambda: insert_command('*'))
	button_slash = Button(root, text='/', width=18, height=10, command=lambda: insert_command('/'))

	button_DEL = Button(root, text='<-', width=18, height=10, command=del_command)
	button_AC = Button(root, text='AC', width=18, height=10, command=ac_command)

	button_decimal = Button(root, text='.', width=18, height=10, command=lambda: insert_command('.'))
	button_equals = Button(root, text='=', width=55, height=10, command=equals_command)


	# Placing buttons

	button_number7.grid(row=1, column=0)
	button_number8.grid(row=1, column=1)
	button_number9.grid(row=1, column=2)
	button_DEL.grid(row=1, column=3)
	button_AC.grid(row=1, column=4)

	button_number4.grid(row=2, column=0)
	button_number5.grid(row=2, column=1)
	button_number6.grid(row=2, column=2)
	button_asterisk.grid(row=2, column=3)
	button_slash.grid(row=2, column=4)

	button_number1.grid(row=3, column=0)
	button_number2.grid(row=3, column=1)
	button_number3.grid(row=3, column=2)
	button_plus.grid(row=3, column=3)
	button_minus.grid(row=3, column=4)

	button_number0.grid(row=4, column=0)
	button_decimal.grid(row=4, column=1)
	button_equals.grid(row=4, column=2, columnspan=3)


def StatisticsFlow():
	
	# Create and place var1 and var2 labels and entry fields

	label1 = Label(root, text='Var1: ')
	entry_var1 = Entry(root, width=70, borderwidth=5)
	label2 = Label(root, text='Var2: ')
	entry_var2 = Entry(root, width=70, borderwidth=5)

	label1.grid(row=1, column=0)
	entry_var1.grid(row=1, column=1, columnspan=4)
	label2.grid(row=2, column=0)
	entry_var2.grid(row=2, column=1, columnspan=4)
	

	# Create and place the frequency checkbox and the frequency label and entry field

	global freq_checkbox_bool, label_freq, entry_freq
	label_freq = Label(root, text='Freq: ')
	entry_freq = Entry(root, width=70, borderwidth=5)
	
	freq_checkbox_bool = IntVar()
	freq_checkbox = Checkbutton(
		root, text='Show frequency field', variable=freq_checkbox_bool, 
		onvalue=1, offvalue=0, command=frequency_checkbox_command)
	freq_checkbox.grid(row=4, column=0, pady=10)


	# Create and place Button for calculation

	stats_calculate_button = Button(root, text='Calculate!', width=20, command=lambda: stats_calculations(entry_var1.get(), entry_var2.get(), entry_freq.get()))
	stats_calculate_button.grid(row=4, column=3, columnspan=2, pady=10)


def DistributionFlow():
	pass

def ChangeFlow(*args):

	ClearScreen()
	
	current_mode = MODE.get()

	if current_mode == 'Basic':
		BasicFlow()

	if current_mode == 'Statistics':
		StatisticsFlow()

	if current_mode == 'Distribution':
		DistributionFlow()


MODE = StringVar()
MODE.trace_add('write', ChangeFlow)
MODE.set('Basic')

ChangeFlow()

root.mainloop()

