
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age, tracks,score):
        self.name= str(name)
        self.age= int(age)
        self.tracks=str(tracks)
        self.score=float(score)
        print("Name:", name, ", Age:",age ,", Tracks:", tracks,", Score:",score)
   
    def change_name(self,newname):
            print("New Student details is as below:")
            print("Student Name: ",str(newname))
    def change_age(self,newage):
            print("Student Age: ",int(newage))
    def add_track(self,*args):
            print(f"Student Track {args}")
    def get_score(self,newscore):
            print("Student Score: ",newscore)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX","Backend")
Bob.get_score(33.8)
