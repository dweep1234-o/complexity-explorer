# 🔍 Algorithm Complexity Explorer

An interactive Python-based application that explores and compares the time complexity of different sorting and searching algorithms. The project measures the number of operations performed on different input sizes and compares the observed growth with theoretical Big-O complexity.

## 📌 Project Overview

Algorithm Complexity Explorer helps users understand how algorithms perform as the input size increases.

Instead of relying only on theoretical time complexity, this application benchmarks algorithms using different input patterns, measures their operations, and visualizes their empirical growth against predicted complexity classes.

## ✨ Features

- **Multiple Algorithms:** Compare Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Linear Search, and Binary Search.
- **Different Input Patterns:** Test algorithms with random, sorted, reversed, nearly sorted, and duplicate-heavy data.
- **Performance Benchmarking:** Measure the number of operations performed for different input sizes.
- **Growth Rate Analysis:** Calculate empirical growth rates using log-log regression.
- **Big-O Comparison:** Compare measured performance against theoretical complexity classes.
- **Interactive Visualization:** Display performance graphs and comparison tables through Streamlit.
- **Multiple Trials:** Run benchmarks multiple times to calculate average results.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Streamlit

## 📂 Project Structure

```text
complexity-explorer/
│
├── app.py              # Streamlit application interface
├── algorithms.py       # Sorting and searching algorithms
├── bench.py            # Benchmarking and growth-rate calculations
├── inputs.py           # Input data generation
├── plot.py             # Performance visualization
├── theory.py           # Theoretical Big-O predictions
│
├── test_sorts.py       # Sorting algorithm tests
├── test_bench.py       # Benchmarking tests
├── test_inputs.py      # Input generation tests
├── test_plot.py        # Visualization tests
├── test_theory.py      # Complexity prediction tests
├── test_bubble.py      # Bubble sort test
│
├── test_plot.png       # Sample performance graph
├── report.md           # Project report
└── README.md
```

## ⚙️ Algorithms Implemented

| Algorithm | Average Time Complexity | Worst Time Complexity |
|---|---|---|
| Bubble Sort | O(n²) | O(n²) |
| Insertion Sort | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) |
| Linear Search | O(n) | O(n) |
| Binary Search | O(log n) | O(log n) |

*Note: Actual performance also depends on the input pattern and algorithm implementation.*

## 📊 Input Patterns

The application supports five different input patterns:

1. **Random:** Randomly generated values.
2. **Sorted:** Elements arranged in ascending order.
3. **Reversed:** Elements arranged in descending order.
4. **Nearly Sorted:** Almost sorted data with a few swapped elements.
5. **Duplicates:** Data containing repeated values.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/complexity-explorer.git
```

### 2. Navigate to the project directory

```bash
cd complexity-explorer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Mac/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install numpy pandas matplotlib streamlit
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📈 How to Use

1. Launch the application.
2. Select the sorting or searching algorithms from the sidebar.
3. Choose an input pattern.
4. Set the maximum input size.
5. Select the number of benchmark trials.
6. Click **Run Benchmark**.
7. View the performance graph and comparison table.

## 🧪 Testing

Run individual test files using Python:

```bash
python test_sorts.py
python test_bench.py
python test_inputs.py
python test_plot.py
python test_theory.py
python test_bubble.py
```

## 🎯 Project Objective

The primary objective of this project is to bridge the gap between theoretical algorithm analysis and practical performance measurement.

By comparing actual operation counts with theoretical Big-O growth rates, users can better understand algorithm efficiency, scalability, and the impact of different input distributions.

