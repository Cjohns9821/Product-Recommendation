# ================================
# PRODUCT RECOMMENDATION ENGINE
# ================================

products = [
    {"name": "Eco Water Bottle", "tags": ["eco-friendly", "durable", "recyclable"]},
    {"name": "Trail Backpack", "tags": ["durable", "water-resistant", "lightweight"]},
    {"name": "Vegan Leather Wallet", "tags": ["vegan", "stylish", "compact"]},
    {"name": "Bamboo Toothbrush", "tags": ["eco-friendly", "vegan", "biodegradable"]},
    {"name": "Smartwatch", "tags": ["tech", "durable", "stylish"]},
]

# Step 2: Explore product data
print("First few products in the catalog:")
for p in products[:3]:
    print(p)

# Step 3: Collect customer preferences
customer_preferences = []

while True:
    pref = input("Input a preference: ")
    customer_preferences.append(pref)

    again = input("Do you want to add another preference? (Y/N): ")
    if again.upper() == "N":
        break

# Step 4: Convert lists to sets
customer_preferences = set(customer_preferences)

products_with_sets = []
for p in products:
    products_with_sets.append({
        "name": p["name"],
        "tags": set(p["tags"])
    })

# Step 5: Count matching tags
def count_matches(product_tags, customer_preferences):
    return len(product_tags.intersection(customer_preferences))

# Step 6: Build recommendation function
def recommend_products(products, customer_preferences):
    results = []
    for p in products:
        matches = count_matches(p["tags"], customer_preferences)
        results.append((p["name"], matches))
    return results

# Run recommendation engine
recommendations = recommend_products(products_with_sets, customer_preferences)

# Print results
print("\nRecommended Products:")
for name, score in recommendations:
    print(f"- {name} ({score} match(es))")


# ================================
# DESIGN MEMO (200–300 words)
# ================================
"""
Design Memo

For this recommendation engine, I relied on core Python operations including loops,
lists, sets, and intersections. The customer preferences begin as a list because
lists are ideal for collecting input dynamically. Once the user finishes entering
preferences, I convert the list into a set. Sets remove duplicates automatically
and make comparisons faster, which is important when matching tags.

Each product’s tags are also converted into sets. This allows me to use the
intersection operation, which quickly identifies shared values between the
customer’s preferences and the product’s attributes. The function count_matches()
returns the number of overlapping tags, which becomes the score for each product.

The recommend_products() function loops through all products, computes the match
score, and stores the results in a list of tuples. This structure is simple,
lightweight, and easy to print. The final output shows each product along with
how many tags matched the customer’s preferences.

If this system had 1,000+ products, the logic would still work, but performance
would matter more. Using sets is already a good optimization because intersections
are fast. For larger systems, I might sort the results by match score, filter out
products with zero matches, or store products in a database instead of a list.
Overall, this design balances simplicity with efficiency and mirrors the basic
logic used in real-world recommendation engines. Come to think of it a filter by type would be best.
"""
