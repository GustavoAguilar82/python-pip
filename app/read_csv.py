import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #reader es un iterable, entonces, puedo iterar de 1 en 1
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data
#me trae toda la informacion en un array que contiene varios diccionarios

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
# el delimeter depende de como mi archivo csv separe los elementos, si con , o ; 
