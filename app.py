import tkinter
import tkinter.messagebox
import customtkinter
import os
import eightPuzzleSolver
import time
import psutil
import matrices


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")

# Create a font object with the desired size
custom_font = ("Helvetica", 12) # font used in the buttons of the puzzle
          
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("8 Puzzle Solver")
        self.geometry(f"{1480}x{720}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)

        
        # left side bar section

        # create and configure the sidebar frame
        self.left_sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.left_sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_sidebar_frame.grid_rowconfigure(5, weight=1)

        # create and configure the logo label
        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Match making system", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))   # set the logo at the top of the left column

        # create and configure the appearance option menu and label
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["Light", "Dark", "System"],
                                                                    command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(0, 10))  # Removed padding at the bottom
        self.appearance_mode_optionemenu.set("Dark")
        self.appearance_mode_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Appearance Mode: ", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(0, 10))

        # create and configure the scaling option menu and label
        self.scaling_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=3, column=0, padx=20, pady=(10, 5))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                            command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=4, column=0, padx=20, pady=(5, 10))  # Removed padding at the bottom
        self.scaling_optionemenu.set("100%")

        # created and configure the quit button
        self.quit_button = customtkinter.CTkButton(self.left_sidebar_frame, command=self.quit_simulation_event)
        self.quit_button.grid(row=6, column=0, padx=20, pady=(10, 40))
        self.quit_button.configure(state="enabled", text="Quit simulation")


        self.puzzle_frame = customtkinter.CTkFrame(self)
        self.puzzle_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Create the tiles as a matrix
        self.tiles = [[None, None, None], [None, None, None], [None, None, None]]
        
        # Create the puzzle grid
        self.tile_1 = customtkinter.CTkButton(self.puzzle_frame, text=" 1 ", width=5, height=2, command=self.clicked_tile_1_event)
        self.tile_1.grid(row=0, column=0, padx=10, pady=10)
        self.tile_1.configure(font = custom_font)       

        self.tile_2 = customtkinter.CTkButton(self.puzzle_frame, text=" 2 ", width=5, height=2, command=self.clicked_tile_2_event)
        self.tile_2.grid(row=0, column=1, padx=10, pady=10)
        self.tile_2.configure(font = custom_font)

        self.tile_3 = customtkinter.CTkButton(self.puzzle_frame, text=" 3 ", width=5, height=2, command=self.clicked_tile_3_event)
        self.tile_3.grid(row=0, column=2, padx=10, pady=10)
        self.tile_3.configure(font = custom_font)
        
        self.tile_4 = customtkinter.CTkButton(self.puzzle_frame, text=" 4 ", width=5, height=2, command=self.clicked_tile_4_event)
        self.tile_4.grid(row=1, column=0, padx=10, pady=10)
        self.tile_4.configure(font = custom_font)

        self.tile_5 = customtkinter.CTkButton(self.puzzle_frame, text=" 5 ", width=5, height=2, command=self.clicked_tile_5_event)
        self.tile_5.grid(row=1, column=1, padx=10, pady=10)
        self.tile_5.configure(font = custom_font)

        self.tile_6 = customtkinter.CTkButton(self.puzzle_frame, text=" 6 ", width=5, height=2, command=self.clicked_tile_6_event)
        self.tile_6.grid(row=1, column=2, padx=10, pady=10)
        self.tile_6.configure(font = custom_font)
        
        self.tile_7 = customtkinter.CTkButton(self.puzzle_frame, text=" 7 ", width=5, height=2, command=self.clicked_tile_7_event)
        self.tile_7.grid(row=2, column=0, padx=10, pady=10)
        self.tile_7.configure(font = custom_font)

        self.tile_8 = customtkinter.CTkButton(self.puzzle_frame, text=" 8 ", width=5, height=2, command=self.clicked_tile_8_event)
        self.tile_8.grid(row=2, column=1, padx=10, pady=10)
        self.tile_8.configure(font = custom_font)

        self.tile_9 = customtkinter.CTkButton(self.puzzle_frame, text="    ", width=5, height=2, command=self.clicked_tile_9_event)
        self.tile_9.grid(row=2, column=2, padx=10, pady=10)
        self.tile_9.configure(font = custom_font)
        
        self.tiles = [[self.tile_1, self.tile_2, self.tile_3], [self.tile_4, self.tile_5, self.tile_6], [self.tile_7, self.tile_8, self.tile_9]]

        self.tile_map= {1: self.tile_1, 
                        2: self.tile_2,
                        3: self.tile_3, 
                        4: self.tile_4, 
                        5: self.tile_5, 
                        6: self.tile_6, 
                        7: self.tile_7, 
                        8: self.tile_8, 
                        0: self.tile_9}

        # middle section containing the puzzle grid
        # self.right_sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        # self.right_sidebar_frame.grid_rowconfigure(5, weight=1)



    def clicked_tile_1_event(self):
        print("Tile 1 clicked")
        self.click_tile(1)

    def clicked_tile_2_event(self):
        print("Tile 2 clicked")
        self.click_tile(2)

    def clicked_tile_3_event(self):
        print("Tile 3 clicked")
        self.click_tile(3)

    def clicked_tile_4_event(self):
        print("Tile 4 clicked")
        self.click_tile(4)
    
    def clicked_tile_5_event(self):
        print("Tile 5 clicked")
        self.click_tile(5)

    def clicked_tile_6_event(self):
        print("Tile 6 clicked")
        self.click_tile(6)
    
    def clicked_tile_7_event(self):
        print("Tile 7 clicked")
        self.click_tile(7)
    
    def clicked_tile_8_event(self):
        print("Tile 8 clicked")
        self.click_tile(8)
    
    def clicked_tile_9_event(self):
        print("Tile 9 clicked")
        self.click_tile(0)

    def click_tile(self, button):
        print("Button clicked")
        if self.tile_map.get(button).cget("text") == "    ":  # check if the empty tile is clicked
            print("Empty tile clicked")
            return
        # print(button)

        # check if the button is next to the empty tile
        for i in range(3):
            for j in range(3):
                # check if the button number is the same as the tile using the tile_map
                if self.tile_map[button] == self.tiles[i][j]:
                    # print(self.tiles[i][j].cget("text"))
                    #if str(self.tiles[i][j].cget("text")) == str(button):
                    #if self.tiles[i][j] == button:
                    print("Button found")
                    print("Button found, number: ", str(self.tiles[i][j]))
                    self.move_tile(i, j)
                    return
         
    def move_tile(self, row, col):
        # Move the tile if possible
        can_go_up = row > 0
        can_go_down = row < 2
        can_go_left = col > 0
        can_go_right = col < 2

        if can_go_up and self.tiles[row - 1][col].cget("text") == "    ":
            label = self.tiles[row][col].cget("text")
            self.tiles[row][col].configure(text="    ")
            self.tiles[row - 1][col].configure(text=label)
            print("Moving tile up")
            return

        if can_go_down and self.tiles[row + 1][col].cget("text") == "    ":
            label = self.tiles[row][col].cget("text")
            self.tiles[row][col].configure(text="    ")
            self.tiles[row + 1][col].configure(text=label)
            print("Moving tile down")
            return

        if can_go_left and self.tiles[row][col - 1].cget("text") == "    ":
            label = self.tiles[row][col].cget("text")
            self.tiles[row][col].configure(text="    ")
            self.tiles[row][col - 1].configure(text=label)
            print("Moving tile left")
            return
        
        if can_go_right and self.tiles[row][col + 1].cget("text") == "    ":
            label = self.tiles[row][col].cget("text")
            self.tiles[row][col].configure(text="    ")
            self.tiles[row][col+1].configure(text=label)
            print("Moving tile right")
            return

        print("Invalid move")


    def run(self):
        print('App is running')

        # alternative implementation uses function from matrices.py to read matrices from matrices.txt

        # previous format was better because it shows the matrix in a more readable way
        # but it stops being viable when the user has to choose a matrix among 20
        matrixId = int(input("Choose matrix to solve from 0 to 39: "))
        selected_matrix = matrices.matricesMaping.get(matrixId)

        algorithmId = int(input("Choose algorithm to solve the puzzle: \n0. Breadth first\n1. Greedy\n2. IDS\n3. IDS star\n"))

        print("solving the puzzle: ")
        print(selected_matrix)
        
        if eightPuzzleSolver.isTableSolvable(selected_matrix) == False:
            print("The puzzle is not solvable")
        else:
            print("The puzzle is solvable")

            # Breadth First
            if algorithmId == 0:
                print("Executing breadthFirst")
                startTime = time.time()
                eightPuzzleSolver.breadthFirst(selected_matrix)
                endTime = time.time()
                print("Time elapsed in seconds: ", endTime - startTime)
            
            # Greedy
            elif algorithmId == 1:
                print("Executing greedy")
                startTime = time.time()
                eightPuzzleSolver.greedy(selected_matrix)
                endTime = time.time()
                print("Time elapsed in seconds: ", endTime - startTime)
            
            # IDS
            elif algorithmId == 2:
                print("Executing IDS")
                startTime = time.time()
                eightPuzzleSolver.IDS(selected_matrix)
                endTime = time.time()
                print("Time elapsed in seconds: ", endTime - startTime)
            
            # IDS star
            elif algorithmId == 3:
                print("Executing IDS star")
                startTime = time.time()
                eightPuzzleSolver.idsStar(selected_matrix)
                endTime = time.time()
                print("Time elapsed in seconds: ", endTime - startTime)
            
            # Invalid algorithm id
            else:
                print("Invalid algorithm id")
                return

            # Get memory usage
            process = psutil.Process()
            memoryUsage = process.memory_info().rss  # in bytes
            print("Memory Usage:", memoryUsage, "bytes")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def quit_simulation_event(self):
        self.destroy()
        exit()
