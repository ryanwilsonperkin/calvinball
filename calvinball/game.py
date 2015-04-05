"""State of a Calvinball game."""

import json

class Game(object):
    """State of a Calvinball game."""

    def __init__(self, language):
        self.rules = []
        self.language = language

    def add_rule(self, rule):
        """Add rule to game."""
        self.rules.append(rule)

    def remove_rule(self, rule):
        """Remove rule from game."""
        self.rules.remove(rule)

    def get_rules(self):
        """Get list of current rules."""
        return self.rules

    def evaluate(self, action):
        """Return true if action is allowed by current rules."""
        return all(rule.allows(action) for rule in self.rules)

    def to_json(self):
        """Serialize this Game instance to JSON."""
        return json.dumps(
            self,
            sort_keys=True,
            default=lambda o: o.__dict__,
            indent=4
        )
