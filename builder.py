from abc import ABC, abstractmethod
import json

# IconFamily class
class IconFamily:
    def __init__(self, type):
        self.type = type

    def load_icon_family(self):
        return f"Loading icon family of type: {self.type}"


# 抽象 StyleFactory 类
class StyleFactory(ABC):
    def __init__(self, icon_family):
        self.icon_family = icon_family
        self.style = None

    @abstractmethod
    def getStyle(self):
        pass


# 具体 TreeFactory 类
class TreeFactory(StyleFactory):
    def getStyle(self):
        self.style = TreeStyle(self.icon_family)
        return self.style


# 具体 RectangleFactory 类
class RectangleFactory(StyleFactory):
    def getStyle(self):
        self.style = RectangleStyle(self.icon_family)
        return self.style


# 抽象 Style 类
class Style(ABC):
    def __init__(self, icon_family):
        self.icon_family = icon_family

    @abstractmethod
    def buildStructure(self):
        pass


# 具体 TreeStyle 类
class TreeStyle(Style):
    def buildStructure(self):
        return [f'Tree structure with {self.icon_family} icons']


# 具体 RectangleStyle 类
class RectangleStyle(Style):
    def buildStructure(self):
        return [f'Rectangle structure with {self.icon_family} icons']


# 抽象建造者
class Builder(ABC):
    def __init__(self, factory):
        self.factory = factory
        self.output = []

    @abstractmethod
    def build_product(self):
        pass

    def draw_product(self):
        return self.output

    def draw(self):
        structure = self.draw_product()
        for item in structure:
            print(item)


# 具体建造者 JsonBuilder
class JsonBuilder(Builder):
    def build_product(self):
        style = self.factory.getStyle()
        self.output = style.buildStructure()


class RecJsonTreeBuilder(JsonBuilder):
    def __init__(self, icon_family, size=60):
        factory = RectangleFactory(icon_family)
        super().__init__(factory)
        self.size = size

    def build_product(self):
        super().build_product()
        self.output.append(f"Rectangle size: {self.size}")


class TreeJsonTreeBuilder(JsonBuilder):
    def __init__(self, icon_family):
        factory = TreeFactory(icon_family)
        super().__init__(factory)


class FunnyJsonExplorer:
    def __init__(self, file, builder):
        self.file_path = file
        self.builder = builder
        self.data = self._load_json()

    def _load_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return {}

    def load(self):
        self.builder.build_product()

    def show(self):
        self.builder.draw()


if __name__ == "__main__":
    icon_family_1 = {'container': '♢', 'leaf': '♤'}
    icon_family_2 = {'container': '♡', 'leaf': '♧'}

    # 使用TreeIcon1Factory
    explorer = FunnyJsonExplorer('file.json', TreeFactory(), icon_family_1)
    explorer.load()
    explorer.show()

    # 使用TreeIcon2Factory
    explorer = FunnyJsonExplorer('file.json', TreeFactory(), icon_family_2)
    explorer.load()
    explorer.show()

    # 使用RecIcon1Factory
    explorer = FunnyJsonExplorer('file.json', RecFactory(), icon_family_1)
    explorer.load()
    explorer.show()

    # 使用RecIcon2Factory
    explorer = FunnyJsonExplorer('file.json', RecFactory(), icon_family_2)
    explorer.load()
    explorer.show()
