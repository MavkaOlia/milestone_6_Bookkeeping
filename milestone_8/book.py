class Book:
    def __init__(self, title, category, author, publish_year):
        self.title = title
        self.category = category
        self.author = author
        self.publish_year = publish_year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publish_year}) - {self.category}"
