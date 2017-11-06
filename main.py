import csv

row_names = ['movie_id', 'movie_title']
with open('u.item.txt', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.DictReader(f, fieldnames=row_names, delimiter='|')
    for row in reader:
        print(row['movie_id'], row['movie_title'])