from datetime import datetime

class FactorHandler:
    
    def __init__(self):
        self.format_dict={"dd/mm/yyyy":"%d/%m/%Y","dd/yyyy/mm":"%d//%Y%m","yyyy/mm/dd":"%Y/%m/%d","yyyy/dd/mm":"%Y/%d/%m","mm/yyyy/dd":"%m/%Y/%d","mm/dd/yyyy":"%m/%d/%Y"}
        self.factors=[]

    def add_factor(self, time_format, time, value):
        for key in self.format_dict.keys():
            if time_format==key :
                d = datetime.strptime(time, self.format_dict[key])
                day = d.strftime('%d')
                month = d.strftime('%m')
                year = d.strftime("%Y")
                date=(f'{year}/{month}/{day}')
                break
        factor={"date":date , "value":value}
        self.factors.append(factor)
        # print(FactorHandler.factors)

    def remove_all_factors(self, time_format, time):
        for key in self.format_dict.keys():
            if time_format==key :
                d = datetime.strptime(time, self.format_dict[key])
                day = d.strftime('%d')
                month = d.strftime('%m')
                year = d.strftime("%Y")
                date=(f'{year}/{month}/{day}')
                i=0
                while i<len(self.factors):
                    if self.factors[i]["date"]==date :
                        self.factors.pop(i)
                    else:
                        i+=1

    def get_sum(self, time_format, start_time, finish_time):
        for key in self.format_dict.keys():
            if time_format==key :
                d1 = datetime.strptime(start_time, self.format_dict[key])
                start_day = d1.strftime('%d')
                start_month = d1.strftime('%m')
                start_year = d1.strftime("%Y")
                # start_date=(f'{start_year}/{start_month}/{start_day}')
                # print(start_date)
                d2 = datetime.strptime(finish_time, self.format_dict[key])
                finish_day = d2.strftime('%d')
                finish_month = d2.strftime('%m')
                finish_year = d2.strftime("%Y")
                # finish_date=(f'{finish_year}/{finish_month}/{finish_day}')
                # print(finish_date)
                break
        total_value=0
        for factor in self.factors:
            y=int(factor["date"][0:4])
            m=int(factor["date"][5:7])
            d=int(factor["date"][8:10])
            if int(start_year)<=y<=int(finish_year) and int(start_month)<=m<=int(finish_month) and int(start_day)<=d<=int(finish_day):
                total_value += factor["value"]
        return total_value
        
        
        
fh = FactorHandler()
# fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)
# fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)

# fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/03/10")

# fh.remove_all_factors("mm/dd/yyyy", "10/03/2019")
# fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/05/10")