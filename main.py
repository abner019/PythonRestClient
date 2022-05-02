# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import json
from types import SimpleNamespace

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    url = 'https://jsonplaceholder.typicode.com/users';
    response = requests.get(url);
    l_users = response.content;
    json_users = json.loads(l_users, object_hook=lambda d: SimpleNamespace(**d))
    for n in (json_users):
        print('############# User Resume ###########')
        print(n.id);
        print(n.name)
        print(n.username)
        print(n.address.city)
        url = 'https://jsonplaceholder.typicode.com/posts?userId' + str(n.id);
        response = requests.get(url);
        data = response.content;
        json_posts = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        for n_post in (json_posts):
            print('##postid##'+ str(n_post.id))
            print('title: ' + n_post.title)
            print('body: ' + n_post.body)
            url = 'https://jsonplaceholder.typicode.com/comments?postId' + str(n_post.id);
            response = requests.get(url);
            data = response.content;
            json_comments = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
            for n_comments in (json_comments):
                print(n_comments.body)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
