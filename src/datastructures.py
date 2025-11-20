"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, first_name, age, lucky_numbers):
        self.age = age
        self.lucky_numbers = lucky_numbers
        ## You have to implement this method
        new_member = {
            'id': self._generate_id(),
            'first_name': first_name,
            'last_name': self.last_name,
            'age': age,
            'lucky_numbers': lucky_numbers
        }
        ## Append the member to the list of _members
        self._members.append(new_member)
        return new_member
     
    def delete_member(self, id):
        ## You have to implement this method
        for item in self._members:
            if item['id'] == id:
                self._members.remove(item)
                return item
        ## Loop the list and delete the member with the given id
        return None

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        for item in self._members:
            if item['id'] == id:
                return item
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members