from abc import ABC, abstractmethod
import json

# IconFamily class
class IconFamily:
    def __init__(self, type):
        self.type = type

    def load_icon_family(self):
        return f"Loading icon family of type: {self.type}"


# 组件类（Component Class）
class Component(ABC):
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

    @abstractmethod
    def draw(self, indent):
        pass


# 叶子类（Leaf Class）
class Leaf(Component):
    def draw(self, indent):
        print(f"{indent}{self.icon} {self.name}")


# 组合类（Composite Class）
class Composite(Component):
    def __init__(self, name, icon):
        super().__init__(name, icon)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, indent):
        print(f"{indent}{self.icon} {self.name}")
        for child in self.children:
            child.draw(indent + "  ")


class Factory(ABC):
    @abstractmethod
    def create_component(self, name, icon_family):
        pass


class TreeFactory(Factory):
    def create_component(self, name, icon_family):
        return Composite(name, icon_family["container"])


class RecFactory(Factory):
    def create_component(self, name, icon_family):
        return Composite(name, icon_family["container"])


class FunnyJsonExplorer:
    def __init__(self, file, factory, icon_family):
        self.file_path = file
        self.factory = factory
        self.icon_family = icon_family
        self.root = self._load_json_to_tree()

    def _load_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return {}

    def _load_json_to_tree(self):
        data = self._load_json()
        root = self.factory.create_component("root", self.icon_family)
        self._build_tree(root, data)
        return root

    def _build_tree(self, parent, data):
        for key, value in data.items():
            if isinstance(value, dict):
                child = self.factory.create_component(key, self.icon_family)
                parent.add(child)
                self._build_tree(child, value)
            else:
                leaf = Leaf(key, self.icon_family["leaf"])
                parent.add(leaf)

    def show(self):
        self.root.draw("")


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
