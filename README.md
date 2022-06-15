# What is this?

A small Telegram userbot
(a program that acts under the name of an existing regular user account,
and not a ["Telegram bot"](https://core.telegram.org/bots))
that reacts to every message from a certain user (or users) in a certain chat (or in all chats).

# Why?

Because I've seen someone else do it and decided that I want to do it too.
Plus I've wanted to mess around with Telegram's non-bot API for quite a while now.

# How to run it?

0. You will need python (probably 3.8+)
and [dependencies](requirements.txt) installed.
(Hint: use [venv](https://docs.python.org/3/library/venv.html))
1. You will need a [Telegram "API_ID" and "API_HASH"](https://core.telegram.org/api/obtaining_api_id).
And a willingness to potentially sacrifice your Telegram account because I've heard multiple stories
of users unfairly receiving bans from Telegram for using userbots even without any malicious intent
(and spamming with reactions is borderline malicious, so...)
2. Copy the `config.example.py` to `config.py`.
Replace example values with your `api_id` and `api_hash`.
Set the id or @username of a chat you want to run the userbot in,
and ids/@usernames of users whose messages you want to react to.
3. On the first launch you will need to log in.
After that a `[something-something].session` file will be created
and it will store the login info, so you won't need to log in again.
If you want to just login, without launching the userbot, run `login.py` or `login.sh`
(the latter set ups a venv automatically and runs the former).
4. Launch the userbot with `python -m userbot` or `python userbot.py` or `./service/launch.sh`
(the last one automatically sets up a venv for you).
5. ?????
6. That's it. You can also run this as a systemd service, see [this config file](service/reaction-userbot.service).
