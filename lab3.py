import math
import csv
from collections import Counter

with open('ds2.csv') as csvFile:
    g_data = [tuple(line) for line in csv.reader(csvFile)]
    g_headers = g_data[0]
    g_data = g_data[1:]

class Node:
    def __init__(self, headers, data):
        self.decision_attribute = None
        self.child = {}
        self.headers = headers
        self.data = data
        self.decision = None


def get_attribute_column(headers, data, attribute):
    i = headers.index(attribute)
    a_list = [ele[i] for ele in data]
    return a_list


def calculate_entropy(probs):
    return sum([-prob * math.log(prob, 2) for prob in probs])


def split_data(headers, data, attribute, attr_value):
    i = headers.index(attribute)
    return [ele for ele in data if ele[i] == attr_value]


def entropy(headers, data, attribute='PlayTennis', gain=False):
    cnt = Counter(get_attribute_column(headers, data, attribute))
    num_instances = len(data)
    probs = [x / num_instances for x in cnt.values()]
    if not gain:
        return calculate_entropy(probs)
    gain = 0
    for Class, prob in zip(cnt.keys(), probs):
        gain += -prob * entropy(headers, split_data(headers, data, attribute, Class))
    return gain


def information_gain(headers, data):
    max_gain = -1
    max_gain_attribute = None
    for attribute in headers:
        if attribute == 'PlayTennis':
            continue
        gain = entropy(headers, data) + entropy(headers, data, attribute, gain=True)
        if gain > max_gain:
            max_gain = gain
            max_gain_attribute = attribute
    return max_gain_attribute


def drop_attribute(headers, data, attribute):
    i = headers.index(attribute)
    new_headers = [ele for ele in headers if ele != attribute]
    new_dataset = [tuple(data[:i] + data[i + 1:]) for data in data]
    return new_headers, new_dataset


def most_common_outcome(headers, data):
    cnt = Counter(get_attribute_column(headers, data, 'PlayTennis'))
    return cnt.most_common(1)[0][0]


def id3(root):
    if len(root.headers) == 1:
        root.decision = most_common_outcome(root.headers, root.data)
        return
    outcome_value_set = set(get_attribute_column(root.headers, root.data, 'PlayTennis'))
    if len(outcome_value_set) == 1:
        root.decision = list(outcome_value_set)[0]
        return
    max_gain_attribute = information_gain(root.headers, root.data)
    root.decision_attribute = max_gain_attribute
    for attr_val in set(get_attribute_column(root.headers, root.data, max_gain_attribute)):
        child_data = split_data(root.headers, root.data, max_gain_attribute, attr_val)
        if child_data is None or len(child_data) == 0:
            root.decision = most_common_outcome(root.headers,root.data)
            return
        (new_headers, new_data) = drop_attribute(root.headers, child_data, max_gain_attribute)
        root.child[attr_val] = Node(new_headers, new_data)
        id3(root.child[attr_val])


root = Node(g_headers, g_data)
id3(root)


def print_tree(root, disp=""):
    if root.decision is not None:
        if len(disp) == 0:
            print(str(root.decision))
        else:
            print(disp[:-4] + "THEN " + str(root.decision))
        return
    for attribute, node in root.child.items():
        print_tree(node, disp + "IF {} EQUALS {} AND ".format(root.decision_attribute, attribute))


print("Decision Tree Rules:")
print_tree(root)