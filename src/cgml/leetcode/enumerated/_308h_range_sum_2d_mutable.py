class BinaryIndexTree:
    def __init__(self, numCols):
        self.BIT = [0] * (numCols + 1)
        self.n = numCols

    def update(self, value, pos):
        pos += 1
        # update all the children of the node
        while (pos < self.n + 1):
            self.BIT[pos] += value
            pos += pos & (-pos)

    """
    returns sum of elements for li[0...pos-1]
    """

    def _getSum(self, pos):
        pos += 1
        sum = 0
        while (pos > 0):
            sum += self.BIT[pos]
            pos -= pos & (-pos)
        return sum

    """
    return sum of elements for li[begin..end]
    """

    def getSum(self, begin, end):
        begin -= 1

        sum2 = self._getSum(end)
        if (begin >= 0):
            sum1 = self._getSum(begin)
            return sum2 - sum1

        return sum2


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        numRow = len(matrix)
        self.binaryIndexTree = []
        self.matrix = matrix

        for row in range(numRow):
            BIT = BinaryIndexTree(len(matrix[row]))

            for col in range(len(matrix[row])):
                BIT.update(matrix[row][col], col)

            self.binaryIndexTree.append(BIT)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        oldValue = self.matrix[row][col]
        diff = val - oldValue
        BIT = self.binaryIndexTree[row]
        BIT.update(diff, col)

        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for row in range(row1, row2 + 1):
            BIT = self.binaryIndexTree[row]
            sum += BIT.getSum(col1, col2)
        return sum


class NumMatrix2(object):

    def __init__(self, matrix):
        for row in matrix:
            for col in range(1, len(row)): row[col] += row[col - 1]
        self.matrix = matrix

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0: original -= self.matrix[row][col - 1]

        diff = original - val

        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for x in range(row1, row2 + 1):
            sum += self.matrix[x][col2]
            if col1 != 0: sum -= self.matrix[x][col1 - 1]
        return sum

