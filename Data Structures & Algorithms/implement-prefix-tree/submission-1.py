class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # Initialize the curr pointer with the root node
        curr = self.root

        # Iterate across the length of the string
        for c in word:

            # Check if the node exists for the
            # current character in the Trie
            index = ord(c) - ord('a')
            if curr.children[index] is None:

                # If node for current character does
                # not exist then make a new node
                new_node = TrieNode()

                # Keep the reference for the newly
                # created node
                curr.children[index] = new_node

            # Move the curr pointer to the
            # newly created node
            curr = curr.children[index]

        # Mark the end of the word
        curr.isEndOfWord = True


    def search(self, word: str) -> bool:
        # Initialize the curr pointer with the root node
        curr = self.root

        # Iterate across the length of the string
        for c in word:

            # Check if the node exists for the 
            # current character in the Trie
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False

            # Move the curr pointer to the 
            # already existing node for the 
            # current character
            curr = curr.children[index]

        # Return true if the word exists 
        # and is marked as ending
        return curr.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')

            # If character doesn't exist, return false
            if curr.children[index] is None:
                return False
            curr = curr.children[index]

        return True
        
        