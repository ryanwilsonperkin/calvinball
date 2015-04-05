"""Rule in a Calvinball game."""

import json

class Rule(object):
    """Rule in a Calvinball game."""

    def __init__(self, rule_string):
        self.tokens = rule_string.split(' ', 3)
        print self.tokens
        if len(self.tokens) != 4:
            raise ValueError('expected 4 tokens in rule_string')
        self.modal = self.tokens[0].lower()
        self.verb = self.tokens[1].lower()
        self.preposition = self.tokens[2].lower()
        self.object = self.tokens[3].lower()

    def allows(self, action):
        """Returns true if this rule allows the action."""
        return not self.forbids(action)

    def forbids(self, action):
        """Returns true if this rule forbids the action."""
        return (self.modal == "cannot" and
                self.verb == action.verb and
                self.preposition == action.preposition and
                self.object == action.preposition)

    def is_valid(self, language):
        """Returns true if the action is valid according to the language."""
        return (self.verb in language.verbs and
                self.preposition in language.prepositions and
                self.object in language.objects)

    def to_json(self):
        """Serialize this Rule instance to JSON."""
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
