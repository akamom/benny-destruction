class Differencer:

    def __init__(self, old, new):
        self.old = old
        self.new = new
        
    def execute(self):
        len_old = len(self.old)
        len_new = len(self.new)
        
        diff_array = []
        if(len_old == len_new):
            for i in range(len(self.old)):
                if (self.old[i] != self.new[i]):
                    diff_array.append([self.new[i][j] - self.old[i][j] for j in range(len(self.old[i]))])
        else:
            return
        
        sum_array = []
        for diff in diff_array:
            round_diff = round(sum(diff))
            if round_diff != 0:
                sum_array.append(hex(round_diff))
                
        return sum_array