
# 🐼 Pandas Course

This folder contains all exercises for the pandas course.
Learning pandas step by step with practical examples.

---

## 📚 Topics Covered

* **Day 1:** DataFrame basics
* **Day 2:** Selection & filtering
* **Day 3:** Basic statistics (sum, mean, std) in pandas
* **Day 4:** Add new column to data frame
* **Day 5:** Apply function to column, `.info()`, `.describe()` & `.describe(all)`
* **Day 6:** Swap to Jupyter Notebook
* **Day 7:** String operations in Pandas (`str.strip()`, `lower()`, `upper()`, `contains`)
* **Day 8:** Filtering & conditions in Pandas (>, >=, ==, &, |, isin, sort_values)
* **Day 9:** GroupBy & aggregation (groupby, mean, sum, count, agg, reset_index)
* **Day 10:** Handling Missing Data & Statistics

- Learned how to handle missing values using `dropna()` and `fillna()`
- Understood the difference between row-wise and column-wise operations using `axis`
- Filled missing numeric values using column means

⚠️ Important Note:
When using statistical functions like `mean()`, `sum()`, or `std()` in pandas,
always specify `numeric_only=True` if the DataFrame contains non-numeric (string) columns.

Example:
```python
clean_df = df.fillna(df.mean(numeric_only=True))
clean_df.mean(numeric_only=True)
---