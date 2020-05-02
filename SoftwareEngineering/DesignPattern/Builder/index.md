Builder pattern
===

<img src='./.img/Builder.jpg' style="background-color: white; padding: 10px;"/>

Provide a flexible solution to various object creation problems in object-oriented programming. The intent of the Builder design pattern is to separate the construction of a complex object from its representation.


Example
---

- [C#](./csharp/Builder.cs)
- [Typescript](./typescript/Builder.ts)


Advantage
---

- Allows you to vary a product's internal representation.
- Encapsulates code for construction and representation.
- Provides control over steps of construction process.


Disadvantages
---

- Requires creating a separate ConcreteBuilder for each different type of product.
- Requires the builder classes to be mutable.
- Dependency injection may be less supported.
