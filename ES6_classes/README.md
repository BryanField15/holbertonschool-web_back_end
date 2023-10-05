# Class Foundations in JavaScript

## Learning Outcomes

Through this project, I've achieved a deeper understanding of the core principles of object-oriented programming in JavaScript. Specifically:

- I've grasped **how to define a class** and structure its blueprint for objects.
- I've learned **how to enrich classes by adding methods**, enabling objects to perform actions.
- Discovering **the concept of static methods** was enlightening; I now understand their utility and know how to implement them in a class.
- **Class inheritance** is a powerful concept; I've delved into how one class can extend from another, inheriting its properties and methods.
- Venturing into the realm of **metaprogramming and symbols**, I've realized the potential of manipulating object behavior dynamically.

It's been a transformative journey, moving beyond the rudimentary aspects of JS to its profound, object-oriented capabilities.

## Tasks

*Here, you can list down the tasks or challenges you undertook as part of the project.*

---
## Tasks

---

### 0. You used to attend a place like this at some point
**Filename**: `0-classroom.js`

**Description**:
  - Implement a class named `ClassRoom`.
  - The class should accept one attribute: `maxStudentsSize` (which is a number).
  - This attribute should be assigned to `_maxStudentsSize`.

---

### 1. Let's make some classrooms
**Filename**: `1-make_classrooms.js`

**Description**:
  - Import the `ClassRoom` class from `0-classroom.js`.
  - Implement a function named `initializeRooms`.
  - This function should return an array of 3 `ClassRoom` objects with the sizes 19, 20, and 34 (in this order).

---

### 2. A Course, Getters, and Setters
**Filename**: `2-hbtn_course.js`

**Description**:
  - Implement a class named `HolbertonCourse`.
  - The class should have the following constructor attributes:
    - `name` (String)
    - `length` (Number)
    - `students` (array of Strings)
  - Ensure type verification for attributes during object creation.
  - Each attribute must be stored in an “underscore” version of the attribute (e.g., `name` is stored in `_name`).
  - Implement a getter and setter for each attribute.

---

### 3. Methods, static methods, computed methods names..... MONEY
**Filename**: `3-currency.js`

**Description**:
  - Implement a class named `Currency`.
  - The class should have the following constructor attributes:
    - `code` (String)
    - `name` (String)
  - Each attribute must be stored in an “underscore” version of the attribute (e.g., `name` is stored in `_name`).
  - Implement a getter and setter for each attribute.
  - Implement a method named `displayFullCurrency` that will return the attributes in the format: `name (code)`.

---
### 4. Pricing
**Filename**: `4-pricing.js`

**Description**:
  - Import the class `Currency` from `3-currency.js`.
  - Implement a class named `Pricing`.
  - The class should have the following constructor attributes:
    - `amount` (Number)
    - `currency` (Currency)
  - Each attribute must be stored in an “underscore” version of the attribute (e.g., `name` is stored in `_name`).
  - Implement a getter and setter for each attribute.
  - Implement a method named `displayFullPrice` that will return the attributes in the format: `amount currency_name (currency_code)`.
  - Implement a static method named `convertPrice`. It should accept two arguments: `amount` (Number) and `conversionRate` (Number). The function should return the amount multiplied by the conversion rate.

---

