import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка запроса: {response.status_code}")
        return

    posts = response.json()

    first_five_posts = posts[:5]

    for i, post in enumerate(first_five_posts, start=1):
        print(f"Пост #{i}")
        print(f"Заголовок: {post['title']}")
        print(f"Текст: {post['body']}")
        print("-" * 40)


if __name__ == "__main__":
    fetch_posts()