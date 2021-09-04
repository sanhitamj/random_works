import pandas as pd


class CollatzNumbers:
    def __init__(self, num=30):
        self.num = num

    def collatz_function(self, num):
        orig_num = num
        num_iter = 0
        max_num = num
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (3 * num + 1) / 2
            if num > max_num:
                max_num = num
            num_iter += 1
        return (orig_num, int(num), num_iter, int(max_num))

    def get_collatz_dataframe(self):
        data = [self.collatz_function(n) for n in range(1, self.num)]
        return pd.DataFrame(data,
                            columns=['orig_num',
                                     'reduced_to',
                                     'num_iterations',
                                     'max_num_found'])


if __name__ == '__main__':
    cn = CollatzNumbers(30)
    df = cn.get_collatz_dataframe()
