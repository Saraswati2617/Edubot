import pandas as pd

# Synthetic dataset
data = {
    "input_text": [
        "I enjoy coding and developing software",
        "I like solving biological problems",
        "I love creating art and painting",
        "I am good at analyzing data and research",
        "I want to work in government and politics",
        "I enjoy managing finances and accounting",
        "I like building machines and working on AI",
        "I am passionate about writing stories",
        "I want to explore fashion design",
        "I like business and sales"
    ],
    "field": [
        "Engineering",
        "Medical",
        "Arts",
        "Science",
        "Politics",
        "Commerce",
        "Engineering",
        "Arts",
        "Arts",
        "Commerce"
    ]
}

# Save dataset to CSV
df = pd.DataFrame(data)
df.to_csv("data/dataset.csv", index=False)
print("Dataset saved!")
