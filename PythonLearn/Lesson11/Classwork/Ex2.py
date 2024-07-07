import random


class Archive:
    deletedArchives = {}

    def __init__(self, number: int, text: str):
        self.digit = number
        self.string = text
        if self.digit in Archive.deletedArchives:
            Archive.deletedArchives[self.digit].append(self.string)
        else:
            Archive.deletedArchives[self.digit] = [self.string]


if __name__ == '__main__':
    for i in range(50):
        Archive(random.randint(1, 10), 'text' + str(i))

    print(Archive.deletedArchives)
