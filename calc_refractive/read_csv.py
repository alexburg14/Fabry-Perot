import csv
def read_csv(filename):
    # Initialize empty arrays for each column
    columns = []

    # Open the CSV file
    with open(filename, 'r', encoding= "utf-8") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Read the headers

        # Initialize empty arrays for each column
        for _ in range(len(headers)):
            columns.append([])

        # Read each row and store values into respective columns
        for row in csv_reader:
            for i, value in enumerate(row):
                # Replace commas inside numbers with dots and remove apostrophes
                cleaned_value = value.replace(',', '.').replace("'","")

                try:
                    # Try converting the cleaned value to float
                    columns[i].append(float(cleaned_value))
                except ValueError:
                    # If conversion fails, just append the cleaned value as is
                    pass

    return columns
