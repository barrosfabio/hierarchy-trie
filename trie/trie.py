class Node():
    def __init__(self, class_name):
        self.children = {}
        self.end_of_word = False
        self.class_name = class_name

class Trie():
    def __init__(self):
        self.root = Node('R')

    def insert(self, data_class):
        current = self.root
        class_splitted = data_class.split('/')

        for sub_class in class_splitted:

            # If the class wasn't included, include it
            if sub_class not in current.children.keys():
                current.children[sub_class] = Node(sub_class)
            current = current.children[sub_class]

        current.end_of_word = True

    def search(self, data_class):
        current = self.root
        class_splitted = data_class.split('/')
        for sub_class in class_splitted:

            # If sub_class doesn't exist, return False
            if sub_class not in current.children.keys():
                return False
            current = current.children[sub_class]

        return current != None and current.end_of_word

    def traverse(self, root):
        current = root
        children = current.children
        print('Current node: {}'.format(current.class_name))

        if len(children) == 0:
            return
        else:
            for child in children:
                # Pass each child as a new root
                self.traverse(children[child])

    def lcpn_predict(self, root, path):
        current = root
        children = current.children
        path.append(current.class_name)
        print('Current node: {}'.format(current.class_name))

        if len(children) == 0:
            return path
        else:
            predicted = self.mock_predict(current.class_name)
            predicted_path = self.lcpn_predict(children[predicted])

        return predicted_path


    def mock_predict(self, class_name):
        return class_name


def main():

    classes = ['A/B/C','D/F/I', 'D/E/H', 'D/E/G']
    search_queries = ['A/B/C','R/D/F', 'D/E/H/J', 'D/E/G']

    trie = Trie()

    for key in classes:
        trie.insert(key)

    for query in search_queries:
        print('{} Present in trie? {}'.format(query,trie.search(query)))

    trie.traverse(trie.root)

if __name__ == '__main__':
    main()

