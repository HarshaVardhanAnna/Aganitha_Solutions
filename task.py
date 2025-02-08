import pandas as pd
from transformers import pipeline

# Load the dataset (Replace with the actual path to your dataset)
file_path = "/Users/HARSHA VARDHAN/OneDrive/Documents/python/sample_customer_support_tickets.csv"
df_real_tickets = pd.read_csv(file_path)

# Check if 'Customer_Message' column exists
if "Customer_Message" not in df_real_tickets.columns:
    raise ValueError("Dataset must contain a 'Customer_Message' column.")

# Load the zero-shot classification model
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",  # Switch to a more robust and supported model
    framework="pt"  # Use PyTorch
)

# Define categories and urgency levels
categories = ["Billing Issue", "Technical Support", "Product Inquiry", "Cancellation Request", "Delivery Issue"]
urgency_levels = ["Low", "Medium", "High", "Critical"]

# Function to classify tickets in batches with progress logging
def classify_tickets_batch(ticket_texts, candidate_labels):
    results = []
    for i in range(0, len(ticket_texts), 8):  # Process in batches of 8
        batch = ticket_texts[i:i+8]
        batch_result = classifier(batch, candidate_labels=candidate_labels)
        results.extend([res["labels"][0] for res in batch_result])
        print(f"Processed batch {i // 8 + 1} / {len(ticket_texts) // 8 + 1}")
    return results

# Classify ticket categories
df_real_tickets["Predicted_Category"] = classify_tickets_batch(
    df_real_tickets["Customer_Message"].tolist(), categories
)

# Classify ticket urgency levels
df_real_tickets["Predicted_Urgency"] = classify_tickets_batch(
    df_real_tickets["Customer_Message"].tolist(), urgency_levels
)

# Save the updated dataset to a CSV file
output_file = "classified_customer_tickets.csv"
df_real_tickets.to_csv(output_file, index=False)

# Display the first few rows of the classified dataset
print("Classification Completed. Preview:")
print(df_real_tickets.head())

# Notify about the saved file
print(f"Classified dataset saved as '{output_file}'.")
