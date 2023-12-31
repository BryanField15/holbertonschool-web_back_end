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

---

### 1. Block Scope
**Filename**: `1-block-scoped.js`

**Description**:
  - Given knowledge on `var` and hoisting, modify the variables inside the function `taskBlock` to ensure the variables aren't overwritten inside the conditional block.

Original Code:

```javascript
export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    var task = true;
    var task2 = false;
  }

  return [task, task2];
}

---

### 2. Arrow Functions
**Filename**: `2-arrow.js`

**Description**:
  - Rewrite the provided standard function to leverage ES6's arrow function syntax. The function `add` should be converted to an anonymous arrow function.

Original Code:

```javascript
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  const self = this;
  this.addNeighborhood = function add(newNeighborhood) {
    self.sanFranciscoNeighborhoods.push(newNeighborhood);
    return self.sanFranciscoNeighborhoods;
  };
}

---

### 3. Parameter Defaults
**Filename**: `3-default-parameter.js`

**Description**:
  - Condense the internals of the provided function to just 1 line without renaming any function or variable.
  - The hint to solve this task is to define default parameter values for the function parameters.

Original Code:

```javascript
export default function getSumOfHoods(initialNumber, expansion1989, expansion2019) {
  if (expansion1989 === undefined) {
    expansion1989 = 89;
  }

  if (expansion2019 === undefined) {
    expansion2019 = 19;
  }
  return initialNumber + expansion1989 + expansion2019;
}

---

### 4. Rest parameter syntax for functions
**Filename**: `4-rest-parameter.js`

**Description**:
  - Modify the function to return the number of arguments passed to it using the rest parameter syntax.

Modified Code:

```javascript
export default function returnHowManyArguments(...args) {
  return args.length;
}

