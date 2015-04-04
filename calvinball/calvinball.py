"""State of a Calvinball game."""

class Calvinball(object):
    """State of a Calvinball game."""

    def __init__(self):
        self.__rules = []

    def add_rule(self, rule):
        """Add rule to game."""
        self.__rules.append(rule)

    def remove_rule(self, rule):
        """Remove rule from game."""
        self.__rules.remove(rule)

    def get_rules(self):
        """Get list of current rules."""
        return self.__rules

    def evaluate(self, action):
        """Return true if action is allowed by current rules."""
        return all(rule.allows(action) for rule in self.__rules)
