# Class Person - Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Tôi là {self.name}, {self.age} tuổi"


# Class Student - Inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        return f"{self.name} đang học bài"
    
    def get_info(self):
        return f"Sinh viên: {self.name}, Tuổi: {self.age}, ID: {self.student_id}"


# Create a student object and call methods
if __name__ == "__main__":
    student = Student("Nguyễn Văn A.", 20, "SV001")
    
    print(student.introduce())
    print(student.study())
    print(student.get_info())