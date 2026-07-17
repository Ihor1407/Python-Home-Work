class GroupError(Exception):
    def __init__(self, message="Unable to add the student. The group has already reached the limit of 10 people."):
        super().__init__(message)
