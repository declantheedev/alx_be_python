weather = input('Whats the weather like today? (sunny/rainy/cold):').strip().lower();
if weather == 'sunny':
    print('Wear a t-shirt and sunglasses'); 
elif weather == 'rainy':
    print("Don't forget to take an umbrella.");
elif weather == 'cold':
    print("Make sure to wear a warm coat and scarf");
else:
    print("Sorry, I don't have recommendations for this weather.")
    
