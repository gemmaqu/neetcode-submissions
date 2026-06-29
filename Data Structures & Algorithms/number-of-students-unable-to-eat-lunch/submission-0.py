class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_zeros = students.count(0)  # how many want circular
        count_ones = students.count(1)   # how many want square 
        while students: #or we can write while len(students) != 0
            if sandwiches[0]==0 and count_zeros == 0:
                return count_ones
            if sandwiches[0]==1 and count_ones == 0:
                return count_zeros
            if students[0] == sandwiches[0]:
                if students[0]== 0:
                    count_zeros -= 1
                else:
                    count_ones -= 1
                students.pop(0)
                sandwiches.pop(0)
                
            else:
                student = students.pop(0)
                students.append(student)
        return 0
            
            