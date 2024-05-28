# Football Goals Prediction Model

## Overview

This project focuses on building a predictive model to forecast the number of goals scored by each team in a football match. The model incorporates various data sources, including player ratings and team information, to create a robust prediction system. The process involves data collection, preprocessing, feature engineering, exploratory data analysis (EDA), model training, and deployment.

## Table of Contents

1. [Data Collection](#data-collection)
2. [Preprocessing](#preprocessing)
3. [Data Cleaning](#data-cleaning)
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
5. [Model Training](#model-training)
6. [API Development with Flask](#api-development-with-flask)
7. [Dockerization](#dockerization)
8. [Deployment on Azure](#deployment-on-azure)

## Data Collection

### Source
Data was collected using Scrapy from [Transfermarkt](https://www.transfermarkt.com/).

### Datasets
The following datasets were collected:
- `clubs_team_players_v1.json`
- `national_team_players_v1.json`
- `matches_v1.json`
- `players_rating_v1.csv`

## Preprocessing

### Summary
The preprocessing stage involves reading the collected data, normalizing team and player names, and mapping players to their respective teams. This step ensures consistency and prepares the data for further analysis.

### Flow Chart
```mermaid
graph TD;
    A[Load Data] --> B[Normalize Team Names]
    B --> C[Normalize Player Names]
    C --> D[Fix Player List]
    D --> E[Map Players to Teams]
    E --> F[Assign Players to Matches]
    F --> G[Normalize Player Names in Matches]
    G --> H[Assign Player Ratings]
```

# Data Cleaning Strategy
The data cleaning stage involves handling missing values and ensuring the integrity of the data. This includes:

- Handling missing values by imputing the mean rating for missing player ratings.
- Ensuring all necessary fields are populated and correctly formatted.

# Exploratory Data Analysis (EDA)

| Top 10 Teams with the Most Players | Number of Home vs. Away Players |
|:---------------------------------:|:------------------------------:|
| ![Top 10 Teams with the Most Players](file-7Bh7sJdcttJ2tTmg0dIkcHLc) | ![Number of Home vs. Away Players](file-EEjJ4J1CwsmawoNFbYmsC9Od) |

| Top 10 Players by Frequency of Appearances | Distribution of Home Team Scores |
|:-----------------------------------------:|:---------------------------------:|
| ![Top 10 Players by Frequency of Appearances](file-H38aSSPCMpTM7av1jEGbGFES) | ![Distribution of Home Team Scores](file-fUJLmbdXgBoEkzkaer9Yr6lA) |

| Distribution of Away Team Scores | Distribution of Home Team Average Ratings |
|:-------------------------------:|:------------------------------------------:|
| ![Distribution of Away Team Scores](file-VnmpXlimdLcPLuIED55Z5K6F) | ![Distribution of Home Team Average Ratings](file-1LfOP0jk1JrspsVTZd4xErVs) |

| Home Team Score vs. Home Team Average Rating | Away Team Score vs. Away Team Average Rating |
|:-------------------------------------------:|:-------------------------------------------:|
| ![Home Team Score vs. Home Team Average Rating](file-USd36aqgS72AjymTO4eVhwjh) | ![Away Team Score vs. Away Team Average Rating](file-1LfOP0jk1JrspsVTZd4xErVs) |

# Model Training
The model training stage involves splitting the data into training and testing sets, selecting a model, and optimizing its hyperparameters.

## Summary
- The dataset is split into training and testing sets.
- A `RandomForestRegressor` is used for prediction.
- Hyperparameters are optimized using `RandomizedSearchCV`.

# API Development with Flask
An API is developed using Flask to serve the model predictions. The API allows users to input match details and receive predicted scores.

# Dockerization
The application is containerized using Docker to ensure consistency across different environments. A Dockerfile is created to define the environment and dependencies.

# Deployment on Azure
The Docker container is deployed on Azure, making the model accessible as a web service. Azure provides scalability and reliability for the deployed model.

