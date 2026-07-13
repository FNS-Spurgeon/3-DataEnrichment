import csv

csv_file = "output3.csv"  # Allusions file
index_file = "../../3-DataExtraction/index/index-csv/index-works.csv"  # Index file
newCsvlines = []

# We parse the allusions file
with open(csv_file, 'r') as c:
    reader = csv.reader(c)

    header = next(reader)  # We get the first line

    # We parse each line of the allusions file
    for row in reader:
        # print(row)
        part = row[2][5:]  # We get the part number only ("Part V" > "V")
        page = row[3][1:]  # We get the page number only ("p24" > "24")
        date = row[5]
        author = row[7].split(",")  # We get the author and split it to get the surname
        author_cleaned = author[0].replace(".", "")  # We remove final dots if there are any
        # print(author_cleaned)

        # We open and parse the index file
        with open(index_file, 'r') as csvinput:
            file = csv.reader(csvinput)
            next(file)  # We skip the first line

            for i in file:
                # We want to find lines where part, page, author's name and date are the same
                if part == i[5] and page == i[6] and author_cleaned == i[3] and date == i[4]:
                    print(row)
                    print(author[0], i[3])
                    print('YES')

                    if row[-1] == '':
                        row[-1] = i[0] + "," + i[1] + "," + i[2]
                    else:
                        row[-1] = row[-1] + "/" + i[0] + "," + i[1] + "," + i[2]
                else:
                    pass

        newCsvlines.append(row)  # The new rows are appended a list

        # We transform the list into a new CSV
        with open('output4.csv', 'w', encoding='utf-8', newline='') as csvoutput:
            writer = csv.writer(csvoutput)
            writer.writerow(header)
            writer.writerows(newCsvlines)
            csvoutput.close()
