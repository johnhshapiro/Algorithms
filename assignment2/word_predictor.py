class Node:
    is_word = False
    lookup = []

class WordPredictor:
    root = Node()

    def build_word_tree(self, root):
        current = root

        read_lines = open("./better_words.txt", "r").readlines()
        for i in read_lines:
            for j in i:
                if j == '\n':
                    break
                print(j)
                if j not in current.lookup:
                    current.lookup.extend([j, Node()])
                print(current)
                print(current.lookup)
                current = current.lookup[current.lookup.index(j) + 1]
                print(current.lookup[current.lookup.index(j) + 1])
                print(current)
                print(current.lookup)
            current.is_word = True
            current = root
        return root
    
    def find_word(self, root, input):
        current = root
        output = ''
        print("Search started")
        for i in input:
            print(i)
            if i in current.lookup:
                output += i
                print("next node")
                current = current.lookup[current.lookup.index(i) + 1]
                print(output)
                print(current.is_word)
            else:
                print("Word not found")
                return False

if __name__ == '__main__':
    tree = WordPredictor()
    tree.root = tree.build_word_tree(tree.root)
    # tree.find_word(tree.root, 'aback')
    # tree.find_word(tree.root, 'aaa')