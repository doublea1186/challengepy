class Club:
    def __init__(self, name, description, tags):
        self.name = name
        self.tags = tags
        self.description = description

    def set_name(self, name):
        self.name = name

    def set_tags(self, tags):
        self.tags = tags

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def get_tags(self):
        return self.tags

    def get_description(self):
        return self.description

