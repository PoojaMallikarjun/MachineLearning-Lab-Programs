import csv

a = []

with open('mushroom.csv') as csfile:
    reader = csv.reader(csfile)
    for row in reader:
        a.append(row)
        print(row)

num_attributes = len(a[0]) - 1

genreic_hypothesis = ["?"]*num_attributes
specific_hypothesis = ["0"]*num_attributes
print("The total number of training instances are:", len(a))
# print("The most specific hypothesis is represented by ", genreic_hypothesis)
print( specific_hypothesis)

hypothesis = specific_hypothesis
print("Find-s: Finding maximally specific hypothesis")

hypothesis = a[0][:-1]

for i in range(len(a)):
    if a[i][num_attributes] == "Yes":
        for j in range(num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = "?"
        print("The training example no:", +i+1,
              "the hypothesis is ", hypothesis)

print("The maximally specific hypothesis is: ")
print(hypothesis)