class OrderedStream:

    def __init__(self, n: int):
        self.messagesMap = [None] * (n + 1)  # Initialize a list to store messages
        self.ptr = 1  # Initialize the pointer to 1

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []

        # Store the message at the given idKey
        self.messagesMap[idKey] = value

        # Check if the message at the current pointer is not None
        while self.ptr < len(self.messagesMap) and self.messagesMap[self.ptr]:
            # Append the message to the result and increment the pointer
            res.append(self.messagesMap[self.ptr])
            self.ptr += 1

        return res
