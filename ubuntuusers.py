#!/usr/bin/env python3
# coding=utf8

from config import database
from classes.database import Database
from repository.topic import TopicRepository
from repository.thread import ThreadRepository
from repository.user import UserRepository
from repository.post import PostRepository
from model.topic import Topic
from model.thread import Thread
import requests
import re

db = Database(database['host'], database['user'], database['password'], database['database'])

def get_topics():
    try:
        topics = TopicRepository(db)
        r = requests.get("https://forum.ubuntuusers.de/")
        content = r.content.decode('utf8')
        reg = "<tr\\sclass=\"entry.+?<a.{0,100}href=\"(.{0,100}?)\".+?>(.+?)<"
        topic_ex = re.compile(reg, re.MULTILINE | re.DOTALL)
        matches = topic_ex.finditer(content)
        for m in matches:
            topic = Topic(m.group(2), m.group(1))
            topics.add(topic)
            print("Added Topic: {topic}".format(topic=topic.name))
        return
    except Exception as e:
        print("Request failed:")
        exit(1)

def get_threads(url, topic):
    repository = ThreadRepository(db)
    r = requests.get(url)
    content = r.content.decode('utf8')
    reg = "<td\\sclass=\"topic\".+?<a.{0,100}href=\"(.{0,255}?)\">(.+?)<"
    thread_ex = re.compile(reg, re.MULTILINE | re.DOTALL)
    matches = thread_ex.finditer(content)
    for m in matches:
        thread = Thread(m.group(2), m.group(1), topic.id)
#        print("Thread: {thread}".format(thread=thread.name))
        repository.add(thread)
    reg = "<div\\sclass=\"pagination(.+?)<\\/div>"
    pagex = re.compile(reg, re.DOTALL)
    m = pagex.search(content)
    paginator = m.group(1)
    regex = ".+href=\"(.+?)\"\sclass=\"next\""
    pagex = re.compile(regex, re.DOTALL)
    matches = pagex.match(paginator)
    if matches is None:
        return None
    url = matches.group(1)
    return url

if __name__ == "__main__":
    users = UserRepository(db)
    topics = TopicRepository(db)
    threads = ThreadRepository(db)
    posts = PostRepository(db)
    get_topics()
    page=1
    items=50
    _topics = topics.get_topics(page, items)
    while (_topics != False):
        print(len(_topics))
        for t in _topics:
            url = get_threads(t.url, t)
            prev_url = ""
            while (url is not None):
                url = get_threads(url, t)
        page += 1   
        _topics = topics.get_topics(page, items)
    exit(0)
    for topic in r_topics:
        #print("Topic: {name}".format(name=topic.name))
        topics.add(topic)
        topic = topics.get_by_url(topic.url)
        get_threads(topic, threads)
    db.close()
