class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            return self._title
        elif isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            print("Title must be a string between 5 and 50 characters.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        self._magazine = magazine
    


class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            return self._name
        elif isinstance(name, str) and 0 < len(name):
            self._name = name
        else:
            print("Name cannot be an empty string.")


    def articles(self):
        return [article for article in Article.all if article.author == self]
        pass

    def magazines(self):
        return list(set(article.magazine for article in self.articles())) 
        pass

    def add_article(self, magazine, title):
        return Article(self, magazine, title)  

    def topic_areas(self):
        magazine_categories = [article.magazine.category for article in self.articles()]  
        return list(set(magazine_categories)) if magazine_categories else None  
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            print("Name must be a string between 2 and 16 characters inclusive.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category= category
        else:
            print("Category cannot be an empty string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        pass 

    def contributors(self):
        return list(set(article.author for article in self.articles()))
        pass

    def article_titles(self):
        titles = [article.title for article in self.articles()]  
        return titles if titles else None  
        pass

    def contributing_authors(self):
        author_counts = {}  
        for article in self.articles():  
            author = article.author  
            author_counts[author] = author_counts.get(author, 0) + 1  
             
        contributing_authors = [author for author, count in author_counts.items() if count > 2]  
        return contributing_authors if contributing_authors else None  
        pass