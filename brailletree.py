class BrailleTree:
  # Constants tracking the representation of braille
  # In our tree, each interiror node represents a braille cell position
  # Braille characters stemming from that position being 0 are stored
  # in left subtrees.
  # Braille characters stemming from that position being 1 are stored in
  # right subtree
  POS_LOWERED_LEFT = '0'
  POS_RAISED_RIGHT = '1'

  '''
  Attributes:
    root; Node representing the first braille cell position.
  '''
  def __init__(self):
    self.root = Node(1)

  def print(self):
    '''
    Prints full tree to console
    Parameters: self
    Return: None
    ''' 
    self.root.print()

  def read_file(self, filename):
    '''
    Reads file of the format
    <braille character> <braille string of 6 0's and 1's>
    example: 
      m 101100
    Parameters:
      self
      filename; string; name of file to read from.
    Return
      none
    '''
    with open(filename) as file:
      lines = file.readlines()
      for line in lines:                            # "m 101100"
        line_vals = line.strip("\n").split(" ")
        self.add_value(line_vals[1], line_vals[0])


  def check_braille(self, braille_string):
    '''
    Checks entire tree for value of braille_string.
    Returns value if it exists, None otherwise.
    Parameters:
      self.
      braille_string: a string of 6 0's and 1's representing braille cell.
    Return:
      string of translated braille character, if one exists, None otherwise
  
    '''
    # use _check_braille to recursively check if path is in tree
    last_node, remaining_braille = self._check_braille(braille_string, self.root)
    if len(remaining_braille) > 0:
      return None
    else:
      return last_node.data

  def _check_braille(self, braille_string, node):
    '''
      Private recursive method for finding the node in the path defined by braille_string.
    
      Parameters:
        self, instance of BrailleTree Class.
        braille_string; a string of 0's and 1's representing braille cells.
        node; instance of Node class to begin our search.
      Return:
        tuple (node, remaining_braille) 
          node: instance of the last Node in partial path down braille_string
          remaining_braille: string; braille encodement not yet represented in the BrailleTree.

      For example, if we had the following partial tree
                                  + -- N8: Pos 6
                                  |           |
                                  |           |
                            + -- N7: Pos 5    + -- N9: q
                            |
                            |        
                      + -- N6: Pos 4
                      |
                      |
                + -- N5: Pos 3
                |
                |
          + -- N4: Pos 2  
          |
          |
      N1: Pos 1
          |
          |
          + -- N2: Pos 2
                |
                |
                + -- N3: Pos 3

	  For the above tree
      _check_braille("111110", self.root) returns (Node N9 with data=q, "")
      _check_braille("000111", self.root) returns (Node N3 with data="Pos 3", "0111")
      _check_braille("1100", Node N5 with data="Pos 3") returns (Node N7 with data="Pos 5", "00")
	  Think about what will _check_braille return if the tree was empty
    '''
    pass

  def add_value(self, braille_string, val):
    '''
    Public method to add value to tree.
    Parameters:
      braille_string; string of 6 0's and 1's representing state of cells in braille.
      val: string; value represented by braille_string.
    '''
    last_node, remaining_braille = self._check_braille(braille_string, self.root)
    if len(remaining_braille) == 0:
      print("Braille Exists in Tree:", braille_string, last_node.data)
    else:
      self._add_value(remaining_braille, last_node, val)

  def _add_value(self, braille_string, node, val):
    '''
    Private recursive method for adding a value to the tree. 
    Starting at node and following the path determined by braille (0 left, 1 right).
    Will add interal len(braille_string) new position nodes, starting at node.
    Will add value as a child node of a Position 6 node.

    Parameters:
      braille_string; string of 0's and 1's representing state of cells in braille.
      node; instance of Node class that is the next positional node to branch from.
      val: string; value represented by braille_string.
    
    '''
    pass

  def write_values(self, filepath):
    '''
    Writes all characters and their braille representation to file named filename.
    Parameters:
      self.
      filename; string; full path of file to write to.
    '''
    f = open(filepath, "w")
    # TODO
    f.close()

class Node:
  '''
   Class for storing data in our braille BinaryTree.
   Attributes:
    data; int or string; for interior position nodes, data will be cell position (1-6). 
         For leaf translation nodes, data will be character represented by path.
    left; Node or None. for position nodes, left children indicate this node's postion is lowered.
    right; Node or None. for position nodes, right children indicate a path where this node's cell postion is raised.
  '''
  def __init__(self, data):
    """ Initialize a binary tree node with given data. The left and right
        branches are set to None (null). 
    Parameters:
      data; for interior position nodes, data will be cell position (1-6). 
         For leaf translation nodes, data will be character represented by path.
    Return:
      None
    """
    # data is either cell # (1-6) or value
    self.data = data
    self.left = None
    self.right = None

  def is_leaf(self):
    '''
    Checks if node is leaf by checking if it has neither a left nor right child.
    Parameters: 
      self.
    Return:
      Boolean, True if leaf, false otherwise.
    '''
    return self.left == None and self.right == None

  def is_position_node(self):
    '''
    Checks if node represents a braille cell postion (as opposed to translated character).
    Parameters: self.
    Return:
      Boolean, True if position node, False if translated character node.
    '''
    return self.data in range(1,7)
    
  def print(self):
    """ Print out the tree rooted at this node. 
    Parameters: self.
    Return: None.
    """
    lines = []
    strings = []
    self.print_nodes(lines, strings)
    st = ""
    for string in strings:
      st = st + string
    print(st)

  def print_nodes(self, lines, strings):
    """ Helper function for print(). """
    level = len(lines)
    if self.right != None:
      lines.append(False)
      self.print_lines(lines, strings, "\n")
      self.right.print_nodes(lines, strings)
      lines.pop(level)
    else:
      self.print_lines(lines, strings, "\n")

    if level>0:
      old = lines.pop(level-1)
      self.print_lines(lines, strings, "  +--")
      lines.append(not old)
    # if a position, add "Pos "
    if self.is_position_node():
      strings.append("Pos ")
    strings.append(str(self.data) + "\n")

    if self.left != None:
      lines.append(True)
      self.left.print_nodes(lines, strings)
      self.print_lines(lines, strings, "\n")
      lines.pop(level)
    else:
      self.print_lines(lines, strings, "\n")

  def print_lines(self, lines, strings, suffix):
    """ Helper function for print(). """
    for line in lines:
      if line: 
        strings.append("  |  ")
      else:    
        strings.append("     ")
    strings.append(suffix)
    
