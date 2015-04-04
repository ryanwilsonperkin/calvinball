"""Action in a Calvinball game."""

class Action(object):
    """Action in a Calvinball game."""

    def __init__(self, action_string):
        self.tokens = action_string.split(' ', 2)
        if len(self.tokens) != 3:
            raise ValueError('expected 3 tokens in action_string')
        self.verb = self.tokens[0].lower()
        self.preposition = self.tokens[1].lower()
        self.object = self.tokens[2].lower()

    def is_valid(self, language):
        """Returns true if the action is valid according to the language."""
        return (self.verb in language.verbs and
                self.preposition in language.prepositions and
                self.object in language.objects)
