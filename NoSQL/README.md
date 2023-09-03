# NoSQL and MongoDB Project

This repository is focused on understanding and practicing NoSQL databases, with a special emphasis on MongoDB.

## What I've Learned

- **What NoSQL means:**
  - Understanding the foundational aspects of NoSQL as a non-relational database system.

- **Difference between SQL and NoSQL:**
  - Recognizing the structural and operational differences between SQL and NoSQL databases.

- **What is ACID:**
  - Comprehending the ACID properties that ensure reliable transactions in databases.

- **What is document storage:**
  - Learning the specifics of document-oriented storage in NoSQL databases like MongoDB.

- **NoSQL types:**
  - Exploring various types of NoSQL databases, such as Document-Stores, Key-Value Stores, etc.

- **Benefits of NoSQL:**
  - Understanding the advantages that NoSQL databases offer, such as scalability and flexibility.

- **Querying in NoSQL:**
  - Mastering the art of querying data from NoSQL databases.

- **CRUD in NoSQL:**
  - Gaining hands-on experience in performing CRUD (Create, Read, Update, Delete) operations in NoSQL databases.

- **How to use MongoDB:**
  - Getting acquainted with MongoDB, including how to install it, run basic commands, and interact with it.

## Tasks

---

### 0. List all databases
**Filename**: `0-list_databases`

**Description**:
  - Write a script that lists all databases in MongoDB.

---

### 1. Create a database
**Filename**: `1-use_or_create_database`

**Description**:
  - Write a script that creates or uses the database `my_db`.

---

### 2. Insert document
**Filename**: `2-insert`

**Description**:
  - Write a script that inserts a document in the collection `school`.
  - The document must have one attribute `name` with value "Holberton school".
  - The database name will be passed as an option of the `mongo` command.

---

### 3. All documents
**Filename**: `3-all`

**Description**:
  - Write a script that lists all documents in the collection `school`.

---

### 4. All matches
**Filename**: `4-match`

**Description**:
  - Write a script that lists all documents with `name="Holberton school"` in the collection `school`.

---

### 5. Count
**Filename**: `5-count`

**Description**:
  - Write a script that displays the number of documents in the collection `school`.
  - The database name will be passed as an option of the `mongo` command.

---

### 6. Update
**Filename**: `6-update`

**Description**:
  - Write a script that adds a new attribute to a document in the collection `school`.
  - The script should update only documents with `name="Holberton school"`.
  - The update should add the attribute `address` with the value "972 Mission street".

---

### 7. Delete by match
**Filename**: `7-delete`

**Description**:
  - Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.

---

### 8. List all documents in Python
**Filename**: `8-all.py`

**Description**:
  - Write a Python function that lists all documents in a collection.
  - Prototype: `def list_all(mongo_collection):`
  - Return an empty list if no document is in the collection.

---

### 9. Insert a document in Python
**Filename**: `9-insert_school.py`

**Description**:
  - Write a Python function that inserts a new document in a collection based on `kwargs`.
  - Prototype: `def insert_school(mongo_collection, **kwargs):`
  - The function should return the new `_id`.

---

### 10. Change school topics
**Filename**: `10-update_topics.py`

**Description**:
  - Write a Python function that changes all topics of a school document based on the name.
  - Prototype: `def update_topics(mongo_collection, name, topics):`

---

### 11. Where can I learn Python?
**Filename**: `11-schools_by_topic.py`

**Description**:
  - Write a Python function that returns the list of schools having a specific topic.
  - Prototype: `def schools_by_topic(mongo_collection, topic):`

---

### 12. Log stats
**Filename**: `12-log_stats.py`

**Description**:
  - Write a Python script that provides some stats about Nginx logs stored in MongoDB.
  - Database: `logs`, Collection: `nginx`
  - The script should display the number of logs, and count the number of logs by methods such as GET, POST, PUT, PATCH, DELETE.
