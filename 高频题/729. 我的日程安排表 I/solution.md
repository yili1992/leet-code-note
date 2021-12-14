方法一：
暴力破解。
遍历当前所有已添加的日程，判断要插入的起止时间区间是否跟它有交集，有交集则返回False，否则在尾端插入。
该方法运行时间：920ms（23%），内存消耗14MB（100%）

```
class MyCalendar:
    def __init__(self):
        self.booked=[]

    def book(self, start: int, end: int) -> bool:
        def intersect(calender,calenders):
            for start ,end in calenders:
                if calender[0]>=end or calender[1]<=start:
                    continue
                else:
                    return True
            return False
        
        if intersect((start,end),self.booked):
            return False
        else:
            self.booked.append((start,end))
            return True
```
方法二：
还是暴力破解，优化交集判断区间，代码也更简洁。
该方法运行时间：684ms（36.8%），内存消耗14.2MB（100%）

```
class MyCalendar:
    def __init__(self):
        self.booked=[]

    def book(self, start: int, end: int) -> bool:
        for date in self.booked:
            if start<date[1] and end>date[0]:
                return False
        self.booked.append((start,end))
        return True
```
方法三：
对每一个预定时间按照起始时间由早到晚排序，使得booked为有序的序列。
对于booked中的某一个元素date,当date[0]大于待插入时间的尾部时，可以提前完成判断，并把它插入到date原本的位置，date及其以后的元素后移一位。
这种操作使得遍历时可以提前中止，减少无用判断。
该方法运行时间：672ms（38.3%），内存消耗14.2MB（100%）

```
class MyCalendar:

    def __init__(self):
        self.booked=[]

    def book(self, start: int, end: int) -> bool:
        count=-1
        for idx,date in enumerate(self.booked):
            if start<date[1] and end>date[0]:
                return False
            if date[0]>=end:
                count=idx
                break
        if count==-1:
            self.booked.append((start,end))
        else:
            self.booked.insert(idx,(start,end))
        return True
```
方法四：
基于方法三，结合二分法提高查找速度。
当while循环完整执行完毕，没有中途return时，表示booked中的任何元素都没有和待插入时间段有交集。此时low指针即是插入的位置
该方法运行时间：292ms（87.23%），内存消耗14.2MB（100%）

```
class MyCalendar:
    def __init__(self):
        self.booked=[]

    def book(self, start: int, end: int) -> bool:
        length=len(self.booked)
        
        low=0
        high=length-1

        while low<=high:
            mid=(low+high)//2
            date_mid=self.booked[mid]

            if end<=date_mid[0]:
                high=mid-1
            elif start>=date_mid[1]:
                low=mid+1
            elif start<=date_mid[1] and end >=date_mid[0] :
                return False
        self.booked.insert(low,(start,end))
        return True    
```