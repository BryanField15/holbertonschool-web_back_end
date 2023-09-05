## What I've Learned

### How to paginate a dataset with simple page and page_size parameters
I've learned how to take a large dataset and split it into smaller, more manageable pieces using the `page` and `page_size` parameters. Now, I know how to efficiently fetch smaller sets of data while navigating through the entire dataset.

### How to paginate a dataset with hypermedia metadata
I've applied the concept of hypermedia pagination, where I not only return the data but also metadata like the current page, next page, and previous page. This helps anyone consuming the API to understand how to navigate through the paginated data effectively.

### How to paginate in a deletion-resilient manner
I've gained valuable insights into handling some of the challenges that come with pagination, specifically when rows get deleted from a dataset. Now, I know how to ensure that the pagination remains reliable and consistent, even when the data is changing.

---

### 0. Simple Helper Function
**Filename**: `0-simple_helper_function.py`

**Description**: 
Write a function named `index_range` that takes two integer arguments: `page` and `page_size`. The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters. Page numbers are 1-indexed, i.e., the first page is page 1.

---

### 1. Simple Pagination
**Filename**: `1-simple_pagination.py`

**Description**:  
Extend the `Server` class to implement a method named `get_page`. This method takes two integer arguments: `page` with a default value of 1, and `page_size` with a default value of 10. Utilize the `index_range` function to find the correct indexes and paginate the dataset. The method should return the appropriate page of the dataset, and assert that both arguments are integers greater than 0. If the input arguments are out of range for the dataset, return an empty list.


---

### 2. Hypermedia Pagination
**Filename**: `2-hypermedia_pagination.py`

**Description**:  
Modify the `Server` class to include a method named `get_hyper` that takes the same arguments as `get_page`. This method should return a dictionary with keys for `page_size`, `page`, `data`, `next_page`, `prev_page`, and `total_pages`. The dictionary should provide hypermedia pagination information about the dataset, including the current page, next and previous pages, and total number of pages. Ensure that `get_page` is reused in this method's implementation.


---

### 3. Deletion-Resilient Hypermedia Pagination
**Filename**: `3-hypermedia_del_pagination.py`

**Description**:  
Modify the `Server` class to add a `get_hyper_index` method that accepts two integer parameters: `index` with a default value of `None`, and `page_size` with a default value of 10. This method should be deletion-resilient, meaning that it should handle cases where rows are deleted between two queries.

The method should return a dictionary with the following keys:
- `index`: The current start index of the returned page.
- `next_index`: The index for the next query.
- `page_size`: The size of the page.
- `data`: The actual page of the dataset.

**Requirements/Behavior**:  
- Use `assert` to verify that the index is in a valid range.
- If rows are deleted between two queries, the method should still return the correct data page.
- For example, if the user queries index 0, page_size 10, they will get rows indexed 0 to 9. If they then query index 10, but rows 3, 6, and 7 were deleted, they should still get rows indexed 10 to 19.

---

