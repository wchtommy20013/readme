# Dependency Injection

## Principle
1. Use of interfaces
   - State explicitly what feature is available
   - Implicit implementation
   - Concept of expected `input -> f(x) -> output`
2. Inverse of Control


## Optimization
- Put all definitions of dependency in the top-most level of the code -> Main
    - Less concern to deeper part of code
    - Seniors concern structure and interfaces, Juniors handle the real implementation
- Use of IoC Framework
    - Optimization by pre-processing and caching
    - Pre-loading time is relatively long (preparation time)
    - Static variables can break things -> state changes will affect the pre-built cache 

## IoC Framework
- StrangeIoC (Unity)