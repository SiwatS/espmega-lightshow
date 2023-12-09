import random
class CustomUserScript:
    def __init__(self, rows: int, columns: int, set_tile_state, get_tile_state):
        self.rows = rows
        self.columns = columns
        # set_element_state(row, column, state) is a function that sets the state of a light at row, column to state
        self.set_tile_state = set_tile_state
        # get_element_state(row, column) is a function that gets the state of a light at row, column
        self.get_tile_state = get_tile_state
        self.active = True
        self.executing = False
        self.frame_count = 0

    def __draw_frame__(self, current_time: float):
        self.executing = True
        self.frame_count += 1
        self.draw_frame(current_time)
        self.executing = False

    def draw_frame(self, current_time: float):
        # This function is called every frame
        for row in range(self.rows):
            for column in range(self.columns):
                # Generate a random state for the light
                state = random.choice([True, False])
                # Set the state of the light at row, column
                self.set_tile_state(row, column, state)
