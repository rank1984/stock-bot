name: Stock Bot

on:
  schedule:
    - cron: '20 13 * * 1-5'
  workflow_dispatch:

jobs:
  run-bot:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Install
      run: pip install -r requirements.txt

    - name: Run bot
      run: python bot.py
