# Design Patterns

## Principle
1. Reusable code
2. Loose coupling


## Creational Patterns

1. [Abstract factory](./AbstractFactory/index.md)

    Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

2. [Builder](./Builder/index.md)

    Separate the construction of a complex object from its representation, allowing the same construction process to create various representations.

3. [Dependency Injection](./DependencyInjection/index.md)
    
    A class accepts the objects it requires from an injector instead of creating the objects directly.

4. [Factory method](./FactoryMethod/index.md)
   
    Define an interface for creating a single object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

5. [Lazy initialization](./LazyInitialization/index.md)
   
    Tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed. This pattern appears in the GoF catalog as "virtual proxy", an implementation strategy for the Proxy pattern.

6. Multiton	
   
   Ensure a class has only named instances, and provide a global point of access to them.

7. Object pool
   
   Avoid expensive acquisition and release of resources by recycling objects that are no longer in use. Can be considered a generalisation of connection pool and thread pool patterns.

8. Prototype

    Specify the kinds of objects to create using a prototypical instance, and create new objects from the 'skeleton' of an existing object, thus boosting performance and keeping memory footprints to a minimum.

9.  Resource acquisition is initialization (RAII)
    
    Ensure that resources are properly released by tying them to the lifespan of suitable objects.

10. Singleton
    
    Ensure a class has only one instance, and provide a global point of access to it.

## Structural Patterns

## Behavioral Patterns

## Concurrency Patterns
