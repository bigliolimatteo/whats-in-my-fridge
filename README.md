# What's in my fridge - Stop wasting your food!

## Description

**What's in my fridge** is a Python-based application designed to help people reduce their food waste by providing personalized recipe suggestions based on the expiration of the food they have at home. The app allows users to scan or manually enter the food items they bought, including the quantity and expiration date. The algorithm then analyzes this information to suggest recipes for breakfast, lunch, and dinner that optimize the usage of expiring food, ensuring that no food goes to waste.

The goal is to make it easier for individuals to prepare delicious meals while minimizing the environmental impact caused by food waste.

## Technologies Used

- **Programming Language**: Python, Javascript
- **Data Storage**: Still to decide
  
## How It Works

1. **Food Input**: 
   - You can either scan the barcode of your food items using your phone’s camera or manually input details such as the type of food, quantity, and expiration date.
   
2. **Food Tracking**:
   - The app stores all food data in a database, which is regularly updated.

3. **Expiration Date Algorithm**:
   - The algorithm checks the expiration date of the food items daily and flags those that are close to expiring.

4. **Recipe Recommendations**:
   - Based on the food items that are about to expire, the app suggests breakfast, lunch, and dinner recipes that incorporate these ingredients, helping users utilize the food before it goes to waste.
   The recipes can be personalized by food preferences, type of diet (vegan, vegetarian, etc) and allergies. 

## Ideal Additional Features 

- **Image Recognition**: Scan barcodes instead of manually entering the food type, quantity, and expiration date. 

- **Food Shopping Reminder**: The application sends an alert when you are about to finish a frequent consumed product. 

- **Shopping List Memo**: An algorithm that optimses the list with the food to purchase in order to minimizes the necessary times to go food shopping. 

- **User Interface**: A user-friendly application with an intuitive user interface. 

## Installation 

git clone git@github.com:bigliolimatteo/whats-in-my-fridge.git