# Late Night Show API

Welcome to the Late Night Show API! This Flask-based project manages episodes of a late-night TV show, its guests, and the appearances they make. It models the relationships between episodes, guests, and their ratings using SQLAlchemy and exposes RESTful endpoints for interaction.

#### By **Ian Dan Cheruiyot**

## Project Overview

This API simulates a late-night talk show, where each episode can have multiple guests, and each guest can appear in multiple episodes. Guests are rated based on their appearances.

### Entities:

- **Episode** – A talk show episode with a date and episode number.
- **Guest** – A celebrity who appears on the show, with a name and occupation.
- **Appearance** – A join table representing a guest’s appearance on an episode, with a rating from 1–5.

## Features

- Full CRUD for `Episodes` and `Guests`
- Custom POST for creating `Appearances` with validations
- Seed script to populate data from a CSV
- Clean RESTful architecture
- Database migrations using Flask-Migrate

## API Endpoints

### `GET /episodes`

Fetch all episodes with their dates and IDs.

### `GET /episodes/<id>`

Fetch a specific episode by ID, including all appearances and guest ratings.

### `GET /guests`

List all guests with names and occupations.

### `POST /appearances`

Create a new appearance for a guest on an episode.

```json
{
  "episode_id": 1,
  "guest_id": 3,
  "rating": 5
}
```

## Setup Instructions

### Prerequisites

- Python 3.12+
- Pipenv installed

### Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com:IanDanCheruiyot/lateshow.git
   cd late-show-compulsory
   ```

2. **Install Dependencies**

   ```bash
   pipenv install
   pipenv shell
   ```

3. **Run Migrations**

   Navigate into the `server` directory and set up the database.

   ```bash
   cd server
   flask db upgrade
   ```

4. **Seed the Database from CSV**

   ```bash
   python seed.py
   ```

## Running the Application

Run the Flask development server:

```bash
python app.py
```

Or using the Flask CLI:

```bash
flask run
```

Access the API at `http://127.0.0.1:5555`.

## Debugging

Use the `debug.py` script to enter an interactive shell:

```bash
python debug.py
```

This lets you inspect your database and models using `ipdb`.

## Technologies Used

- Flask
- Flask-RESTful
- Flask-Migrate
- SQLAlchemy
- SQLite
- Faker (for seed data)
- CSV (as seed input)

## Support & Contact

For any issues or questions, please contact **[ian.cheruiyot1@student.moringaschool.com]**.

## License

This project is licensed under the MIT License.