## 模式
### 1、工厂方法模式 (Factory Method)
工厂方法模式定义了一个用于创建对象的接口，但由子类决定实例化的类是哪一个。通过使用工厂方法模式，我们可以轻松地添加新的图标风格，而不需要修改现有代码。
主要角色：
Product（产品）：定义工厂方法所创建的对象的接口。
ConcreteProduct（具体产品）：实现Product接口的具体类。
Creator（创建者）：声明工厂方法，用于返回一个Product对象。创建者类通常包含一个工厂方法的默认实现，该实现可能返回一个具体产品对象。
ConcreteCreator（具体创建者）：重写工厂方法，返回具体产品的实例。
角色关系：
Creator定义了一个工厂方法，允许子类决定创建哪个具体产品对象。
ConcreteCreator具体实现了这个工厂方法，以便实例化具体的产品对象。

### 2、抽象工厂模式 (Abstract Factory)
抽象工厂模式提供一个接口，用于创建相关或依赖对象的家族，而无需明确指定具体类。通过使用抽象工厂模式，我们可以方便地添加新的风格或图标族，而不需要修改现有代码。
主要角色：
AbstractFactory（抽象工厂）：声明创建抽象产品对象的操作。
ConcreteFactory（具体工厂）：实现创建具体产品对象的操作。
AbstractProduct（抽象产品）：为一类产品对象声明接口。
ConcreteProduct（具体产品）：定义一个将被抽象工厂创建的产品对象，需实现AbstractProduct接口。
角色关系：
AbstractFactory定义了一组创建产品的方法，具体工厂类实现这些方法以创建特定的具体产品。
ConcreteFactory实现了创建产品的方法，每个具体工厂对应一个产品家族。
AbstractProduct定义了产品对象的接口，具体产品实现该接口。

### 3、组合模式 (Composite)
组合模式允许将对象组合成树形结构来表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。
主要角色：
Component（抽象构件）：为组合中的对象声明接口，在适当情况下，实现所有类共有接口的默认行为。声明一个接口用于访问和管理Child部件。
Leaf（叶子构件）：在组合中表示叶节点对象，叶节点没有子节点。定义组合中叶节点对象的行为。
Composite（组合构件）：定义有子部件的那些部件的行为。存储子部件并实现与子部件相关的操作。
角色关系：
Component定义了组合对象的接口，并实现了默认行为。
Leaf实现了Component接口，不包含子对象。
Composite实现了Component接口，并包含子对象的添加、移除和访问操作。

### 4、建造者模式（Builder Pattern）
建造者模式是一种创建型设计模式，它允许通过分步骤构建复杂对象，使得创建过程可以更加灵活和可控。建造者模式将对象的构造过程与表示分离，使得相同的构造过程可以创建不同的表示。
主要角色：
Builder（抽象建造者）：定义创建产品各个部件的接口。
ConcreteBuilder（具体建造者）：实现Builder接口，构建和装配各个部件。
Director（指挥者）：负责安排具体建造者的构建步骤。
Product（产品）：由多个部件组成的复杂对象。

# 类图：
FunnyJsonExplorer  
  |  
  1  
 Builder <-------AbstractClass (refer StyleFactory) ------->
  |  
  1  
 JsonBuilder (inherits Builder)

StyleFactory <----- inherit -----> TreeFactory  <---- inherits ---  TreeStyle
               |                          |                                |
               | inherits                 | inherits                       |
               |                          |                                |
 RectangleFactory <----- inherit -----> RectangleStyle
               |
 depends 
IconFamily

FunnyJsonExplorer 与 Builder 之间是 关联 关系，FunnyJsonExplorer 拥有一个 Builder 对象。
Builder 与 StyleFactory 之间是 使用 关系，Builder 依赖于 StyleFactory 来创建不同的样式。
JsonBuilder 继承自 Builder，表示特定的 JSON 构建器。
StyleFactory 被 TreeFactory 和 RectangleFactory 继承，提供具体的工厂实现。
Style 被 TreeStyle 和 RectangleStyle 继承，提供具体的样式实现。
IconFamily 类与 Style 类之间是 依赖 关系，样式需要加载图标家族。

# 为了完成这个任务，做了多方面的工作。
### 1. 学习设计模式概念

首先对设计模式有一个深入的理解，特别是抽象工厂模式和组合模式。

#### 1.1 学习资源
- 经典书籍《设计模式：可复用面向对象软件的基础》（Design Patterns: Elements of Reusable Object-Oriented Software） by Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides。
- 在线教程和文章，诸如https://refactoringguru.cn/、https://www.runoob.com/design-pattern 等编程博客。

#### 1.2 理解主要概念
- **抽象工厂模式**：用于创建相关对象的家族，而无需明确指定它们的具体类。理解如何通过抽象接口来创建一组相关或依赖的对象。
- **组合模式**：处理树形结构，使得单个对象和组合对象具有一致的接口。理解如何通过递归方式构建和遍历树。

### 2. 分析示例代码
分析代码结构，识别出不同的组件和职责。

### 3. 构建类和接口
根据设计模式的要求，创建相应的类和接口：

#### 3.1 抽象工厂类和具体工厂类

- `AbstractFactory`: 定义抽象工厂接口来创建产品。
- `TreeFactory`, `RectangleFactory`: 实现具体工厂类来创建树形和矩形产品。
  
#### 3.2 抽象产品类和具体产品类

- `Style` 抽象类及其子类 `TreeStyle`, `RectangleStyle`：定义和实现不同风格的结构构建方式。
- 抽象的 `Component` 类及其子类 `Leaf` 和 `Composite`：定义树形结构的组件。

#### 3.3 构建器类和具体构建器类

- `Builder` 抽象类及其子类 `RecJsonTreeBuilder`, `TreeJsonTreeBuilder`：实现构建 JSON 树结构的具体逻辑。

### 4. 编写代码

编写和实现上述类和接口，确保它们符合设计模式的要求。包括：

- 接口方法的定义和实现。
- 类的属性与方法的具体执行逻辑。

### 5. 编写测试文件

创建一个 `file.json` 示例文件，用于测试和演示不同工厂和构建器的效果。

### 6. 测试和调试
编写测试用例，在主函数中调用不同的工厂和构建器。

```python
if __name__ == "__main__":
    icon_family_1 = {'container': '♢', 'leaf': '♤'}
    icon_family_2 = {'container': '♡', 'leaf': '♧'}

    explorer_tree1 = FunnyJsonExplorer('file.json', TreeJsonTreeBuilder(TreeFactory(icon_family_1)))
    explorer_tree1.load()
    explorer_tree1.show()

    explorer_tree2 = FunnyJsonExplorer('file.json', TreeJsonTreeBuilder(TreeFactory(icon_family_2)))
    explorer_tree2.load()
    explorer_tree2.show()

    explorer_rec1 = FunnyJsonExplorer('file.json', RecJsonTreeBuilder(RectangleFactory(icon_family_1)))
    explorer_rec1.load()
    explorer_rec1.show()

    explorer_rec2 = FunnyJsonExplorer('file.json', RecJsonTreeBuilder(RectangleFactory(icon_family_2)))
    explorer_rec2.load()
    explorer_rec2.show()
```

### 总结
在这一过程中，不仅需要理论的基础，还需要大量的实践经验和细心的调试工作。这不仅加强了我对设计模式的深刻理解，也提升了我的实践能力。