class Hamming:
    def distance(self, first, second):
        num_of_errors = 0
        if type(first) != str or type(second) != str:
            return "Wrong type of strands"
        if len(first) != len(second):
            return "Strands should be the same length"
        for i in range(len(first)):
            if first[i] != second[i]:
                num_of_errors += 1
        return num_of_errors
