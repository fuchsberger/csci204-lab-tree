# Here are the lab instructions
# https://docs.google.com/document/d/1PhC90CbdukN7ac8yP30Mme16f_sLyarHyQSdCRNO5uI

# Your name:
# Your partner's name (if applicable):

from brailletree import BrailleTree

def is_yes(response):
  '''Was it a yes response?'''
  return response in ["y", "yes", "Yes", "Y"]

def main():
  ''' Run Braille Translator
  '''
  # see if printing tree as we go
  debug_mode = input("Print tree as you go?")
  debug = is_yes(debug_mode)

  # Assemble initial tree
  braille_tree = BrailleTree()

  # read values from file
  braille_tree.read_file("alphabet.txt")

  if debug:
    braille_tree.print()

  # UNCOMMENT THE FOLLOWING TO RUN YOUR WRITE_VALUES FUNCTION.

  # # write traversal of tree
  # braille_tree.write_values("traversal.txt")

  # while True:
  #   braille = input("Give a braille sequence of 0's and 1's to translate.\n")

  #   translation = interactive_translator(braille_tree, braille)

  #   print("Braille Translation: ", translation)

  #   if debug:
  #     braille_tree.print()
  #     print()

  #   response = input("Enter another sequence? ")
  #   if not is_yes(response):
  #     break


def interactive_translator(braille_tree, braille):
  """Currently returns the character or alternatively _ if the character is not in the tree. You will need to reject invalid braille strings and extend the translator to process whole words."""
  # TODO Task 4 and 5
  translation = braille_tree.check_braille(braille)

  if translation != None:
    return translation
  else:
    return "_"


if __name__=="__main__":
  main()
