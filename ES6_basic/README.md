# My Learning Objectives

By the end of this project, I've accomplished the following:

- I've grasped the essence of ES6 and the new features it introduced.
- I now understand the difference between a constant and a variable, as well as the concept of block-scoped variables.
- I've delved into the world of arrow functions, learned about their default parameters, and explored rest and spread function parameters.
- I've experienced the convenience of string templating in ES6, got hands-on with new methods of object creation, and recognized their properties.
- I've also mastered iterators and the use of for-of loops in ES6.

## Tasks

---

### 0. Const or let?
**Filename**: `0-constants.js`

**Description**:
  - Modify the function `taskFirst` to instantiate variables using `const`.
  - Modify the function `taskNext` to instantiate variables using `let`.

Original Code:

```javascript
export function taskFirst() {
  var task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  var combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
