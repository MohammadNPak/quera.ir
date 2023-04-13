# [فاکتوریسم](https://quera.org/problemset/76277/)
from datetime import datetime

class FactorHandler:
    
    def __init__(self):
        self.format_dict={"dd/mm/yyyy":r"%d/%m/%Y","dd/yyyy/mm":r"%d/%Y/%m","yyyy/mm/dd":r"%Y/%m/%d","yyyy/dd/mm":r"%Y/%d/%m","mm/yyyy/dd":r"%m/%Y/%d","mm/dd/yyyy":r"%m/%d/%Y"}
        self.factors=[]

    def add_factor(self, time_format, time, value):
        d = datetime.strptime(time, self.format_dict[time_format])
        factor=(d, value)
        self.factors.append(factor)

    def remove_all_factors(self, time_format, time):
        d = datetime.strptime(time, self.format_dict[time_format])
        self.factors = [factor for factor in self.factors if factor[0] != d]

    def get_sum(self, time_format, start_time, finish_time):
        start_d = datetime.strptime(start_time, self.format_dict[time_format])
        finish_d = datetime.strptime(finish_time, self.format_dict[time_format])
        return sum([factor[1] for factor in self.factors if start_d <= factor[0] <= finish_d])
        
        
        
# fh = FactorHandler()
# fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)
# fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)
# print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/03/10"))
# fh.remove_all_factors("mm/dd/yyyy", "10/03/2019")
# print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/05/10"))