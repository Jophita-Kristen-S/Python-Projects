import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

player = "X"
buttons = [[None]*3 for _ in range(3)]

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def click(row, col):
    global player

    if buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = player

    if check_winner():
        messagebox.showinfo("Game Over", f"{player} wins!")
        reset()
        return

    if is_draw():
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset()
        return

    player = "O" if player == "X" else "X"

def reset():
    global player
    player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""

for i in range(3):
    for j in range(3):
        btn = tk.Button(
            root,
            text="",
            font=("Arial", 24),
            width=5,
            height=2,
            command=lambda r=i, c=j: click(r, c)
        )
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

root.mainloop()