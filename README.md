# QAMaster

A discord bot to manage questions and answers in a server

## Installing in discord

- Invite the discord bot - [invite link](https://discord.com/oauth2/authorize?client_id=845545262466465824&permissions=3533888&scope=bot)

## How to run locally

- Setup Repository

  - clone the repository

  ```bash
  git clone https://github.com/RITct/QAMaster
  ```

  - Create virtual environment

  ```bash
  python -m venv venv
  ```

  - activate virtual environment

    - Unix or MacOS

        ```bash
        source venv/bin/activate
        ```

    - Windows

        ```Batchfile
        venv\Scripts\activate.bat
        ```

  - install dependencies

  ```bash
  python -m pip install -r requirements.txt
  ```

- Setup discord bot authentication
  - [Create a bot account](https://discordpy.readthedocs.io/en/stable/discord.html)

  - set Environment variable 'DISCORD_TOKEN' to the token given after creation

  - create a personal server in discord and [invite your bot](https://discordpy.readthedocs.io/en/stable/discord.html#inviting-your-bot) there

- Run the bot locally

  ```bash
  python QAMaster/bot.py
  ```
