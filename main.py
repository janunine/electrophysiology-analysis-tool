import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend for interactivity
# from decimal import Decimal


# Initialize an empty dictionary
my_dict = {}

# Open the text file for reading
with open("activ_04.txt", "r") as file:
    for line in file:
        # Split the line into two values using space as a separator
        key, value = line.strip().split()
        key = float(key)
        value = float(value)
        # Convert the value to a float and create a dictionary entry
        my_dict[key] = value


stimulus = {}
# Open the text file for reading stimulus
with open("stimulus_04.txt", "r") as file:
    for line in file:
        # Split the line into two values using space as a separator
        key, value = line.strip().split()
        key = float(key)
        value = float(value)
        # Convert the value to a float and create a dictionary entry
        stimulus[key] = value


# # Iterate through the dictionary and print key-value pairs
# for key, value in my_dict.items():
#     print(f'{key}: {value}')

# print(stimulus)


peak_keys = []  # Initialize a list to store peak keys

keys = list(my_dict.keys())  # Get a list of keys

for i in range(1, len(keys) - 1):
    key = keys[i]
    value = my_dict[key]
    if (
        value > 0
        and value >= my_dict[keys[i - 1]]
        and value >= my_dict[keys[i + 1]]
    ):
        peak_keys.append(key)

print("Peak Keys:", peak_keys)



# Extract all keys and their corresponding values from my_dict
all_keys = list(my_dict.keys())
all_values = [my_dict[key] for key in all_keys]


if peak_keys:
    # Create a fixed y-value for all peak values
    fixed_y = [0.7] * len(peak_keys)

    # Extract the values of the peak keys
    peak_values = [my_dict[key] for key in peak_keys]

    # Extract all keys and their corresponding values from my_dict
    all_keys = list(my_dict.keys())
    all_values = [my_dict[key] for key in all_keys]

    # Plot the scatter of peak values with y fixed at 1
    # no need for peak value
    # plt.scatter(peak_keys, fixed_y, c='pink', s=10, marker='o', label='Peak Values')


############


    positive_keys = []
    # Iterate through the peak keys
    for peak_key in peak_keys:


        reversed_dict = {key: stimulus[key] for key in reversed(stimulus)}

        start_search = False
        count = 0

        #print(reversed_dict)

        for key, value in reversed_dict.items():
            if start_search:
                if value > 4:
                    count = count + 1
                    if count == 50:
                        positive_keys.append(key)
                        break

                elif value < 4:
                    if count == 0:
                        continue
                    else:
                        break  # Stop when value < 4 is encountered
            if key == peak_key:
                start_search = True  # Set the flag to start the search from this point


    # Print the positive stimulus keys
    # print("Positive stimulus keys:", positive_keys)


    ############
    # Transform the dictionary
    transformed_dict = {key: 1 if value >= 4 else 0 for key, value in stimulus.items()}



    # # Extract all keys and their corresponding values from my_dict
    stimulus_keys = list(transformed_dict.keys())
    stimulus_values = [transformed_dict[key] for key in stimulus_keys]


    # Plot the scatter of peak values with y fixed at 1
    plt.plot(stimulus_keys, stimulus_values, c='blue')


    fixed_positive_stimu = [1.1] * len(positive_keys)

    # positive_values = [stimulus[key] for key in positive_keys]
    # plt.plot(positive_keys, positive_values, c='red', linewidth=2.0)
    plt.scatter(positive_keys, fixed_positive_stimu, c='black', s=15, marker='o')


    # plt.xlabel('Time')
    # plt.ylabel('Value')
    # plt.title('Plot of Peak Values with Fixed Y=1 and All Keys (Background)')

    plt.subplots_adjust(top=0.9, bottom=0.2)
    # plt.legend()
    plt.show()
else:
    print("No peak keys found in the dictionary.")

