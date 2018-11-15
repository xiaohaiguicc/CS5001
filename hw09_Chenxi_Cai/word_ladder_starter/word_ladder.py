from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, wordlist):
        """Constructor.
        w1 and w2 are begining and end of word ladder.
        Wordlist is a dictionary containing set of words
        with lengths between [len(w1), len(w2)].
        String, String, Dictionary -> None"""
        self.w1 = w1
        self.w2 = w2
        self.worddic = wordlist  # worddic is a dictionary
        self.queue = Queue()
        self.wordset = set()

    def initialize(self):
        """Initialize a queue containing a single stack
        None -> None"""
        stack = Stack()
        stack.push(self.w1)
        self.queue.enqueue(stack)

    def make_ladder(self):
        """1. First generate all possible words with the same length as w1.
        (This part of word is the Algorithm of hw9).
        2. Then enqueue each stack and get top word.
        (i)If top word is shorter than w2,
        for each position of the word, (->word<-, from 0 to len(word)).
        For each letter in the alpahbet,
        add letter to the position. The len(word) increase by 1.
        (ii)If top word is longer than w2,
        for each position of the word, (->word<-, from 0 to len(word)).
        delete character in this position from it. The len(word) decrease by 1.
        Add new word to stack and enqueue stack to queue.
        Continue step 2 until we get the final w2.
        If word ladder exist, return the word ladder stack
        Else, return None
        None -> Stack/None"""
        self.initialize()
        alph = "abcdefghijklmnopqrstuvwxyz"
        while not self.queue.isEmpty():
            stack = self.queue.dequeue()
            word = stack.peek()
            for i in range(len(word)):
                for letter in alph:
                    new_word = word[:i]
                    new_word += letter
                    new_word += word[i + 1:]
                    new_stack = self.word_in_wordlist(new_word, stack)
                    if new_stack is not None:
                        return new_stack
            if len(word) < len(self.w2):
                for i in range(len(word) + 1):
                    for letter in alph:
                        new_word = word[:i]
                        new_word += letter
                        new_word += word[i:]
                        new_stack = self.word_in_wordlist(new_word, stack)
                        if new_stack is not None:
                            return new_stack
            elif len(word) > len(self.w2):
                for i in range(len(word)):
                    new_word = word[:i]
                    new_word += word[i + 1:]
                    new_stack = self.word_in_wordlist(new_word, stack)
                    if new_stack is not None:
                        return new_stack
        return None

    def word_in_wordlist(self, new_word, stack):
        """1.First check if the new word in the wordset.
        2.Then check if the new word is in wordlist.
        If it is in wordlist, copy stack and put it into new stack.
        3.(i)If the word is the last word of the word ladder,
        return the new stack.
        (ii)If the word is not the last word of the ladder,
        enqueue the new stack onto the end of the queue and return None.
        String, Stack -> Stack/None"""
        if new_word not in self.wordset:
            self.wordset.add(new_word)
            wordlist = self.worddic[len(new_word)]
            if new_word in wordlist:
                new_stack = stack.copy()
                new_stack.push(new_word)
                if new_word == self.w2:
                    return new_stack
                self.queue.enqueue(new_stack)
