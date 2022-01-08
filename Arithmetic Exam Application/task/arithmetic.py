def first_massege():
	while True:
		print('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29''')
		try:
			ansower = int(input())
		except ValueError:
			print('Incorrect format.')
		else:
			if ansower == 1 or ansower == 2:
				return ansower
			else:
				print('Incorrect format.')



def arithmetic_calc():
	import random
	count = 0
	for i in range(5):
		a = random.randint(2, 9)
		b = random.randint(2, 9)
		s = random.choice('+-*')
		q = str(a) + ' ' + s + ' ' + str(b)
		print(q)
		n = q.split()
		if n[1] == '+':
			res = int(n[0]) + int(n[2])
		elif n[1] == '-':
			res = int(n[0]) - int(n[2])
		elif n[1] == '*':
			res = int(n[0]) * int(n[2])
		while True:
			try:
				ansower = int(input())
			except ValueError:
				print('Incorrect format.')
			else:
				print(('Wrong!', 'Right!')[res == ansower])
				if res ==ansower:
					count += 1
					break
				else:
					break
	return count

def integral_squares():
	import random
	lst = list(range(11, 30))
	n_lst = random.sample(lst, 5)
	count = 0
	for i in n_lst:
		print(i)
		res = i ** 2
		while True:
			try:
				ansower = int(input())
			except ValueError:
				print('Incorrect format.')
			else:
				print(('Wrong!', 'Right!')[res == ansower])
				if res == ansower:
					count += 1
					break
				else:
					break
	return count
lavel = first_massege()

if lavel == 1:
	mark = arithmetic_calc()
	lavel_name = 'simple operations with numbers 2-9'
else:
	mark = integral_squares()
	lavel_name = 'integral squares 11-29'
print(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.')
ansower_file = input()
if ansower_file.lower() in ['yes', 'y']:
	print('What is your name?')
	name = input()
	with open('results.txt', 'a', encoding='utf-8') as result:
		print(f'{name}: {mark}/5 in level {lavel} ({lavel_name}).', file=result)
	print('The results are saved in "results.txt"')
else:
	exit()

