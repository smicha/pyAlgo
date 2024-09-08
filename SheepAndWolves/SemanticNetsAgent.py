class SemanticNetsAgent:
    """
    This class implements an agent using Breadth-First Search (BFS) to solve the Sheep and Wolves problem.
    """

    def __init__(self):
        """
        Initializes the agent.
        """
        # Valid moves: (sheep_to_move, wolves_to_move)
        self.valid_moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

    def solve(self, initial_sheep, initial_wolves):
        """
        Solves the Sheep and Wolves problem using BFS.

        Args:
            initial_sheep (int): The initial number of sheep on the left side.
            initial_wolves (int): The initial number of wolves on the left side.

        Returns:
            list: A list of moves representing the solution path, or an empty list if no solution exists.
        """

        # Initialize variables
        left_sheep = initial_sheep
        left_wolves = initial_wolves
        right_sheep = 0
        right_wolves = 0

        # Use a queue to explore states
        state_queue = [(left_sheep, left_wolves, right_sheep, right_wolves)]
        visited_states = set()

        solution = []

        while state_queue:
            current_state = state_queue.pop(0)  # Get the next state to explore from the queue
            visited_states.add(current_state)  # Mark the current state as visited to avoid exploring it again


            # Check if the goal state is reached (all sheep and wolves on the right side)
            if current_state[0] == 0 and current_state[1] == 0:
                return solution

            for move in self.valid_moves:
                # Calculate the next state by applying the move to the current state
                new_state = self._get_next_state(current_state, move)

                # Check if the new state is valid and hasn't been visited
                if self._is_valid_state(new_state) and new_state not in visited_states:
                    state_queue.append(new_state)
                    solution.append(move)

        # No solution found
        return []

    def _get_next_state(self, current_state, move):
        """
        Calculates the next state after applying a move.

        Args:
            current_state (tuple): The current state (left_sheep, left_wolves, right_sheep, right_wolves).
            move (tuple): The move to be applied (sheep_to_move, wolves_to_move).

        Returns:
            tuple: The new state after applying the move.
        """

        left_sheep, left_wolves, right_sheep, right_wolves = current_state
        sheep_to_move, wolves_to_move = move

        # Ensure the move is valid within the boat's capacity
        if sheep_to_move > left_sheep or wolves_to_move > left_wolves:
            return current_state

        # Update state based on the move direction (left to right or right to left)
        if left_sheep > 0 or left_wolves > 0:  # Moving from left to right
            new_left_sheep = left_sheep - sheep_to_move
            new_left_wolves = left_wolves - wolves_to_move
            new_right_sheep = right_sheep + sheep_to_move
            new_right_wolves = right_wolves + wolves_to_move
        else:  # Moving from right to left (boat returning empty)
            new_left_sheep = left_sheep + right_sheep
            new_left_wolves = left_wolves + right_wolves
            new_right_sheep = 0
            new_right_wolves = 0

        return new_left_sheep, new_left_wolves, new_right_sheep, new_right_wolves

    def _is_valid_state(self, state):
        """
        Checks if a state is valid (wolves don't outnumber sheep on either side).

        Args:
            state (tuple): The state (left_sheep, left_wolves, right_sheep, right_wolves).

        Returns:
            bool: True if the state is valid, False otherwise.
        """

        left_sheep, left_wolves, right_sheep, right_wolves = state
        return (left_sheep >= left_wolves or left_sheep == 0) and (right_sheep >= right_wolves or right_sheep == 0)