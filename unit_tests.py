import unittest
from io import StringIO
import sys
from brailletree import *

"""
Name each method beginning with test_

Here are examples of the tests you can run:
self.assertIsInstance(x, str) # variable, name of type
self.assertEqual(x, y) # tests if x == y
self.assertTrue(x) # tests if x is True
self.assertFalse(x) # tests if x is False
self.assertIn(stringToLookFor, largeString, "errorMessage if not found")

capturedOutput = StringIO()  # Create StringIO object
sys.stdout = capturedOutput  # redirect the console output to stringIO
# line(s) of code that print go here
sys.stdout = sys.__stdout__  # reset to stdout
output = capturedOutput.getvalue().strip(
)  # convert the output to a string
# Then you can do tests on the string named output

with self.assertRaises(ExceptionClass):
  code to run
"""
class Testing(unittest.TestCase):

  # You should always pass this first test."""
  def test_empty_tree(self):
    """Test 1: Empty Tree"""
    tree = BrailleTree()
    # tree field is named root and is a Node (not None)
    self.assertEqual(type(tree.root), Node)
    # the root is a position Node
    self.assertTrue(tree.root.is_position_node())
    # the root is technically a leaf for the moment
    self.assertTrue(tree.root.is_leaf())

  # You should pass these next tests after you complete check_braille()
  def test_check_braille_empty(self):
    """Test 2: check_braille (empty)"""
    tree = BrailleTree()
    # The braille for m is not currently in the tree since its empty
    node,string = tree._check_braille("101100", tree.root)
    self.assertEqual(node.data, 1)
    self.assertEqual(string, "101100")


  def test_check_braille_m(self):
    """Test 3: check_braille (m)"""
    tree = BrailleTree()
    # Stuffing the letter m 101100 into the tree by hand!
    tree.root.right=Node(2)
    tree.root.right.left = Node(3)
    tree.root.right.left.right = Node(4)
    tree.root.right.left.right.right = Node(5)
    tree.root.right.left.right.right.left = Node(6)
    tree.root.right.left.right.right.left.left = Node("m")
    node, string = tree._check_braille("101100", tree.root)
    self.assertEqual(node.data, "m")
    self.assertEqual(string, "")

  def test_check_braille_a(self):
    """Test 4: check_braille (m NOT a)"""
    tree = BrailleTree()
    # Stuffing the letter m 101100 (NOT a) into the tree by hand!
    tree.root.right=Node(2)
    tree.root.right.left = Node(3)
    tree.root.right.left.right = Node(4)
    tree.root.right.left.right.right = Node(5)
    tree.root.right.left.right.right.left = Node(6)
    tree.root.right.left.right.right.left.left = Node("m")
    node, string = tree._check_braille("100000", tree.root)
    self.assertEqual(node.data, 3) # didnt match digit 3
    self.assertEqual(string, "0000")

  # You should pass these next tests after you complete add_value()
  def test_add_value_m(self):
    """Test 5: add_value (m)"""
    tree = BrailleTree()
    tree.add_value("101100", "m")
    m_test = tree.check_braille("101100")
    self.assertEqual(m_test, "m")

  def test_add_value_max_m(self):
    """Test 6: add_value (max m)"""
    tree = BrailleTree()
    tree.add_value("101100", "m")
    tree.add_value("100000", "a")
    tree.add_value("101101", "x")
    m_test = tree.check_braille("101100")
    self.assertEqual(m_test, "m")

  def test_add_value_max_a(self):
    """Test 7: add_value (max a)"""
    tree = BrailleTree()
    tree.add_value("101100", "m")
    tree.add_value("100000", "a")
    tree.add_value("101101", "x")
    a_test = tree.check_braille("100000")
    self.assertEqual(a_test, "a")

  def test_add_value_max_x(self):
    """Test 8: add_value (max x)"""
    tree = BrailleTree()
    tree.add_value("101100", "m")
    tree.add_value("100000", "a")
    tree.add_value("101101", "x")
    x_test = tree.check_braille("101101")
    self.assertEqual(x_test, "x")

  def test_add_value_max_b(self):
    """Test 9: add_value (max b)"""
    tree = BrailleTree()
    tree.add_value("101100", "m")
    tree.add_value("100000", "a")
    tree.add_value("101101", "x")
    b_test = tree.check_braille("110000")
    self.assertEqual(b_test, None)

unittest.main()
