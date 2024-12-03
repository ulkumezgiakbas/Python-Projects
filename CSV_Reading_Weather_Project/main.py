import pandas as pd

data = pd.read_csv("weather_data.csv")

print(data[data['day'] == "Monday"])

print(data[data['temp'] == data['temp'].max()])

monday = data[data['day'] == "Monday"]

monday_temp = monday['temp'].iloc[0]
monday_temp_F = monday_temp * 9 / 5 + 32
print(f"Here is the F value of temp: {monday_temp_F}")

data_dict = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "condition": ["Sunny", "Rain", "Cloudy", "Sunny", "Rain", "Cloudy", "Sunny"]
}
new_data = pd.DataFrame(data_dict)

new_data.to_csv("new_data.csv", index=False)
