# Rasa Menu - Sample Bot

Explore this example of a conversational bot that showcases menu and submenu interactions. This bot allows users to interact with menus using letter-based selections and text-based commands, enhancing user engagement.

Key Features:

Intuitive menu navigation with letter selections.
Seamless transition between main menus and submenus.
Support for direct intent-based commands.
Clear slot management for menu tracking.
This repository serves as a practical demonstration of how to implement menu-driven interactions in Rasa chatbots. Explore the code and documentation to learn more about building conversational experiences with Rasa.

## Detail

In some channels, option buttons cannot be used. The goal is to show a menu with letters so that the user can navigate through different options. Additionally, the user can also type what they want to do.

For example, the bot initially offers:
      This is the main menu:
        A. Info Enterprise
        B. Turns
        C. List People
      Choose an option or type what you are looking for.

Then the user can:
 - Type one of the letters, for example, letter A.
 - Or they can directly type the intention like "I want to know about the enterprise."

Additionally, since there are times when there are many options, there is also the possibility of using a sub-menu.

For example:
The bot initially offers:
      This is the main menu:
        A. Info Enterprise
        B. Turns
        C. List People
      Choose an option or type what you are looking for.

The user can type:
 - Type letter B.

And they will be shown the submenu:
      Please, select an option:
        A. Request a new turn
        B. List your turns
        C. Delete a turn
        D. Back to the main menu

## How It Works
The bot primarily relies on a central slot, known as current_menu, to keep track of the menu the user is currently navigating. When a user attempts to select an option (done through a regular expression that detects letters), the selected option is stored in the current_menu slot. This action is then processed by a custom action, which determines the active menu and the user's choice within that menu.

Maintaining an up-to-date current_menu is crucial. It's activated when a user's intent is a specific menu selection. However, there's also an action in place to clear the slot if the user makes an invalid selection, such as entering a letter that doesn't correspond to any menu item.

Additionally, the bot provides examples of calling actions or utterances as part of its functionality.

This architecture ensures smooth navigation through menus, allowing users to interact with the bot effectively.

## Install dependencies

Run :
```bash
pip install -r requirements.txt
```

## Run the bot

Use `rasa train` to train a model. It is also possible to generate training data for scenarios (stories) by using [interactive learning](https://rasa.com/docs/rasa/writing-stories/#using-interactive-learning) with the command:
```
rasa interactive -m {path_to_a_model} 
```
> If there is no model already trained, you can remove the argument. Rasa will train the model with actual data.


Then, to run the bot, first set up your action server in one terminal window:
```bash
rasa run actions
```

In another window, you can talk to the bot by running:
```
rasa shell --debug  
```

It is also possible to do the two above with a single command:  
```
rasa run actions & rasa shell --debug  
```

> Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working under the hood. To simply talk to the bot, you can remove this flag.


## Overview of the files

`data/stories.yml` - contains [stories](https://rasa.com/docs/rasa/stories/)

`data/rules.yml` - contains [rules](https://rasa.com/docs/rasa/rules)

`data/nlu/` - contains [NLU training data](https://rasa.com/docs/rasa/nlu-training-data)

`actions/actions.py` - contains [custom action](https://rasa.com/docs/rasa/custom-actions)/api calls code

`domain.yml`         - the [domain](https://rasa.com/docs/rasa/domain) file, including bot response templates

`config.yml`         - training [configurations](https://rasa.com/docs/rasa/model-configuration) for the NLU pipeline and policy ensemble

## Contributing

Feel free to make a PR or report an issue