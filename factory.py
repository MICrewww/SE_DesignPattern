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
    def getFactory(self):
        if self.style == 'tree':
            return TreeFactory(self.icon_family, self.style)
        elif self.style == 'rectangle':
            return RectangleFactory(self.icon_family, self.style)
        else:
            print('Invalid style')
            return None
    
    def getStyle(self):
        if self.style == 'tree':
            return TreeStyle(self.icon_family, self.style)
        elif self.style == 'rectangle':
            return RectangleStyle(self.icon_family, self.style)
        else:
            print('Invalid style')
            return None



# 具体 TreeFactory 类
class TreeFactory(StyleFactory):
    def __init__(self, name, icon):
        super().__init__(name, icon)
        self.icon = icon['factory']
        self.children = []
    def getStyle(self):
        self.style = TreeStyle(self.icon_family)
        return self.style
    def get_root(self):
        return self.root
    def setEvetyNodeTotalNum(self):
        pass
    def add_child(self, child):
        self.children.append(child)
    def isFactory(self):
        return True
    def draw(self, isBottom=False, prefix=""):
        if isBottom:
            line = "└─ " + str(self.icon) + str(self.name) + " "
        else:
            line = "├─ " + str(self.icon) + str(self.name) + " "
        line = prefix + line
        if self.level > 0:
            print(line)
            if isBottom:
                prefix = prefix + "   "
            else:
                prefix = prefix + "│  "
        for i in range(len(self.children)):
            if(i == len(self.children) - 1):
                self.children[i].draw(True, prefix)
            else:
                self.children[i].draw(False, prefix)


# 具体 RectangleFactory 类
class RectangleFactory(StyleFactory):
    def __init__(self, name, icon):
        super().__init__(name, icon)
        self.icon = icon['factory']
        self.children = []
    def getStyle(self):
        self.style = RectangleStyle(self.icon_family)
        return self.style
    def get_root(self):
        return self.root
    def setEvetyNodeTotalNum(self):
        pass
    def add_child(self, child):
        self.children.append(child)
    def isFactory(self):
        return True
    def draw(self):
        line = ''
        if self.num == 1:
            line = "┌─ " + str(self.icon) + str(self.name) + " "
        else:
            line = "├─ " + str(self.icon) + str(self.name) + " "
        for i in range(self.level - 1):
            line = "│  " + line
        for i in range(self.size - len(line) - 1):
            line += "─"
        if self.num == 1:
            line += "┐"
        else:
            line += "┤"
        if self.num > 0:
            print(line)
        for child in self.children:
            child.draw()


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
    def __init__(self, icon_family):
        self.icon_family = icon_family
        self.root = None
        self.children = []
        self.level = 0
        self.num = 0
        self.total_num = 0
        self.name = "root"
        self.icon = icon_family['style']
        self.size = 60
        self.style = 'tree'
    def build_root(self):
        self.root = TreeFactory(self.name, self.icon)
        self.root.setLevel(0)
        self.root.setNum(1)
    def build_children(self, parent, data):
        for key, value in data.items():
            if isinstance(value, dict):
                child = TreeFactory(key, self.icon_family)
                child.setLevel(parent.getLevel() + 1)
                child.setNum(parent.num + 1)
                parent.add_child(child)
                self.build_children(child, value)
            else:
                child = TreeStyle(key, self.icon_family)
                child.setLevel(parent.getLevel() + 1)
                child.setNum(parent.num + 1)
                parent.add_child(child)
        parent.setTotalNum(parent.num)
    def get_root(self):
        return self.root
    def setEvetyNodeTotalNum(self, node):
        if node.isFactory():
            total_num = 0
            for child in node.children:
                self.setEvetyNodeTotalNum(child)
                total_num += child.total_num
            node.setTotalNum(total_num)
        else:
            node.setTotalNum(1)
    def isFactory(self):
        return False
    def draw(self):
        if isBottom:
            line = "└─ " + str(self.icon) + str(self.name) + " "
        else:
            line = "├─ " + str(self.icon) + str(self.name) + " "
        line = prefix + line
        if self.level > 0:
            print(line)

# 具体 RectangleStyle 类
class RectangleStyle(Style):
    def buildStructure(self):
        return [f'Rectangle structure with {self.icon_family} icons']
    def __init__(self, icon_family):
        self.icon_family = icon_family
        self.root = None
        self.children = []
        self.level = 0
        self.num = 0
        self.total_num = 0
        self.name = "root"
        self.icon = icon_family['rectangle']
        self.size = 60
        self.style = 'rectangle'
    def build_root(self):
        self.root = RectangleFactory(self.name, self.icon)
        self.root.setLevel(0)
        self.root.setNum(1)
    def build_children(self, parent, data):
        for key, value in data.items():
            if isinstance(value, dict):
                child = RectangleFactory(key, self.icon_family)
                child.setLevel(parent.getLevel() + 1)
                child.setNum(parent.num + 1)
                parent.add_child(child)
                self.build_children(child, value)
            else:
                child = RectangleStyle(key, self.icon_family)
                child.setLevel(parent.getLevel() + 1)
                child.setNum(parent.num + 1)
                parent.add_child(child)
        parent.setTotalNum(parent.num)
    def get_root(self):
        return self.root
    def setEvetyNodeTotalNum(self, node):
        if node.isFactory():
            total_num = 0
            for child in node.children:
                self.setEvetyNodeTotalNum(child)
                total_num += child.total_num
            node.setTotalNum(total_num)
        else:
            node.setTotalNum(1)
    def isFactory(self):
        return False
    def draw(self):
        if self.num == self.total_num:
            line = "└─ " + str(self.icon) + str(self.name) + " "
            for i in range(self.level - 1):
                line = "└──" + line
        else:
            line = "├─ " + str(self.icon) + str(self.name) + " "
            for i in range(self.level - 1):
                line = "│  " + line
        for i in range(self.size - len(line) - 1):
            line += "─"
        if self.num == self.total_num:
            line += "┘"
        else:
            line += "┤"
        print(line)

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

# 具体建造者
 
class JsonBuilder(Builder):
    def build_product(self):
        style = self.factory.getStyle()
        self.output = style.buildStructure()
    def get_root(self):
        return self.root
    def setEvetyNodeTotalNum(self, node):
        pass





class RecJsonTreeBuilder(JsonBuilder):
    def __init__(self, icon_family, size):
        factory = RectangleFactory(icon_family)
        super().__init__(factory)
        self.size = size

    def build_product(self):
        style = self.factory.getStyle()
        self.output = style.buildStructure() + [f'Rectangle size: {self.size}']
    def setEvetyNodeTotalNum(self, node):
        node.setTotalNum(1)
        for child in node.children:
            self.setEvetyNodeTotalNum(child)



class TreeJsonTreeBuilder(JsonBuilder):
    def __init__(self, icon_family):
        factory = TreeFactory(icon_family)
        super().__init__(factory)
    def build_product(self):
        style = self.factory.getStyle()
        self.output = style.buildStructure()





class FunnyJsonExplorer:
    def __init__(self, file, builder):
        self.root = None
        self.file_path = file
        self.builder = builder
        self._load()

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