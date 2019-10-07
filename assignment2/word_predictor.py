"""
Author[s]: John Shapiro
Course:    CS 4050, Algorithms and Algorithm Analysis
Term:      Fall 2019

Overview:
    This program builds a tree of TrieNodes (definde below). It then allows a user
    to search for the next ten possible words following a provided prefix.
    Much of this code has been adapted from:
        https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-lessthan-100-lines-of-code-a877ea23c1a1



Classes:
    TrieNode -- a node that knows what character led to it, if it is the end of a complete word,
        and if it is the end of a word it knows the word it is the end of.
"""

word_list = []

class TrieNode(object):
    """A trie type node tracking a char, a word boolean, and a word if the boolean is true
        Adapted from
        https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-lessthan-100-lines-of-code-a877ea23c1a1
    
    Arguments:
        object {char} -- the character is used to search for words
    """
    
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        self.word = None
        # How many times this character appeared in the addition process    

def add(root, word: str):
    """This adds a word to the tree by checking the character in existing nodes, and creating new nodes when
        when necessary. When the function reaches the end of the word, the node saves the word.
        Adapted from
        https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-lessthan-100-lines-of-code-a877ea23c1a1
    
    Arguments:
        root {TriedNode} -- the root of the entire tree
        word {str} -- adds this word to the tree
    """
    node_word = ''
    node = root
    for char in word:
        node_word += char
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # Point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word and add the word to the node
    node.word = node_word[:-1]
    node.word_finished = True

def print_words(root):
    """Print the next ten words alphabetically starting from the given root
    
    Arguments:
        root {TrieNode} -- This can be any node from the tree
    """
    global word_list
    if not root.children:
        return
    # Fill the word_list until it has ten words
    for child in root.children:
        if child.word_finished == True and len(word_list) < 11:
            word_list.append(child.word)
        print_words(child)

def find_prefix(root, prefix: str):
    """Check if the prefix exsists in any of the words in the tree and if so 
        call print_words with the node led to by the prefix as the root.

    Arguments:
        root {TrieNode} -- this is the first node in the trie
        prefix {str} -- This is the prefix that tells us what node to search from
    
    Returns:
        bool -- whether or not the prefix is the prefix of a word in the tree
    """
    global word_list
    word_list = []
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    print_words(node)
    for word in word_list:
        print(word)
    return True

def build_tree(root):
    """Reads a word from each line of input file and adds it to the tree.
        All words are converted to lowercase and duplicate words are removed.
    
    Arguments:
        root {TrieNode} -- the root of the entire tree
    """
    previous_word = ""
    words = open("./words.txt", "r").readlines()
    for word in words:
        if word.lower() != previous_word:
            add(root, word.lower())
        previous_word = word.lower()

if __name__ == "__main__":
    root = TrieNode('*')
    print("\ngrowing tree...\n")
    build_tree(root)

    print("************************************\n" + 
          "Enter the beginning of a word and\n" +
          "see ten words you might be typing\n" +
          "If you see less than ten words then\n" +
          "the prefix you entered does not come\n" +
          "before ten words.\n" + 
          "************************************\n")
    
    while True:
        string = input("Input a string of letters then press enter. (0 then enter to quit): ")
        if string.isalpha():
            find_prefix(root, string.lower())
        elif string == '0':
            print("\nchopping tree\n")
            break
        else:
            print("\nEnter letters only\n")

