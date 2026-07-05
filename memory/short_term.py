# memory/short_term.py

class ShortTermMemory:
    """
    Stores information during the current session.
    """

    def __init__(self):

        self.memory = {}

    def store(self, key, value):

        self.memory[key] = value

    def retrieve(self, key):

        return self.memory.get(key)

    def retrieve_all(self):

        return self.memory

    def clear(self):

        self.memory.clear()