import data_generator, chart_generator

print("Moldova anual compensation calculator and visualizer by 02-t")
print("-\n-\n-\nPress 1 to generate random data\n"
      "Press 2 to visualize the data\n"
      )
choice = input("Your choice: ")

if choice == '1':
    print("\nGenerating the data...\n")
    data_generator.generate_data()
    print("\nFinished! Data saved to data.csv")
else:
    print("Initializing chart...\n")
    chart_generator.run_chart()