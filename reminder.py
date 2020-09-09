# coding: utf-8
import random
import requests
import os

members = ["佐倉（不良）", "p-hone", "炭素", "すばる", "rnvneko"]

def random_member():
    member = random.choice(members)
    return "「" + member + "」お題を決めんかい！\nおやすみのときは「/あんこーる」って言うんやで！"

requests.post(os.environ["URL"], json={"content": random_member()})
