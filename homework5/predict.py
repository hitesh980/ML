import pickle

# Load the trained pipeline
with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

# Client record to score
client = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Predict probability
probability = model.predict_proba([client])[0, 1]
print(probability)
