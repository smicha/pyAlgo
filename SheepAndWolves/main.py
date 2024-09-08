from SemanticNetsAgent import SemanticNetsAgent

def main():
  """
  This function demonstrates how to use the SemanticNetsAgent class.

  It prompts the user for the initial number of sheep and wolves on the left side,
  and then uses the SemanticNetsAgent to find the solution for moving them all
  to the right side.
  """

  # Get user input for initial state
  while True:
    try:
      initial_sheep = int(input("Enter the initial number of sheep: "))
      initial_wolves = int(input("Enter the initial number of wolves: "))
      if initial_sheep < 0 or initial_wolves < 0:
        print("Error: Initial sheep and wolves cannot be negative.")
      else:
        break
    except ValueError:
      print("Error: Please enter valid integers for sheep and wolves.")

  # Create an agent and solve the problem
  agent = SemanticNetsAgent()
  solution = agent.solve(initial_sheep, initial_wolves)

  # Print the solution
  if solution:
    print("Solution found:")
    for move in solution:
      sheep, wolves = move
      print(f"- Move {sheep} sheep and {wolves} wolves together")
  else:
    print("No solution exists.")

if __name__ == "__main__":
  main()