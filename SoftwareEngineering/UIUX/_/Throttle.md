Throttle
===

“Limit” the frequency of multiple sequential calls.

Implementation
---
1. Underscore.js https://underscorejs.org/
  
      `_.debounce`

2. Write your own

    ```js
    function throttle(func, threshhold) {
      var last, timer;
      if (threshhold) threshhold = 250;
      return function () {
        var context = this
        var args = arguments
        var now = +new Date()
        if (last && now < last + threshhold) {  // what's the difference from debounce: threshold
          clearTimeout(timer)
          timer = setTimeout(function () {
            last = now
            func.apply(context, args)
          }, threshhold)
        } else {
          last = now
          fn.apply(context, args)
        }
      }
    }
    ```

Use case example
---
1. Limit scroll calls

[Debounce](Debounce.md) | [Back](../index.md)
