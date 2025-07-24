# Course Review Analyser

A Python-based tool for analyzing and extracting insights from course reviews using data science and machine learning techniques. This project processes course review data, performs sentiment analysis, and helps educators and learners assess course quality effectively.

## Features

- **Data Cleaning & Preprocessing:** Efficient handling and cleaning of raw review datasets.
- **Sentiment Analysis:** Uses a trained machine learning model to classify review sentiments as positive, negative, or neutral.
- **Interactive Jupyter Notebook:** Step-by-step exploration, feature engineering, and model training.
- **Reusable Components:** Python scripts for running predictions (`app.py`) and model/vectorizer pickle files for quick inference.
- **CSV Integration:** Supports importing/exporting review and course data via CSV files.

## Project Structure

| File/Folder                       | Description                                                  |
|---------------------------------|--------------------------------------------------------------|
| `Course_Review_Analyser.ipynb`  | Main notebook for data analysis, feature engineering, and model training |
| `app.py`                        | Python script for running sentiment predictions and workflows |
| `coursea_data.csv`              | Contains course metadata and features                         |
| `Coursera_courses.csv`          | Dataset containing Coursera course details                    |
| `reviews.csv`                   | CSV file with raw or preprocessed course reviews             |
| `sentiment_model.pkl`           | Serialized trained sentiment analysis model                   |
| `vectorizer.pkl`                | Serialized text vectorizer (e.g., TF-IDF)                     |
| `.ipynb_checkpoints/`           | Jupyter notebook autosave checkpoints (can be ignored or added to `.gitignore`) |

## Installation & Setup

It is recommended to create a Python virtual environment or use Anaconda




- Follow the notebook to explore data, preprocess, train models, and visualize results.



- Use this script to perform sentiment analysis predictions on new reviews or batches.

## How to Contribute

Contributions, bug fixes, and feature requests are very welcome!

1. Fork this repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a Pull Request

## Notes

- Consider adding a `.gitignore` file to exclude large datasets, model checkpoints, or personal files.
- Handle cross-platform line-ending issues by configuring `.gitattributes` or `core.autocrlf` in Git.
- This project currently uses static CSV files; future updates might integrate APIs or databases.


## Contact

- **GitHub:** [unbeatable951/Course_Review_Analyser](https://github.com/unbeatable951/Course_Review_Analyser)
---









