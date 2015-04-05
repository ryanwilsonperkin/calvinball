"""Rule in a Calvinball game."""

class Rule(object):
    """Rule in a Calvinball game."""

    def __init__(self, modal, verb, preposition, obj):
        self.modal = modal
        self.verb = verb
        self.preposition = preposition
        self.object = obj

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return '{0}({1})'.format(self.__class__, self.__dict__)

    def __str__(self):
        return '{0} {1} {2} {3}.'.format(
            self.modal,
            self.verb,
            self.preposition,
            self.object
        ).capitalize()

    def allows(self, action):
        """Returns true if this rule allows the action."""
        return not self.forbids(action)

    def forbids(self, action):
        """Returns true if this rule forbids the action."""
        return (self.modal == "cannot" and
                self.verb == action.verb and
                self.preposition == action.preposition and
                self.object == action.object)

    @classmethod
    def parse(cls, rule_string):
        """Parse rule_string into MODAL VERB PREPOSITION OBJECT for new Rule."""
        tokens = rule_string.split(' ', 3)
        if len(tokens) != 4:
            raise ValueError('expected 4 tokens in rule_string')
        return cls(*(token.lower() for token in tokens))
