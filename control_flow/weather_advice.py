current_weather = input('Whats the weather like today? (sunny/rainy/cold):').strip().lower();
if current_weather == 'sunny':
    print('Wear a t-shirt and sunglasses'); 
elif current_weather == 'rainy':
    print("Don't forget to take an umbrella");
elif current_weather == 'cold':
    print("Make sure to wear a warm coat and scarf");
else:
    print("Sorry, I don't have recommendations for this weather.")
    
