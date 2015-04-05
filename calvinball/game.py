"""State of a Calvinball game."""

import json

from rule import Rule

class Game(object):
    """State of a Calvinball game."""

    def __init__(self):
        self.rules = []

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

    def save(self, json_fp):
        """Save json serialization of this game to json_fp."""
        json.dump(
            self,
            json_fp,
            sort_keys=True,
            default=lambda o: o.__dict__,
            indent=4
        )

    @classmethod
    def load(cls, game_fp):
        """Load game instance from game_fp file."""
        game = cls()
        contents = json.load(game_fp)
        for rule in contents[u'rules']:
            modal = rule[u'modal']
            verb = rule[u'verb']
            preposition = rule[u'preposition']
            obj = rule[u'object']
            game.add_rule(Rule(modal, verb, preposition, obj))
        return game
