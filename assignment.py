import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/PratikPhysics/SNDT-College/refs/heads/main/car_price_dataset.csv")
print(df)
#1. What is the average price of all cars in the dataset? 
print(f"The average price of all cars in the dataset is ${round(df['Price'].mean(),2)}")

#2. Which car brand has the highest average price? 
Brand=df[df['Price']==df['Price'].max()]['Brand'][1100]
print(f"The brand with the highest price is {Brand}")

#3.What is the most common fuel type in the dataset? 
common_fuel_type=df['Fuel_Type'].mode()[0]
print(f"The most common fuel type in the dataset is {common_fuel_type}")

#4.How many cars have a mileage greater than 200,000? 
cars_with_high_mileage = df[df['Mileage'] > 200000]
print(f"The number of cars with a mileage greater than 200,000 is {len(cars_with_high_mileage)}")

#5.What is the distribution of cars by transmission type? 
transmission_distribution = df['Transmission'].value_counts()
print(f"The distribution of cars by transmission type is:\n{transmission_distribution}")

#5.Which car model has the highest price? 
highest_price_model = df[df['Price'] == df['Price'].max()]['Model'].iloc[0]
print(f"The car model with the highest price is {highest_price_model}")

#6.What is the average price of cars by fuel type? 
average_price_by_fuel_type = df.groupby('Fuel_Type')['Price'].mean()
print(f"The average price of cars by fuel type is:\n{average_price_by_fuel_type}")

#7.What is the average price of cars by fuel type? 
average_price_by_fuel_type = df.groupby('Fuel_Type')['Price'].mean()
print(f"The average price of cars by fuel type is:\n{average_price_by_fuel_type}")

#8.How many cars are from the year 2020 or later? 
cars_from_2020_or_later = df[df['Year'] >= 2020]
print(f"The number of cars from the year 2020 or later is {len(cars_from_2020_or_later)}")

#9.What is the average engine size for each brand? 
average_engine_size_by_brand = df.groupby('Brand')['Engine_Size'].mean()
print(f"The average engine size for each brand is:\n{average_engine_size_by_brand}")

#10.Which car has the lowest mileage? 
lowest_mileage_car = df[df['Mileage'] == df['Mileage'].min()]['Model'].iloc[0]
print(f"The car with the lowest mileage is {lowest_mileage_car}")

#11.What is the correlation between mileage and price? 
correlation_mileage_price = df['Mileage'].corr(df['Price'])
print(f"The correlation between mileage and price is {correlation_mileage_price}")

#12. How many cars have more than 2 owners? 
cars_with_more_than_2_owners = df[df['Owner_Count'] > 2]
print(f"The number of cars with more than 2 owners is {len(cars_with_more_than_2_owners)}")

#13.What is the average price of cars by year? 
average_price_by_year = df.groupby('Year')['Price'].mean()
print(f"The average price of cars by year is:\n{average_price_by_year}")

#14.Which car has the highest number of doors? 
highest_doors_car = df[df['Doors'] == df['Doors'].max()]['Model'].iloc[0]
print(f"The car with the highest number of doors is {highest_doors_car}")

#15. What is the average mileage for each fuel type? 
average_mileage_by_fuel_type = df.groupby('Fuel_Type')['Mileage'].mean()
print(f"The average mileage for each fuel type is:\n{average_mileage_by_fuel_type}")

#16. How many cars are from the brand 'Toyota'? 
toyota_cars = df[df['Brand'] == 'Toyota']
print(f"The number of cars from the brand 'Toyota' is {len(toyota_cars)}")

#17. What is the average price of cars with automatic transmission? 
automatic_transmission_cars = df[df['Transmission'] == 'Automatic']
average_price_automatic = automatic_transmission_cars['Price'].mean()
print(f"The average price of cars with automatic transmission is {average_price_automatic}")

#18. Which car has the highest owner count? 
highest_owner_car = df[df['Owner_Count'] == df['Owner_Count'].max()]['Model'].iloc[0]
print(f"The car with the highest owner count is {highest_owner_car}")

#19. What is the average engine size for cars with diesel fuel type? 
diesel_cars = df[df['Fuel_Type'] == 'Diesel']
average_engine_size_diesel = diesel_cars['Engine_Size'].mean()
print(f"The average engine size for cars with diesel fuel type is {average_engine_size_diesel}")

#20. How many cars have a price greater than $10,000? 
expensive_cars = df[df['Price'] > 10000]
print(f"The number of cars with a price greater than $10,000 is {len(expensive_cars)}")