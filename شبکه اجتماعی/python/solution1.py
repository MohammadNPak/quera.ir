# https://quera.ir/problemset/9742/



class Person:
    def __init__(self,username, gender, age, id) -> None:
        self.username= username
        self.gender= gender
        self.age= age
        self.id = id
    
    def __str__(self) -> str:
        return f"{self.username} {self.gender} {self.age} {self.id}"

persons = dict()

def add(username, gender, age, id):
    p = Person(username, gender, age, id)
    persons.update({id:p})
    print(f"User {p.id} added successfully")


def find(id):
    found_user = persons.get(id)
    if found_user:
        print(find.counter,found_user)
    else:
        persons_with_similar_id = sorted(list(filter(lambda x:x.startswith(id) ,persons.keys())))
        if len(persons_with_similar_id):
            for person_id in persons_with_similar_id[:10]:
                print(find.counter,persons[person_id])
        else:
            print(find.counter, 'No user found')

    find.counter+=1
         
find.counter=1


for i in range(100000):
    try:
        command = input().split()
        if command[0]== "Add":
            add(*command[1:])
        elif command[0]=="Find":
            find(command[1])
    except:
        break