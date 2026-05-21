from inspect_ai.dataset import Sample

number_in_amenities_samples = [
    Sample(
        input="""
"property_id": 1,
    "property_name": "Sunny Central Apartment",
    "property_type": "NormalApartment",
    "description": {
        "name": "Sunny Central Apartment",
        "headline": "Bright apartment near the city center",
        "description": "<p>A cozy apartment with natural light and easy access to restaurants.</p>",
    },
    "amenities": [
        "DishWasher type 54237483",
        "InternetBroadband",
        "BathroomAndLaundry",
    ],
    "image_urls": [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
    ],
    "reviews": [
        "Great location and very clean.",
        "The apartment was comfortable and close to everything.",
    ],
    "num_of_reviews": 2,
    "average_review_score": 4.8,
    "rental_info": {
        "max_guests": 4,
        "bedrooms": 2,
        "bathrooms": 1,
    },
    "location": {
        "city": "Barcelona",
        "country": "Spain",
        "latitude": 41.3874,
        "longitude": 2.1686,
    },
    "policies": {
        "cancellation_policy": "Free cancellation up to 7 days before arrival",
        "payment_schedule": "Pay 30% now and the rest before arrival",
        "damage_deposit": "€200",
    },
    "house_rules": {
        "check_in_time": "3 PM",
        "check_out_time": "11 AM",
    },
}
"""     ,
        target="The listing must not contain phone numbers."
    )
]
