import unittest
from SemanticNetsAgent import SemanticNetsAgent

class TestSemanticNetsAgent(unittest.TestCase):
  def test_solve_simple(self):
    """Tests solving the Sheep and Wolves problem with a simple case."""
    agent = SemanticNetsAgent()
    solution = agent.solve(1, 0)
    self.assertEqual(solution, [(1, 0)])  # Move one sheep

  def test_solve_complex(self):
    """Tests solving the Sheep and Wolves problem with a more complex case."""
    agent = SemanticNetsAgent()
    solution = agent.solve(2, 2)
    self.assertEqual(solution, [(1, 0), (2, 0)])  # Move one sheep, then two sheep

  def test_no_solution(self):
    """Tests the case where there is no solution for the Sheep and Wolves problem."""
    agent = SemanticNetsAgent()
    solution = agent.solve(3, 1)
    self.assertEqual(solution, [])  # Empty list indicates no solution

if __name__ == '__main__':
  unittest.main()