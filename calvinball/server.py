"""Serve up a game of Calvinball."""

import json
import logging

import web

from action import Action
from game import (Game, DuplicateRuleException, NonexistentRuleException,
                  ForbiddenActionException)
from language import Language, InvalidActionException, InvalidRuleException
from rule import Rule

LOGGER = logging.getLogger(__name__)

URLS = (
    '/add', 'AddRule',
    '/remove', 'RemoveRule',
    '/list', 'ListRules',
)

APP = web.application(URLS, globals())

SEMANTIC_ERROR, SYNTAX_ERROR, LOGICAL_ERROR = range(3)

class AddRule:
    """Respond to POST /add requests."""

    def POST(self):
        """Add a new rule to the database."""
        i = web.input()
        web.header('Content-Type', 'application/json')
        try:
            rule = Rule.parse(i.rule_string)
            INSTANCE['language'].validate_rule(rule)
            INSTANCE['game'].add_rule(rule)
        except ValueError:
            LOGGER.error('syntax error in rule "%s"', i.rule_string)
            return error_response(SEMANTIC_ERROR,
                                  'RULE is MODAL VERB PREPOSITION OBJECT')
        except InvalidRuleException:
            LOGGER.error('invalid token in rule "%s"', i.rule_string)
            return error_response(SYNTAX_ERROR, 'invalid token in rule')
        except DuplicateRuleException:
            LOGGER.error('attempt to add duplicate rule "%s"', rule)
            return error_response(LOGICAL_ERROR, 'rule exists')
        else:
            LOGGER.info('successfully added "%s"', rule)
            return success_response('Rule added.')

class RemoveRule:
    """Respond to POST /remove requests."""

    def POST(self):
        """Remove a rule from the database."""
        i = web.input()
        web.header('Content-Type', 'application/json')
        try:
            rule = Rule.parse(i.rule_string)
            INSTANCE['language'].validate_rule(rule)
            INSTANCE['game'].remove_rule(rule)
        except ValueError:
            LOGGER.error('syntax error in rule "%s"', i.rule_string)
            return error_response(SEMANTIC_ERROR,
                                  'RULE is MODAL VERB PREPOSITION OBJECT')
        except InvalidRuleException:
            LOGGER.error('invalid token in rule "%s"', i.rule_string)
            return error_response(SYNTAX_ERROR, 'invalid token in rule')
        except NonexistentRuleException:
            LOGGER.info('attempt to remove nonexistent rule "%s"', rule)
            return error_response(LOGICAL_ERROR, 'rule does not exist')
        else:
            LOGGER.info('successfully removed "%s"', rule)
            return success_response('Rule removed.')

class ListRules:
    """Respond to GET /list requests."""

    def GET(self):
        """List rules of the game."""
        rules = INSTANCE['game'].get_rules()
        return success_response('\n'.join([str(rule) for rule in rules]))

class Evaluate:
    """Respond to POST /evaluate requests."""

    def POST(self):
        """Evaluate an action."""
        i = web.input()
        web.header('Content-Type', 'application/json')
        try:
            action = Action.parse(i.action_string)
            INSTANCE['language'].validate_action(action)
            INSTANCE['game'].evaluate(action)
        except ValueError:
            LOGGER.error('syntax error in action "%s"', i.action_string)
            return error_response(SEMANTIC_ERROR,
                                  'ACTION is VERB PREPOSITION OBJECT')
        except InvalidActionException:
            LOGGER.error('invalid token in action "%s"', i.action_string)
            return error_response(SYNTAX_ERROR, 'invalid token in action')
        except ForbiddenActionException:
            LOGGER.error('action "%s" is forbidden by rules', action)
            return error_response(LOGICAL_ERROR, 'Action failed.')
        else:
            LOGGER.info('successfully evaluated "%s"', action)
            return success_response('Action succeeded.')

def error_response(error_no, msg):
    """Return json encoded error response."""
    error_type = {
        SEMANTIC_ERROR: 'semantic',
        SYNTAX_ERROR: 'syntactic',
        LOGICAL_ERROR: 'logical',
    }.get(error_no)
    response = {
        'error': True,
        'error_type': error_type,
        'error_msg': msg,
        'msg': '',
    }
    return json.dumps(response)

def success_response(msg):
    """Return json encoded success response."""
    response = {
        'error': False,
        'error_type': '',
        'error_msg': '',
        'msg': msg,
    }
    return json.dumps(response)

INSTANCE = dict()

def serve(language, game, game_file):
    """Serve up a game of Calvinball."""
    INSTANCE['language'] = language
    INSTANCE['game'] = game
    INSTANCE['game_file'] = game_file
    APP.run()
