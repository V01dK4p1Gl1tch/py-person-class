class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self    


def create_person_list(people: list) -> list:
    Person.people.clear()
    for p_dict in people:
        Person(p_dict["name"], p_dict["age"])

    result_list = []
    for p_dict in people:
        name = p_dict["name"]
        instance = Person.people[name]

        spouse_key = "wife" if "wife" in p_dict else "husband"
        spouse_name = p_dict[spouse_key]

        if spouse_name is not None:
            setattr(instance, spouse_key, Person.people[spouse_name])
            
        result_list.append(instance)
        
    return result_list
