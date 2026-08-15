# Python

Personal Python learning code and projects, organized by topic.

## Structure

| Folder | Contents |
|---|---|
| `01_basics/` | Core Python: control flow, functions, OOP, file handling, small console programs (ATM machine, calculator, dice roll, pyramids), plus a lambda/map/filter notebook |
| `02_numpy/` | NumPy fundamentals — array creation, reshaping, aggregation, comparison, slicing |
| `03_visualization/` | Plotting code. `matplotlib/` covers bar charts, scatter plots, subplots and insets (both pyplot and OOP styles); `seaborn/` covers statistical plots on built-in datasets |
| `04_machine_learning/` | `classification_notebooks/` — decision tree / logistic regression / KNN work on the kyphosis, loan, SUV and titanic datasets (CSVs live alongside their notebooks). `svm/` — SVM on the iris dataset |
| `05_projects/` | End-to-end projects. `customer_segmentation/` — KMeans clustering notebook plus a Streamlit/Gradio app and pickled model + scaler. `gradio_demo/` — Gradio interface experiments |

## Notes

- Notebooks load their CSVs by bare filename, so data files are kept in the same folder as the notebook that uses them.
- `.pkl` files in `05_projects/customer_segmentation/` are trained artifacts produced by `analysis_model.ipynb`.
- Files and folders use `snake_case`; top-level folders are numbered roughly in order of increasing complexity.
