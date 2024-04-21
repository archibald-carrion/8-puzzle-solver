import tkinter as tk

class EightPuzzleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("8 Puzzle Game")
        
        # Create the tiles as a matrix
        self.tiles = [[None, None, None], [None, None, None], [None, None, None]]
        
        # Create the puzzle grid
        self.tile_1 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(tile_1))
        self.tile_1.grid(row=0, column=0, padx=5, pady=5)

        self.tile_2 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(tile_2))
        self.tile_2.grid(row=0, column=1, padx=5, pady=5)

        self.tile_3 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(3))
        self.tile_3.grid(row=0, column=2, padx=5, pady=5)
        
        self.tile_4 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(4))
        self.tile_4.grid(row=1, column=0, padx=5, pady=5)

        self.tile_5 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(5))
        self.tile_5.grid(row=1, column=1, padx=5, pady=5)

        self.tile_6 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(6))
        self.tile_6.grid(row=1, column=2, padx=5, pady=5)
        
        self.tile_7 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(7))
        self.tile_7.grid(row=2, column=0, padx=5, pady=5)

        self.tile_8 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(8))
        self.tile_8.grid(row=2, column=1, padx=5, pady=5)

        self.tile_9 = tk.Button(master, text=" ", width=5, height=2, command=lambda: self.click_tile(0))
        self.tile_9.grid(row=2, column=2, padx=5, pady=5)
        
        self.tiles = [[self.tile_1, self.tile_2, self.tile_3], [self.tile_4, self.tile_5, self.tile_6], [self.tile_7, self.tile_8, self.tile_9]]
        # Initialize the puzzle
        self.init_puzzle()


    def init_puzzle(self):
        # set the current state of the puzzle 
        self.current_state = [[1, 2, 3], [4, 5, 6], [7, 8, " "]]
        self.update_tiles()

    def update_tiles(self):
        # Update the tiles with the current state of the puzzle
        for i in range(3):
            for j in range(3):
                self.tiles[i][j].config(text=str(self.current_state[i][j]))
                #value = self.current_state[i][j]
                #self.tiles[i][j].config(text=str(value))

    def click_tile(self, button):
        # print("Button clicked")
        # print(button)

        # check if the button is next to the empty tile
        for i in range(3):
            for j in range(3):
                # print(self.tiles[i][j].cget("text"))
                #if str(self.tiles[i][j].cget("text")) == str(button):
                if self.tiles[i][j] == button:
                    print("Button found")
                    self.move_tile(i, j)
                    return

        
        # Handle clicks on tiles
        # for i in range(3):
        #     for j in range(3):

                # if self.tiles[i][j] == button:
                    # self.move_tile(i, j)
                    # return

    def move_tile(self, row, col):
        # Move the tile if possible
        # print("Moving tile")
        can_go_up = row > 0
        can_go_down = row < 2
        can_go_left = col > 0
        can_go_right = col < 2

        if can_go_up and self.tiles[row - 1][col].cget("text") == " ":
            buffer_tile = self.tiles[row][col]
            self.tiles[row][col] = self.tiles[row - 1][col]
            self.tiles[row - 1][col] = buffer_tile
            # label = self.tiles[row][col].cget("text")
            # self.tiles[row][col].config(text=" ")
            # self.tiles[row - 1][col].config(text=label)
            print("Moving tile up")
            # self.tiles[row][col], self.tiles[row - 1][col] = self.tiles[row - 1][col], self.tiles[row][col]
            return

        if can_go_down and self.tiles[row + 1][col].cget("text") == " ":
            buffer_tile = self.tiles[row][col]
            self.tiles[row][col] = self.tiles[row + 1][col]
            self.tiles[row + 1][col] = buffer_tile
            # label = self.tiles[row][col].cget("text")
            # self.tiles[row][col].config(text=" ")
            # self.tiles[row + 1][col].config(text=label)
            print("Moving tile down")
            # self.tiles[row][col], self.tiles[row + 1][col] = self.tiles[row + 1][col], self.tiles[row][col]
            return

        if can_go_left and self.tiles[row][col - 1].cget("text") == " ":
            buffer_tile = self.tiles[row][col]
            self.tiles[row][col] = self.tiles[row][col - 1]
            self.tiles[row][col - 1] = buffer_tile
            # label = self.tiles[row][col].cget("text")
            # self.tiles[row][col].config(text=" ")
            # self.tiles[row][col - 1].config(text=label)
            print("Moving tile left")
            # self.tiles[row][col], self.tiles[row][col - 1] = self.tiles[row][col - 1], self.tiles[row][col]
            return
        
        if can_go_right and self.tiles[row][col + 1].cget("text") == " ":
            buffer_tile = self.tiles[row][col]
            self.tiles[row][col] = self.tiles[row][col + 1]
            self.tiles[row][col + 1] = buffer_tile
            # label = self.tiles[row][col].cget("text")
            # self.tiles[row][col].config(text=" ")
            # self.tiles[row][col+1].config(text=label)
            print("Moving tile right")
            # self.tiles[row][col], self.tiles[row][col + 1] = self.tiles[row][col + 1], self.tiles[row][col]
            return

        print("Invalid move")
        # check if the empty tile is next to the clicked tile
        # if so, swap the two tiles
        #       

        # moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # for dr, dc in moves:
        #     new_row, new_col = row + dr, col + dc
        #     if 0 <= new_row < 3 and 0 <= new_col < 3 and self.current_state[new_row][new_col] == " ":
        #         self.current_state[row][col], self.current_state[new_row][new_col] = self.current_state[new_row][new_col], self.current_state[row][col]
        #         self.update_tiles()
        #         return

# Create the main window
root = tk.Tk()
app = EightPuzzleApp(root)
root.mainloop()
