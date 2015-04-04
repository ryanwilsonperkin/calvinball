"""Rule in a Calvinball game."""

class Rule(object):
    """Rule in a Calvinball game."""

    def __init__(self, rule_string, language):
        self.tokens = rule_string.split()
        if len(self.tokens) != 4:
            raise ValueError('expected 4 tokens in rule_string')

        self.modal = self.tokens[0].upper()
        self.verb = self.tokens[1].upper()
        self.preposition = self.tokens[2].upper()
        self.object = self.tokens[3].upper()

        if not language.valid_modal(self.modal):
            raise ValueError('invalid modal "{0}"'.format(self.modal))
        if not language.valid_verb(self.verb):
            raise ValueError('invalid verb "{0}"'.format(self.verb))
        if not language.valid_preposition(self.preposition):
            raise ValueError('invalid preposition "{0}"'.format(self.preposition))
        if not language.valid_object(self.object):
            raise ValueError('invalid object "{0}"'.format(self.object))

    def allows(self, action):
        """Returns true if this rule allows the action."""
        return True

    def forbids(self, action):
        """Returns true if this rule forbids the action."""
        return True
