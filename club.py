class Club:
    def __init__(self, name, description, tags, likes):
        self.name = name
        self.tags = tags
        self.description = description
        self.likes = likes

    def set_name(self, name):
        self.name = name

    def set_tags(self, tags):
        self.tags = tags

    def set_description(self, description):
        self.description = description

    def set_likes(self, likes):
        self.likes = likes

    def get_name(self):
        return self.name

    def get_tags(self):
        return self.tags

    def get_description(self):
        return self.description

    def get_likes(self):
        return self.likes

