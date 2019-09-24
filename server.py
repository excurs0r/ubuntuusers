#!/usr/bin/python3
#coding=utf8

from classes.database import Database
from classes.user_repository import UserRepository
from classes.post_repository import PostRepository
from classes.topic_repository import TopicRepository
import requests
import re

def get_topics():
    topics = []
    r = requests.get("https://forum.ubuntuusers.de/")
    content = r.content.decode('utf8')
    reg = "<tr\sclass=\"entry.+?<a.{0,100}href=\"(.{0,100}?)\".+?>(.+?)<"
    threadex = re.compile(reg, re.MULTILINE | re.DOTALL)
    matches = threadex.finditer(content)
    for m in matches:
        topics.append((m.group(1), m.group(2)))
    return topics






if __name__ == "__main__":
    db = Database('localhost', 'python3', 'python3', 'python3')
    users = UserRepository(db)
    topics = TopicRepository(db)
    r_topics = get_topics()
    for topic in r_topics:
        print("Adding topic {topic}".format(topic=topic[1]))
        topics.add(topic[1], topic[0])


    

