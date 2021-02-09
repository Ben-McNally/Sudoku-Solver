import os
from colorama import Fore

board = [
[0] * 9,
[0] * 9,
[0] * 9,
[0] * 9,
[0] * 9,
[0] * 9,
[0] * 9,
[0] * 9,
[0] * 9,
]

colours = [
Fore.WHITE,
Fore.RED,
Fore.LIGHTYELLOW_EX,
Fore.YELLOW,
Fore.GREEN,
Fore.CYAN,
Fore.BLUE,
Fore.MAGENTA,
Fore.WHITE,
]
c_float = 82.0

def print_board(_board):
	print("- " * 12)
	y_line = 0
	for y, row in enumerate(_board):
		x_line = 0
		print(Fore.WHITE+"| ", end="")
		for x, num in enumerate(row):
			c_num = int(x / 2) + int(y / 2)
			if c_num >= 9:
				c_num = c_num % 8
			colour = colours[c_num]
			if num != 0:
				print(f"{colour}{num} ", end="")
			else:
				print(f"{colour}  ", end="")
			x_line += 1
			if not x_line % 3:
				print(Fore.WHITE+"| ", end="")
		print()
		y_line += 1
		if not y_line % 3:
				print(Fore.WHITE+"- " * 13)

def fill_board(_board):
	for y, row in enumerate(_board):
		for x in range(len(row)):
			num = input("enter number: ")
			os.system("clear")
			try:
				_board[y][x] = int(num)
			except ValueError:
				_board[y][x] = 0

			print_board(_board)

def get_squares(x, y, _board):
	x = int(x / 3) * 3
	y = int(y / 3) * 3
	squares = []
	for _x in range(3):
		for _y in range(3):
			if _x != x and _y != y:
				squares.append(_board[y + _y][x + _x])

	return squares

def get_lines(x, y, board):
	x_line = []
	for _x in range(9):
		if _x != x:
			x_line.append(board[y][_x])

	y_line = []
	for _y in range(9):
		if _y != y:
			y_line.append(board[_y][x])

	return x_line + y_line

def get_next_square(x, y, _board):
	reached = False
	for _y in range(9):
		for _x in range(9):
			if reached:
				if _board[_y][_x] == 0:
					return _x, _y
			elif _x == x and _y == y:
				reached = True
	return None

def get_nums(x, y, _board):
	used_nums = get_squares(x, y, _board) + get_lines(x, y, _board)
	available_nums = [i for i in list(range(1, 10)) if i not in used_nums]
	try:
		available_nums.remove(0)
	except:
		pass
	return available_nums

def get_legal(x, y, _board):
	used_nums = get_squares(x, y, _board) + get_lines(x, y, _board)
	return _board[y][x] in used_nums

def fin(_board):
	print_board(_board)
	quit()

def copy_board(_board):
	return_board = []
	for ls in _board:
		return_board.append(ls[:])
	return return_board

def solve_board(x, y, _board):
	new_board = copy_board(_board)
	nums = get_nums(x, y, new_board)
	if not nums:
		return
	for num in nums:
		new_board[y][x] = num
		try:
			nx, ny = get_next_square(x, y, new_board)
		except:
			fin(new_board)
		solve_board(nx, ny, new_board)


if __name__ == "__main__":
	fill_board(board)
	solve_board(0, 0, board)
