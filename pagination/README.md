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
The function `index_range` takes two integer arguments: `page` and `page_size`. The function returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters. Page numbers are 1-indexed, i.e., the first page is page 1.

---

### 1. Simple Pagination
**Filename**: `1-simple_pagination.py`

**Description**:
The `Server` class was extended to implement a method named `get_page`. This method took two integer arguments: `page`, which had a default value of 1, and `page_size`, with a default value of 10. The method utilized the `index_range` function to find the correct indexes and paginated the dataset accordingly. It returned the appropriate page of the dataset and asserted that both arguments were integers greater than 0. If the input arguments were out of range for the dataset, it returned an empty list.

---

### 2. Hypermedia Pagination
**Filename**: `2-hypermedia_pagination.py`

**Description**:
The `Server` class was modified to include a method named `get_hyper`, which took the same arguments as `get_page`. This method returned a dictionary with keys for `page_size`, `page`, `data`, `next_page`, `prev_page`, and `total_pages`. This dictionary provided hypermedia pagination information, including the current, next, and previous pages, as well as the total number of pages. The `get_page` method was reused in this method's implementation.

---

### 3. Deletion-Resilient Hypermedia Pagination
**Filename**: `3-hypermedia_del_pagination.py`

**Description**:
The `Server` class was further modified to add a `get_hyper_index` method. This method accepted two integer parameters: `index`, with a default value of `None`, and `page_size`, with a default value of 10. The method was designed to be deletion-resilient, handling cases where rows were deleted between two queries. 

The method returned a dictionary containing the following keys:
- `index`: The current start index of the returned page.
- `next_index`: The index for the next query.
- `page_size`: The size of the page.
- `data`: The actual page of the dataset.

#### Requirements/Behavior
- `assert` was used to verify that the index was in a valid range.
- If rows were deleted between two queries, the method still returned the correct data page.
- For instance, querying index 0 with `page_size` 10 returned rows indexed 0 to 9. If a subsequent query was made with index 10 but rows 3, 6, and 7 had been deleted, rows indexed 10 to 19 were still returned.

---

