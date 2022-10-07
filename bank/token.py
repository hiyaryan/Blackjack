# Token


class Token:

    def __init__(self, face, value):
        '''
        face str: the face or name of the token
        value float: the monetary value of the token
        '''
        self.face = face
        self.value = value

    def __str__(self):
        return f"¢{self.face}: ${self.value}"
