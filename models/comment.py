from models.model import Model


class Comment(Model):

    __repository = 'repository.comment_repository'

    def __init__(self, author, text):
        Model.__init__(self)
        self.__author = author
        self.__text = text

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text