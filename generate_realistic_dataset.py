import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


# ==============================
# CONFIG
# ==============================

START_DATE = "2024-01-01"
DAYS = 365

vaccines = [
    ("Covishield", "Serum Institute"),
    ("Covaxin", "Bharat Biotech"),
    ("Sputnik V", "Dr. Reddy's"),
    ("Pfizer", "Pfizer India"),
    ("Moderna", "Moderna India")
]

locations = [
    "Kerala",
    "Tamil Nadu",
    "Karnataka",
    "Maharashtra",
    "Delhi"
]


# ==============================
# GENERATE DATA
# ==============================

def generate_dataset():

    data = []
    start = datetime.strptime(START_DATE, "%Y-%m-%d")

    for vaccine, manufacturer in vaccines:

        base_demand = random.randint(150, 250)
        trend_factor = random.uniform(0.05, 0.15)

        for day in range(DAYS):

            current_date = start + timedelta(days=day)

            # Trend (slow increase)
            trend = day * trend_factor

            # Weekly seasonality
            weekly = 20 * np.sin(2 * np.pi * day / 7)

            # Monthly seasonality
            monthly = 30 * np.sin(2 * np.pi * day / 30)

            # Random noise
            noise = np.random.normal(0, 10)

            demand = base_demand + trend + weekly + monthly + noise
            demand = max(50, int(demand))

            supply = int(demand + random.randint(-20, 30))
            stock = max(0, supply - random.randint(0, 50))

            location = random.choice(locations)

            batch_id = f"{vaccine[:3].upper()}-{day:03d}"

            data.append([
                current_date.strftime("%Y-%m-%d"),
                vaccine,
                batch_id,
                manufacturer,
                location,
                demand,
                supply,
                stock
            ])

    columns = [
        "date",
        "vaccine_name",
        "batch_id",
        "manufacturer",
        "location",
        "demand",
        "supply",
        "stock"
    ]

    df = pd.DataFrame(data, columns=columns)

    df.to_csv("data/vaccine_demand.csv", index=False)

    print("✅ Realistic dataset generated successfully!")


if __name__ == "__main__":
    generate_dataset()