from typing import Tuple
import keyboard
# required for autocomplete module
from autocomplete import AutocompleteEntry
from autocomplete import NO_RESULTS_MESSAGE
import tkinter as tk
from tkinter import ttk

word_list = []

class Application(tk.Frame, tree, object):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        label = tk.Label(self, text="Start typing a word... ")
        label.pack()

        self.entry = AutocompleteEntry(self)
        self.build(case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
        self.entry.pack(after=label)

        self.nr = tk.StringVar()
        self.cs = tk.StringVar()

    def _update(self, *args):
        case_sensitive = False
        no_results_message = self.nr.get()
        self.build(
            case_sensitive=case_sensitive,
            no_results_message=no_results_message
        )
        self.entry.pack()

    def build(self, *args, **kwargs):
        find_prefix(root, self.entry.text.get())
        global word_list
        self.entry.build(
            word_list,
            kwargs["case_sensitive"],
            kwargs["no_results_message"]
        )

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

class Tr26(object):

    def __init__(self, root):
        self.word_list = []
        self.root = (root)

    def add(self, word: str):
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

    def print_words(self, root):
        """Print the next ten words alphabetically starting from the given root
        
        Arguments:
            root {TrieNode} -- This can be any node from the tree
        """
        if not root.children:
            return
        for child in root.children:
            if child.word_finished == True and len(self.word_list) < 11:
                self.word_list.append(child.word)
            self.print_words(child)

    def find_prefix(self, prefix: str):
        """Check if the prefix exsists in any of the words added so far calls print_words

        Arguments:
            root {TrieNode} -- this is the first node in the trie
            prefix {str} -- This is the prefix that tells us what node to search from
        
        Returns:
            boolean -- whether or not the prefix is possible in the tree
        """
        node = root
        self.word_list = []
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
        self.print_words(node)
        for word in self.word_list:
            print(word)
        return True

    def build_tree(self):
        """Reads a word from each line of input file and adds it to the tree
        
        Arguments:
            root {TrieNode} -- the root of the entire tree
        """
        words = open("./words.txt", "r").readlines()
        for word in words:
            self.add(word)

if __name__ == "__main__":
    root = TrieNode('*')
    word_tree = Tr26(root)
    word_tree.build_tree()

    while True:
        string = input("Input a string of letters (quit with 0 + Enter): ")
        word_tree.find_prefix(string.lower())
        if string == '0':
            break

    # window = tk.Tk()
    # window.title("DEMO")
    # window.resizable(False, False)
    # window.tk_setPalette("white")

    # application = Application(window)
    # application.pack()

    # window.mainloop()
