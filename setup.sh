#!/bin/bash

if [[ $EUID -eq 0 ]]; then
  echo "This script should not be run as root!" 2>&1
  exit 1
fi

function run_program {
  read -p "Do you want to run the program now? (y/n) " choice
  case "$choice" in
    y|Y )
      python3 main.py
      ;;
    n|N )
      echo "Exit program."
      ;;
    * )
      echo "Invalid choice. Exiting."
      ;;
  esac
}

function edit_token {
  read -p "form now on need to edit your token.json file, input your token here: " token

  sed -i "s/\"token\": \".*\"/\"token\": \"$token\"/" token.json
  run_program
}

read -p "Now will install pyTelegramBotAPI, pyyaml module (y/n) " install_module
case "$install_module" in
  y|Y )
    pip3 install pyTelegramBotAPI pyyaml
    ;;
  n|N )
    edit_token
    ;;
  * )
    echo "Invalid choice. Exiting."
    exit 1
    ;;
esac