import pandas as pd

import os

# Define the file path
# Create a simulated dataset of 100 customer support tickets
data = {
    "Ticket_ID": range(1, 101),
    "Customer_Message": [
        "My credit card was charged twice, and I need a refund immediately.",
        "The mobile app keeps crashing whenever I try to log in.",
        "Can you provide more details about your subscription plans?",
        "I want to cancel my membership. Please let me know the process.",
        "My order is delayed. It was supposed to arrive last week.",
        "The internet connection is too slow; I can't work like this.",
        "I need help updating my billing information.",
        "Can you explain the additional charges on my last invoice?",
        "I want to upgrade my account to the premium plan.",
        "The router is not connecting to the internet after restarting.",
        "I have not received the refund I was promised last week.",
        "Can I speak with a support representative?",
        "Please assist me in cancelling my current plan and switching to a new one.",
        "My delivery was damaged when it arrived.",
        "I am unable to reset my account password; the link is broken.",
        "Why was my card charged even though I didn't make a purchase?",
        "Can you fix the issue with my account showing incorrect details?",
        "I need assistance setting up my new internet connection.",
        "My subscription got cancelled, but I want to reactivate it.",
        "The app is not displaying my recent transactions correctly.",
        # Adding more varied examples
        *[f"This is a simulated customer message number {i}" for i in range(21, 101)]
    ]
}

# Convert to DataFrame
df_sample_tickets = pd.DataFrame(data)

# Save to a CSV file for the user
file_path = "sample_customer_support_tickets.csv"  # Save in the current working directory or specify an existing folder

# Save the dataset to CSV
df_sample_tickets.to_csv(file_path, index=False)

print(f"Dataset successfully saved to: {os.path.abspath(file_path)}")

import ace_tools as tools; tools.display_dataframe_to_user(name="Sample Customer Support Tickets", dataframe=df_sample_tickets)
