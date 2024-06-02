## Introduction

Welcome to EasyBot! This bot is designed to address common issues related to the absence of sticker packs and language user interfaces on Telegram. It's an open-source project, so if you encounter any problems, feel free to open an issue on this repository.

## What makes EasyBot special?

EasyBot focuses on two main features:

- **Telegram Sticker Packs**
- **Telegram Third-party Languages**

## Getting Started

To begin using EasyBot, you'll need to install the following dependencies:

- **pyyaml**: Used for reading content.
  
  ```shell
  pip3 install pyyaml
  ```

- **pyTelegrambotAPI**: EasyBot is built using pyTelegrambotAPI, which requires Python 3.
  
  ```shell
  pip3 install pyTelegramBotAPI
  ```

### Installation Script

If you find it cumbersome to type multiple commands, you can use the provided setup script:

```shell
./setup.sh
```

### Usage

1. Clone this repository.
2. Edit the `token.json` file and insert your bot API token.
3. Run the command `python3 main.py` on your server.

Once your bot is running, type `/start` to initiate it.

## License

All files in this repository are released under the Apache License 2.0.

For more details, refer to the [LICENSE](./LICENSE) file.
