import chart_generator
import data_generator

print("Moldova anual compensation calculator and visualizer by 02-t")
print("-\n-\n-\nPress 1 to generate 50 random entries\n"
      "Press 2 to generate  data for every color possible\n"
      "Press 3 to visualize the data\n"
      )
choice = input("Your choice: ")

if choice == '1':
    print("\nGenerating the data...\n")
    data_generator.generate_data()
    print("\nFinished! Data saved to data.csv")
elif choice == '2':
    print("\nGenerating the data...\n")
    data_generator.generate_full_data()
    print("\nFinished! Data saved to data.csv")
else:
    print("Initializing chart...\n")
    chart_generator.run_chart()
