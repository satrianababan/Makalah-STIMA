import string
from tkinter import *
import tkinter as tk
import random
from collections import deque

width = 13
height = 13

global score
score = 0

def put_word(word, grid):
    dir = random.choice([[1, 0], [0, 1], [1, 1]])
    x_size = width if dir[0] == 0 else width - len(word)
    y_size = height if dir[1] == 0 else height - len(word)

    x = random.randrange(0, x_size)
    y = random.randrange(0, y_size)

    for i in range(0, len(word)):
        grid[y + dir[1] * i][x + dir[0] * i] = word[i]
    return grid

words = ['TUPAI', 'GAJAH', 'MUSANG', 'ZEBRA', 'MONYET']

grid = [[random.choice(string.ascii_uppercase) for i in range(0, width)] for j in range(0, height)]

for word in words:
    grid = put_word(word, grid)

def startwin():
    top = Toplevel()
    top.title('Word Search Game')
    head = Label(top, text="TEMUKAN NAMA HEWAN!!", font=('helvetica', 30, 'bold', 'underline'), fg="#3F3F3F").grid()
    for i in range(width):
        lb3 = Label(top, text=' '.join(grid[i]), font=('gothic', 20, 'bold'), fg='#3E3F64').grid()

    text_input = StringVar()

    sc = Label(top, text=('                            SCORE : ' + str(score) + '                             '), bg='#3F3F3F', fg='white', font=('helvetica', 13, 'bold'))
    sc.grid()

    def btnClick():
        global score
        x = ans.get()
        print(x)

        if bfs(grid, x):
            print("BFS: Kata ditemukan")
            score += 10
            sc.config(text=('                            SCORE : ' + str(score) + '                             '))
            print(score)
        else:
            if x in words:
                print("Bruteforce : Kata ditemukan")
                score += 10
                sc.config(text=('                            SCORE : ' + str(score) + '                             '))
                print(score)
            else:
                print("Kata tidak ditemukan")
                print(score)

            text_input.set("")

    text_input.set("")

    ans = Entry(top, font=('helvetica', 30), bg='#3E3F64', fg='white', bd=10, justify='left', textvariable=text_input, insertwidth=6)
    ans.grid()

    check = Button(top, font=('helvetica', 8, 'bold'), text='CHECK', padx=220, pady=8, bd=4, command=btnClick).grid()

    hint0 = Label(top, font=('helvetica', 15, 'bold'),
                  text=">>>>>> Hints <<<<<<", fg='#3E3F64', anchor="center").grid()
    hint1 = Label(top, font=('helvetica', 9, 'bold'), text="1. Aku sangat besar, tapi aku bukan raja", fg='#125E00').grid()
    hint2 = Label(top, font=('helvetica', 9, 'bold'), text="2. Aku memandang rendah hewan lainnya", fg='#125E00').grid()
    hint3 = Label(top, font=('helvetica', 9, 'bold'), text="3. Aku sangat lincah bergerak di pohon", fg='#125E00').grid()
    hint4 = Label(top, font=('helvetica', 9, 'bold'), text="4. Kotoranku dapat dijadikan luwak", fg='#125E00').grid()
    hint5 = Label(top, font=('helvetica', 9, 'bold'), text="5. Aku suka makan pisang ", fg='#125E00').grid()

def bfs(grid, word):
    queue = deque()

    for i in range(height):
        for j in range(width):
            if grid[i][j] == word[0]:
                queue.append((i, j, 0))

    while queue:
        i, j, idx = queue.popleft()

        if idx == len(word) - 1:
            return True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < height and 0 <= nj < width and grid[ni][nj] == word[idx + 1]:
                queue.append((ni, nj, idx + 1))

    return False

h = 300
w = 350

root = Tk()
root.title('WordSearch')

canvas = tk.Canvas(root, height=h, width=w).grid()
frame = tk.Frame(root, bg='#3E3F64', height=h, width=w)
frame.place(relwidth=1, relheight=1)
lb1 = tk.Label(frame, font=('aharoni', 35, 'bold'), text='  Word-Search', fg='white', bg='#3E3F64', anchor='center').grid(row=1, column=2)
start = tk.Button(frame, font=('helvetica', 20, 'bold'), text='START', padx=12, pady=8, bd=8, bg='#40AF45', command=lambda: startwin()).grid(row=3, column=2, padx=30, pady=10)
quit = tk.Button(frame, font=('helvetica', 20, 'bold'), text=' QUIT ', padx=12, pady=8, bd=8, bg='#EE2E2E', command=lambda: root.destroy()).grid(row=5, column=2, padx=30, pady=10)
lb2 = Label(root, text='Word-Search © Tugas Makalah STIMA', bg='#3E3F64').grid()
tk.mainloop()
