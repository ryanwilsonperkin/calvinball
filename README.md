# calvinball

calvinball is a hybrid python/javascript assignment designed to play the
"Calvinball" game made up by Bill Watterson in his cartoon Calvin and Hobbes.

You can interact directly with calvinball by running:

    % python calvinball.py

You'll see usage instructions for the subprograms, they are:

- add: Add a rule to the database
- remove: Remove a rule from the database
- evaluate: Determine if an action is valid
- list: List rules in the database
- serve: Interact with calvinball through a webserver at 0.0.0.0:8080
- "--usage": get usage instructions
- "--help": get help

These subprograms can be run like this:

    % python calvinball add 'Cannot hit with mallet'
    % python calvinball remove 'Cannot hit with mallet'
    % python calvinball evaluate 'Hit with mallet'
    % python calvinball list
    % python calvinball serve
    % python calvinball -h

### Grammar

Rules are of the form: MODAL VERB PREPOSITION OBJECT
Actions are of the form: VERB PREPOSITION OBJECT

The complete grammar of the language can be found in `language.json`.

### Chat bot

calvinball is also chat bot built on the [Hubot][hubot] framework. It was
initially generated by [generator-hubot][generator-hubot], and configured to be
deployed on [Heroku][heroku] to get you up and running as quick as possible.

[heroku]: http://www.heroku.com
[hubot]: http://hubot.github.com
[generator-hubot]: https://github.com/github/generator-hubot

### Running calvinball chat bot Locally

The calvinball chat client interacts through the Slack chat client.
Detailed instructions for configuring the chat bot with your own client can be
found through [Slack's Github][slack-github].

[slack-github]: https://github.com/slackhq/hubot-slack

You can test your hubot by running the following, however some plugins will not
behave as expected unless the [environment variables](#configuration) they rely
upon have been set.

You can start calvinball locally by running:

    % bin/hubot

You'll see some start up output and a prompt:

    [Sat Feb 28 2015 12:38:27 GMT+0000 (GMT)] INFO Using default redis on localhost:6379
    calvinball>

Then you can interact with calvinball by typing `calvinball help`.

    calvinball> calvinball help
    calvinball animate me <query> - The same thing as `image me`, except adds [snip]
    calvinball help - Displays all of the help commands that calvinball knows about.
    ...


### Configuration

