#!/usr/bin/python3
#coding=utf8

from config import database
from classes.database import Database
from repository.topic import TopicRepository
from repository.thread import ThreadRepository
from repository.user import UserRepository
from model.topic import Topic
from model.thread import Thread
import requests
import re

def get_topics():
    topics = []
    r = requests.get("https://forum.ubuntuusers.de/")
    content = r.content.decode('utf8')
    reg = "<tr\sclass=\"entry.+?<a.{0,100}href=\"(.{0,100}?)\".+?>(.+?)<"
    topicex = re.compile(reg, re.MULTILINE | re.DOTALL)
    matches = topicex.finditer(content)
    for m in matches:
        topic = Topic(m.group(2), m.group(1))
        topics.append(topic)
    return topics

def get_threads(url, topic, repository):
    r = requests.get(url)
    content = r.content.decode('utf8')
    reg = "<td\sclass=\"topic\".+?<a.{0,100}href=\"(.{0,255}?)\">(.+?)<"
    threadex = re.compile(reg, re.MULTILINE | re.DOTALL)
    matches = threadex.finditer(content)
    for m in matches:
        thread = Thread(m.group(2), m.group(1), topic.id)
        repository.add(thread)
    reg = "<div\sclass=\"pagination(.+?)<\/div>"
    pagex = re.compile(reg, re.DOTALL)
    m = pagex.search(content)
    paginator = m.group(1)
    regex = ".+href=\"(.+?)\""
    pagex = re.compile(regex, re.DOTALL)
    matches = pagex.match(paginator)
    next_page = matches.group(1)
    if next_page == url:
        return
    get_threads(next_page, topic, repository)

    



if __name__ == "__main__":
    db = Database(database['host'], database['user'], database['password'], database['database'])
    users = UserRepository(db)
    topics = TopicRepository(db)
    threads = ThreadRepository(db)
    r_topics = get_topics()
    for topic in r_topics:
        topics.add(topic)
        topic = topics.get_by_url(topic.url)
        r_threads = get_threads(topic.url, topic, threads)
    db.close()

    

