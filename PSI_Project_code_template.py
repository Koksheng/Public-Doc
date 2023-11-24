import pandas as pd

psi_data = pd.read_csv("Historical24hrPSI.csv")
if psi_data is not None:
    # Convert the '24-hr_psi' column to datetime with errors='coerce'
    psi_data['24-hr_psi'] = pd.to_datetime(psi_data['24-hr_psi'], format='%d/%m/%Y %H:%M', errors='coerce')

# Set display options to show all rows and columns
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

while True:
  print("")
  print('*******PSI data analytic System*******')
  print('1. Display PSI reading for November 2022 in Singapore')
  print('2. To display the highest PSI reading')
  print('3. To display the lowest PSI reading')
  print('4. To update PSI reading')
  print('5. To Save PSI data file \n')
  print('Press any other numbers to exit')

# Prompt the user to enter an option
  choice = input('Enter your option:')

# Use if - elif for conditional check and match the input (1 to 5, any other number exit the program)
  if choice == '1':
    # read excel file and assign to a data frame pd.read_excel(XXXX.xlsx)

    # Add your codes.....
    if psi_data is not None:
        # Filter data for November 2022
        nov_2022_data = psi_data[(psi_data['24-hr_psi'].dt.year == 2022) & (psi_data['24-hr_psi'].dt.month == 11)].copy()
        # Convert '24-hr_psi' column to the desired datetime format in the copied filtered DataFrame
        nov_2022_data.loc[:, '24-hr_psi'] = nov_2022_data['24-hr_psi'].dt.strftime('%Y-%d-%m %H:%M:%S')
        # Print the DataFrame
        print(nov_2022_data)


  elif choice == '2':
    
    # Prompt user to enter direction north, south, east or west for the highest PSI
    # Display the highest directon PSI. Hint: You may use method max() from pandas

    # Add your codes....
    if psi_data is not None:
      direction = input('Enter direction (north, south, east, west): ')
      if direction in psi_data.columns:
          highest_psi = psi_data[direction].max()
          print(f'The highest PSI reading in the {direction} direction is: {highest_psi}')
      else:
          print(f"Error: Direction {direction} not found in the data.")
    

  elif choice == '3':
    
    # Prompt user to enter direction north, south, east or west for the lowest PSI
    # Display the lowest directon PSI. Hint: You may use method min() from pandas

    # Add your codes....
    if psi_data is not None:
        direction = input('Enter direction (north, south, east, west): ')
        if direction in psi_data.columns:
            lowest_psi = psi_data[direction].min()
            print(f'The lowest PSI reading in the {direction} direction is: {lowest_psi}')
        else:
            print(f"Error: Direction {direction} not found in the data.")

  elif choice == '4':
    
    # Prompt the user to enter the date in DD/MM/YYYY, time in 24 hour and the new PSI value
    # Make sure the format is (DD/MM/YYYY hh:mm) refer to the given PSI data excel file
    # Compare the (DD/MM/YYYY hh:mm) in the data frame and get the row information
    # Use index.tolist() method to get the row index value based on the input(date and time)
    # *Use loc[row_index, [direction]] or at[row_index, direction] methods to change the value of the PSI

    # Add your codes....
    # Prompt the user to enter the date, time, and new PSI value
    input_date = input('Enter the date in YYYY-DD-MM format: ')
    input_time = input('Enter the time in 24-hour format HH:MM:SS: ')
    input_datetime_str = f'{input_date} {input_time}'
    new_psi_value = int(input('Enter the new PSI value: '))

    # Convert to pandas datetime object
    parsed_datetime = pd.to_datetime(input_datetime_str, format='%Y-%d-%m %H:%M:%S')

    # Format as a string in the desired format
    formatted_datetime_str = parsed_datetime.strftime('%Y-%m-%d %H:%M:%S')

    # Check if the input date and time exist in the DataFrame
    if (psi_data['24-hr_psi'] == formatted_datetime_str).any():
        # Get the index of the row with the matching date and time
        row_index = psi_data.index[psi_data['24-hr_psi'] == formatted_datetime_str][0]

        # Prompt the user to enter the direction to update
        direction = input('Enter direction (north, south, east, west, central): ')

        # Check if the entered direction exists in the DataFrame columns
        if direction in psi_data.columns:
            # Use the .at method to update the PSI value at the specified row and direction
            psi_data.at[row_index, direction] = new_psi_value
            print('PSI value updated successfully.')
        else:
            print(f"Error: Direction {direction} not found in the data.")
    else:
        print(f"No matching entry found for {input_datetime_str}. Please check your input.")


  elif choice == '5':
    # save excel file pd.to_excel(XXXX_new.xlsx)

    # Add your codes....
    print("Saving and exporting Historical24hrPSI_NOV_2022new.xlsx ...")
    # Filter data for November 2022
    nov_2022_data = psi_data[(psi_data['24-hr_psi'].dt.year == 2022) & (psi_data['24-hr_psi'].dt.month == 11)].copy()
    output_filename = "Historical24hrPSI_NOV_2022new.xlsx"
    nov_2022_data.to_excel(output_filename, index=False)
    print(f"PSI data for November 2022 saved to {output_filename} successfully.")

  else:
  # use break

  # Add your codes....
    print("Exiting the PSI data analytic system. Goodbye!")
    break
  