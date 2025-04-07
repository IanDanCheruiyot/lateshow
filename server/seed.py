import csv
from datetime import datetime
from app import app
from models import Appearance, Episode, Guest, db

def seed_from_csv():
    print("Resetting database...")
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()
    db.session.commit()

    print("Reading from file.csv...")
    guests_dict = {}
    episodes_dict = {}
    appearances_added = 0

    with open("file.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            guest_name = row["Raw_Guest_List"].strip()
            occupation = row["GoogleKnowlege_Occupation"].strip()
            show_date_str = row["Show"].strip()

            # Convert to datetime format
            try:
                date_obj = datetime.strptime(show_date_str, "%m/%d/%y")
            except ValueError:
                print(f"Skipping invalid date: {show_date_str}")
                continue

            date_formatted = date_obj.strftime("%m/%d/%y")

            # Create guest if not exists
            if guest_name not in guests_dict:
                guest = Guest(name=guest_name, occupation=occupation)
                db.session.add(guest)
                db.session.flush()  # get guest.id
                guests_dict[guest_name] = guest
            else:
                guest = guests_dict[guest_name]

            # Create episode if not exists
            if date_formatted not in episodes_dict:
                episode = Episode(date=date_formatted, number=len(episodes_dict))
                db.session.add(episode)
                db.session.flush()  # get episode.id
                episodes_dict[date_formatted] = episode
            else:
                episode = episodes_dict[date_formatted]

            # Create appearance
            appearance = Appearance(guest_id=guest.id, episode_id=episode.id, rating=5)
            db.session.add(appearance)
            appearances_added += 1

    db.session.commit()
    print(f"Seeded {len(guests_dict)} guests, {len(episodes_dict)} episodes, {appearances_added} appearances.")

if __name__ == "__main__":
    with app.app_context():
        seed_from_csv()
        print("Database seeded successfully from CSV!")