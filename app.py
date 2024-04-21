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
          
class App(customtkinter.CTk):
    def __init__(self):
        # print('App is initialized')
        super().__init__()

        # configure window
        self.title("8 Puzzle Solver")
        self.geometry(f"{1480}x{720}")


        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        # self.grid_rowconfigure((0, 1, 2), weight=1)
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

        # middle section containing the puzzle grid
        self.right_sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.puzzle_frame = customtkinter.CTkFrame(self, corner_radius=0)

        # self.tiles = []
        row = []
        tile = customtkinter.CTkButton(master=self.right_sidebar_frame, text=" ", width=5, height=2, command=self.click_tile(tile))
        tile.grid(row=0, column=0, padx=5, pady=5)
        row.append(tile)

        tile = customtkinter.CTkButton(master=self.right_sidebar_frame, text=" ", width=5, height=2, command=self.click_tile(tile))
        tile.grid(row=1, column=0, padx=5, pady=5)
        row.append(tile)

        tile = customtkinter.CTkButton(master=self.right_sidebar_frame, text=" ", width=5, height=2, command=self.click_tile(tile))
        tile.grid(row=2, column=0, padx=5, pady=5)
        row.append(tile)

        self.puzzle_frame.append(row)
         


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

    def click_tile(self, button):
        # Handle clicks on tiles
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == button:
                    self.move_tile(i, j)
                    return