# East Africa Countries GDP Tracker

This CLI application allows users to track the GDP of East African countries based on their sources of revenue and consequently gauge the economic performance of the countries.The app allows users to interact with a database to retrieve GDP data, economic rankings, and add or delete revenue sources all through a user-friendly command-line interface.

## Features

- **Obtain a country's economic ranking** based on GDP.
- **Get a country's GDP** by inputting its name.
- **Retrieve all sources of revenue** for a country.
- **Add a revenue source** with its generated revenue.
- **Delete a revenue source**.
- **Graceful Error Handling**: The app provides meaningful error messages in case of invalid input or database issues.

## Technologies Used

- Python
- SQLAlchemy (for ORM)
- Alembic (for migrations)
- Click (for CLI)

## Database Tables

The app uses the following tables:

1. **Revenue Sources**: Stores information about East African countries' sources of revenue and the generated revenue in KSH.
2. **GDPs**: Stores the calculated GDP values based on revenues for each country.
3. **Economic Rankings**: Stores the rankings of countries' economic power based on their GDP.

## Installation

To install and set up the project, follow these steps:

- Fork then clone the repository:
      `git clone git@github.com:Visionnaire1000/East-Africa-Countries-GDP-Tracker.git`
- Navigate to the local repo:
      `cd East-Africa-Countries-GDP-Tracker`
- Create then activate virtual environment:
      `Python3 -m venv venv`
      `Source venv/bin/activate`
- Install the dependencies:
       `pip install -r requirements.txt`
- Set up the database using Alembic Migrations:
       `alembic upgrade head`
- Seed the RevenueSources Table:
       `python3 lib/database/seed.py`
- Run main.py file to access the cli:
       `python3 main.py`

## Usage

- After running main.py file,you'll see an interactive menu,particularly numbered choices which are all the functionalities of the cli app.
- Input the first number,you'll then receive further input prompts which are well detailed to enable you easily 
interact with the app.
- Continue to interact with the menu to test all functionalities,and once you are done you'll input the last number to exit the cli.
- The app provides meaningful error messages in case of invalid input or database issues.