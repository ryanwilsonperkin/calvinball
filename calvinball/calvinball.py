"""Play a game of Calvinball."""

from __future__ import print_function

import argparse
import logging
import logging.config
import os

from action import Action
from game import Game
from language import Language
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
    rule = Rule.parse(rule_string)
    if language.valid_rule(rule):
        game.add_rule(rule)
    else:
        print('Invalid rule.')

def remove_rule(game, language, rule_string):
    """Remove a rule from the database."""
    rule = Rule.parse(rule_string)
    if language.valid_rule(rule):
        game.remove_rule(rule)
    else:
        print('Invalid rule.')

def evaluate(game, language, action_string):
    """Evaluate an action."""
    action = Action.parse(action_string)
    if language.valid_action(action):
        game.evaluate(action)
    else:
        print('Invalid action')

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
