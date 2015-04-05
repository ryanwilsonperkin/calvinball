"""Language of a Calvinball game."""

import json

class Language(object):
    """Language of a Calvinball game."""

    def __init__(self, modals, verbs, prepositions, objects):
        self.modals = modals
        self.verbs = verbs
        self.prepositions = prepositions
        self.objects = objects

    def valid_modal(self, modal):
        """Returns true if modal is valid."""
        return modal in self.modals

    def valid_verb(self, verb):
        """Returns true if verb is valid."""
        return verb in self.verbs

    def valid_preposition(self, preposition):
        """Returns true if preposition is valid."""
        return preposition in self.prepositions

    def valid_object(self, obj):
        """Returns true if object is valid."""
        return obj in self.objects

    def valid_action(self, action):
        """Returns true if the action is valid according to the language."""
        return (action.verb in self.verbs and
                action.preposition in self.prepositions and
                action.object in self.objects)

    def valid_rule(self, rule):
        """Returns true if the action is valid according to the language."""
        return (rule.verb in self.verbs and
                rule.preposition in self.prepositions and
                rule.object in self.objects)

def load(json_file):
    """Load json file into a new Language object."""
    contents = json.load(json_file)
    modals = contents[u'modals']
    verbs = contents[u'verbs']
    prepositions = contents[u'prepositions']
    objects = contents[u'objects']
    return Language(modals, verbs, prepositions, objects)
