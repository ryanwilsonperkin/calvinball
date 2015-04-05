"""Action in a Calvinball game."""

class Action(object):
    """Action in a Calvinball game."""

    def __init__(self, verb, preposition, obj):
        self.verb = verb
        self.preposition = preposition
        self.object = obj

    def is_valid(self, language):
        """Returns true if the action is valid according to the language."""
        return (self.verb in language.verbs and
                self.preposition in language.prepositions and
                self.object in language.objects)

    @classmethod
    def parse(cls, action_string):
        """Parse action_string into VERB PREPOSITION OBJECT for new Action."""
        tokens = action_string.split(' ', 2)
        if len(tokens) != 3:
            raise ValueError('expected 3 tokens in action_string')
        return cls(*(token.lower() for token in tokens))
