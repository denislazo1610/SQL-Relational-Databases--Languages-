class values:
    def __init__(self, username, password, NativeLanguage, LearningLanguage, minutes, joinDate):
        self.username = username
        self.password = password
        self.NativeLanguage = NativeLanguage
        self.LearningLanguage = LearningLanguage
        self.minutes = minutes
        self.joinDate = joinDate

     @classmethod
    def from_input(cls):
        return cls(
            input('Username: '),
            input('Password: '),
            input('Native Language: '),
            input('Learning a language: '),
            input('Minutes spend: '),
            input('Date of joining: ')
        )


