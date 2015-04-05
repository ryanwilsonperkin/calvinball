"""Play a game of Calvinball."""

from __future__ import print_function

import argparse
import logging
import logging.config
import os

from action import Action
from game import (Game, DuplicateRuleException, NonexistentRuleException,
                  ForbiddenActionException)
from language import Language, InvalidActionException, InvalidRuleException
from rule import Rule

DATA_DIR = os.path.dirname(os.path.realpath(__file__))
LANGUAGE_FILE = os.path.join(DATA_DIR, 'language.json')
GAME_FILE = os.path.join(DATA_DIR, 'calvinball.json')
LOG_CONFIG_FILE = os.path.join(DATA_DIR, 'logging.conf')

# Load logging configuration
logging.config.fileConfig(LOG_CONFIG_FILE)
LOGGER = logging.getLogger(__name__)

def add_rule(game, language, rule_string):
    """Add a new rule to the database."""
    try:
        rule = Rule.parse(rule_string)
        language.validate_rule(rule)
        game.add_rule(rule)
    except ValueError:
        LOGGER.error('syntax error in rule "%s"', rule_string)
        print('syntax error: RULE is MODAL VERB PREPOSITION OBJECT')
    except InvalidRuleException:
        LOGGER.error('invalid token in rule "%s"', rule_string)
        print('syntax error: invalid token in rule')
    except DuplicateRuleException:
        LOGGER.error('attempt to add duplicate rule "%s"', rule)
        print('Rule exists.')
    else:
        LOGGER.info('successfully added "%s"', rule)
        print('Rule added.')

def remove_rule(game, language, rule_string):
    """Remove a rule from the database."""
    try:
        rule = Rule.parse(rule_string)
        language.validate_rule(rule)
        game.remove_rule(rule)
    except ValueError:
        LOGGER.error('syntax error in rule "%s"', rule_string)
        print('syntax error: RULE is MODAL VERB PREPOSITION OBJECT')
    except InvalidRuleException:
        LOGGER.error('invalid token in rule "%s"', rule_string)
        print('syntax error: invalid token in rule')
    except NonexistentRuleException:
        LOGGER.info('attempt to remove nonexistent rule "%s"', rule)
        print('Rule does not exist.')
    else:
        LOGGER.info('successfully removed "%s"', rule)
        print('Rule removed.')

def list_rules(game):
    """List rules of the game."""
    for rule in game.get_rules():
        print(rule)

def evaluate(game, language, action_string):
    """Evaluate an action."""
    try:
        action = Action.parse(action_string)
        language.validate_action(action)
        game.evaluate(action)
    except ValueError:
        LOGGER.error('syntax error in action "%s"', action_string)
        print('syntax error: ACTION is VERB PREPOSITION OBJECT')
    except InvalidActionException:
        LOGGER.error('invalid token in action "%s"', action_string)
        print('syntax error: invalid token in action')
    except ForbiddenActionException:
        LOGGER.error('action "%s" is forbidden by rules', action)
        print('Action failed.')
    else:
        LOGGER.info('successfully evaluated "%s"', action)
        print('Action succeeded.')

def create_parser():
    """Create a command line argument parser."""
    parser = argparse.ArgumentParser(description=main.__doc__)
    subparsers = parser.add_subparsers(
        dest='subcommand',
        help='Available subcommands.'
    )
    parser_add = subparsers.add_parser(
        'add',
        help='Add a new rule to the database.'
    )
    parser_add.add_argument(
        'rule',
        metavar='RULE',
        help='The rule to be added.'
    )
    parser_remove = subparsers.add_parser(
        'remove',
        help='Remove a rule from the database.'
    )
    parser_remove.add_argument(
        'rule',
        metavar='RULE',
        help='The rule to be removed'
    )
    parser_evaluate = subparsers.add_parser(
        'evaluate',
        help='Evaluate an action.'
    )
    parser_evaluate.add_argument(
        'action',
        metavar='ACTION',
        help='The action to be evaluated.'
    )
    subparsers.add_parser(
        'list',
        help='List rules in the database.'
    )
    return parser

def main():
    """Play a game of calvinball."""

    # Parse arguments and take action
    args = create_parser().parse_args()

    # Load language
    try:
        with open(LANGUAGE_FILE) as language_fp:
            language = Language.load(language_fp)
    except IOError:
        LOGGER.error('could not read from language file "%s"', LANGUAGE_FILE)
        raise
    else:
        LOGGER.info('loaded language from file "%s"', LANGUAGE_FILE)

    # Initialize game
    try:
        with open(GAME_FILE) as game_fp:
            game = Game.load(game_fp)
    except IOError:
        LOGGER.info('could not read from game file "%s"', GAME_FILE)
        game = Game()
        LOGGER.info('created new game')
    else:
        LOGGER.info('loaded game from file "%s"', LANGUAGE_FILE)

    if args.subcommand == 'add':
        add_rule(game, language, args.rule)
    elif args.subcommand == 'remove':
        remove_rule(game, language, args.rule)
    elif args.subcommand == 'evaluate':
        evaluate(game, language, args.action)
    elif args.subcommand == 'list':
        list_rules(game)

    try:
        with open(GAME_FILE, 'w') as game_fp:
            game.save(game_fp)
    except IOError:
        LOGGER.error('could not write to game file "%s"', GAME_FILE)
        raise
    else:
        LOGGER.info('saved game to file "%s"', GAME_FILE)

if __name__ == '__main__':
    main()
