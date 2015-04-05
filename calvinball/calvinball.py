"""Play a game of Calvinball."""

import argparse
import os

from action import Action
from game import Game
from language import Language, load
from rule import Rule

DATA_DIR = os.path.dirname(os.path.realpath(__file__))
LANGUAGE_FILE = os.path.join(DATA_DIR, 'language.json')
GAME_FILE = os.path.join(DATA_DIR, 'calvinball.json')

def add_rule(game, language, rule_string):
    """Add a new rule to the database."""
    rule = Rule.parse(rule_string)
    game.add_rule(rule)

def remove_rule(game, language, rule_string):
    """Remove a rule from the database."""
    rule = Rule.parse(rule_string)
    game.remove_rule(rule)

def evaluate(game, language, action_string):
    """Evaluate an action."""
    action = Action.parse(action_string)
    game.evaluate(action)

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

    # Load language
    with open(LANGUAGE_FILE) as language_fp:
        language = load(language_fp)

    # Initialize game
    game = Game()

    # Parse arguments and take action
    args = create_parser().parse_args()
    if args.subcommand == 'add':
        add_rule(game, language, args.rule)
    elif args.subcommand == 'remove':
        remove_rule(game, language, args.rule)
    elif args.subcommand == 'evaluate':
        evaluate(game, language, args.action)

if __name__ == '__main__':
    main()
