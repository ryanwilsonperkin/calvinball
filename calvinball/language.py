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

    def to_json(self):
        """Serialize this Language instance to JSON."""
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

def load(json_file):
    """Load json file into a new Language object."""
    contents = json.load(json_file)
    modals = contents[u'modals']
    verbs = contents[u'verbs']
    prepositions = contents[u'prepositions']
    objects = contents[u'objects']
    return Language(modals, verbs, prepositions, objects)
