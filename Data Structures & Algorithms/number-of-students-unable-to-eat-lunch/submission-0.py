class Solution:
    
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rotations = 0
        while students and sandwiches and rotations < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rotations = 0
            else:
                students.append(students.pop(0))
                rotations += 1
                
        return len(students)