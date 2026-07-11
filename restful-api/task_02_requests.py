#!/usr/bin/python3
"""Module includes fetch_and_print_posts()
and fetch_and_save_posts() functions"""


import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and prints titles."""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {r.status_code}')
    if r.status_code == requests.codes.ok:
        posts = r.json()
        for p in posts:
            print(p["title"])

def fetch_and_save_posts():
    """Fetch posts and save them to CSV file."""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == requests.codes.ok:
        posts = r.json()
        data = [{"id": p["id"], "title": p["title"], "body": p["body"]}
                for p in posts]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
