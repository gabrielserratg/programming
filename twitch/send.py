import json
import socket
import re
from time import sleep

with open('config.json', 'r') as f:
    config = json.load(f)


def chat(sock, msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    sock.send("PRIVMSG #{} :{}\r\n".format(config['channel'], msg).encode("utf-8"))


def ban(sock, user):
    """
    Ban a user from the current channel.
    Keyword arguments:
    sock -- the socket over which to send the ban command
    user -- the user to be banned
    """
    chat(sock, ".ban {}".format(user))


def timeout(sock, user, secs=600):
    """
    Time out a user for a set period of time.
    Keyword arguments:
    sock -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    """
    chat(sock, ".timeout {}".format(user, secs))

s = socket.socket()
s.connect((config['HOST'], config['PORT']))
s.send("PASS {}\r\n".format(config['AUTH_PASS']).encode("utf-8"))
s.send("NICK {}\r\n".format(config['AUTH_NICK']).encode("utf-8"))
s.send("JOIN {}\r\n".format(config['channel']).encode("utf-8"))

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
chat(s, "SCRIPTED & SPAM BY IG @gabrielsukinsyn!")

response = ""

while True:
    response = s.recv(2048).decode("utf-8")
    print(response)
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)  # return the entire match
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)

        # Commands
        if message.strip() == "!what":
            chat(s, "sup it's me")
    sleep(1 / (20/30))
