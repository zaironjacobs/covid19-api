def parse_news(news) -> dict:
    """ Parse the database results into a Python dictionary """

    return {
        'title': news.get('title'),
        'source_name': news.get('source_name'),
        'author': news.get('author'),
        'description': news.get('description'),
        'url': news.get('url'),
        'published_at': news.get('published_at')
    }
