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
  # write traversal of tree
    '''Uncomment to run your write_values function'''
  # braille_tree.write_values("traversal.txt")
  # interactive_translator(braille_tree, debug)


def interactive_translator(braille_tree, debug):
  # interactive translator
  while True:
    braille = input("Give a braille sequence of 0's and 1's to translate.\n")

    # TODO: Check for invalid input braille sequence here

    # TODO: Edit code here to translate whole braille words

    translation = braille_tree.check_braille(braille)
    if translation != None:
      print("Braille Translation: ", translation)
    else:
      print("Braille sequence", braille, "not in tree.")

    if debug:
      braille_tree.print()
      print()

    response = input("Enter another sequence? ")
    if not is_yes(response):
      break

if __name__=="__main__":
  main()
