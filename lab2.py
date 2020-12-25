# # import random
# # import csv
# # def g_0(n):
# #     return ("?",)*n
# #
# #
# # def s_0(n):
# #     return ('ɸ',)*n
# #
# #
# # def more_general(h1, h2):
# #     more_general_parts = []
# #     for x, y in zip(h1, h2):
# #         mg = x == "?" or (x != "ɸ" and (x == y or y == "ɸ"))
# #         more_general_parts.append(mg)
# #     return all(more_general_parts)
# #
# #
# # def fulfills(example, hypothesis):
# #     return more_general(hypothesis, example)
# #
# #
# # def min_generalizations(h, x):
# #     h_new = list(h)
# #     for i in range(len(h)):
# #         if not fulfills(x[i:i+1], h[i:i+1]):
# #             h_new[i] = '?' if h[i] != 'ɸ' else x[i]
# #     return [tuple(h_new)]
# #
# #
# # def min_specializations(h, domains, x):
# #     results = []
# #     for i in range(len(h)):
# #         if h[i] == "?":
# #             for val in domains[i]:
# #                 if x[i] != val:
# #                     h_new = h[:i] + (val,) + h[i + 1:]
# #                     results.append(h_new)
# #         elif h[i] != "ɸ":
# #             h_new = h[:i] + ('ɸ',) + h[i + 1:]
# #             results.append(h_new)
# #     return results
# #
# #
# # with open('train.csv') as csvFile:
# #     examples = [tuple(line) for line in csv.reader(csvFile)]
# #
# # def get_domains(examples):
# #     d = [set() for i in examples[0]]
# #     for x in examples:
# #         for i, xi in enumerate(x):
# #             d[i].add(xi)
# #     return [list(sorted(x)) for x in d]
# #
# #
# # get_domains(examples)
# #
# #
# # def candidate_elimination(examples):
# #      domains = get_domains(examples)[:-1]
# #      G = set([g_0(len(domains))])
# #      S = set([s_0(len(domains))])
# #      i = 0
# #      print("\n G[{0}]:".format(i), G)
# #      print("\n S[{0}]:".format(i), S)
# #      for xcx in examples:
# #          i = i + 1
# #          x, cx = xcx[:-1], xcx[-1]  # Splitting data into attributes and decisions
# #          if cx == 'Y':  # x is positive example
# #              G = {g for g in G if fulfills(x, g)}
# #              S = generalize_S(x, G, S)
# #          else:
# #              S = {s for s in S if not fulfills(x, s)}
# #              G = specialize_G(x, domains, G, S)
# #          print("\n G[{0}]:".format(i), G)
# #          print("\n S[{0}]:".format(i), S)
# #      return
# #
# #
# # def generalize_S(x, G, S):
# #     S_prev = list(S)
# #     for s in S_prev:
# #         if s not in S:
# #             continue
# #         if not fulfills(x, s):
# #             S.remove(s)
# #             Splus = min_generalizations(s, x)
# #             S.update([h for h in Splus if any([more_general(g,h) for g in G])])
# #             S.difference_update([h for h in S if any([more_general(h, h1) for h1 in S if h != h1])])
# #     return S
# #
# #
# # def specialize_G(x, domains, G, S):
# #     G_prev = list(G)
# #     for g in G_prev:
# #         if g not in G:
# #             continue
# #         if fulfills(x, g):
# #             G.remove(g)
# #             Gminus = min_specializations(g, domains, x)
# #             ## keep only specializations that have a conuterpart in S
# #             G.update([h for h in Gminus if any([more_general(h, s) for s in S])])
# #              ## remove hypotheses less general than any other in G
# #             G.difference_update([h for h in G if any([more_general(g1, h) for g1 in G if h != g1])])
# #     return G
# # candidate_elimination(examples)
# import csv
#
# with open('train.csv') as csvFile:
#     data = [tuple(line) for line in csv.reader(csvFile)]
#
#
# def domain():
#     D = []
#     for i in range(len(data[0])):
#         D.append(list(set([ele[i] for ele in data])))
#     return D
#
#
# D = domain()
# print(D)
#
#
# def is_consistent(h1, h2):
#     for x, y in zip(h1, h2):
#         if x != "?" and (x == "o" or x != y):
#             return False
#     return True
#
#
# def candidate_elimination():
#     G = {('?',) * (len(data[0]) - 1), }
#     S = ['o'] * (len(data[0]) - 1)
#     no = 0
#     print("\n G[{0}]:".format(no), G)
#     print("\n S[{0}]:".format(no), S)
#     for item in data:
#         no += 1
#         inp, res = item[:-1], item[-1]
#         if res in "Yy":
#             i = 0
#             G = {g for g in G if is_consistent(g, inp)}
#             for s, x in zip(S, inp):
#                 if not s == x:
#                     S[i] = '?' if s != 'o' else x
#                 i += 1
#         else:
#             Gprev = G.copy()
#             print("gprev:",Gprev)
#             for g in Gprev:
#                 print(g)
#                 if g not in G:
#                     continue
#                 for i in range(len(g)):
#                     if g[i] == "?":
#                         for val in D[i]:
#                             if inp[i] != val and val == S[i]:
#                                 g_new = g[:i] + (val,) + g[i + 1:]
#                                 G.add(g_new)
#                     else:
#                         G.add(g)
#                 G.difference_update([h for h in G if
#                                      any([is_consistent(h, g1) for g1 in G if h != g1])])
#         print("\n G[{0}]:".format(no), G)
#         print("\n S[{0}]:".format(no), S)
#
#
# if __name__ == '__main__':
#     candidate_elimination()
import csv

with open('train.csv') as csvf:
	data = [tuple(line) for line in csv.reader(csvf)]

S = ['phi']* (len(data[0])-1)
G = ['?']* (len(data[0])-1)
print('S 0: ',S)
print('G 0: ',G)
cnt=0

#Getting all possible values for each attribute in the dataset
all_possible_values=dict()
for i in range(len(data[0])-1):
	if i not in all_possible_values.keys():
		all_possible_values[i] = set()
	for j in range(len(data)):
		all_possible_values[i].add(data[j][i])
#Loop through each training example
for x in data:
	if x[-1] == 'Y':
		for i in range(len(x)-1):
			if S[i] == 'phi' or x[i] == S[i]:											# Basically FIND-S
				S[i] = x[i]
			else:
				search_str = '<' + ' ? '*i + S[i] + ' ? '*(len(S)-i-1) + '>'			#Inconsistent ele from G are removed, for eg
				if search_str in G:														#if <??'Cloudy'??> is in G but both 'Cloudy' & 'Sunny'
					G.remove(search_str)												#appear in +ve eg, <??'Cloudy'??> is removed
				S[i] = '?'
	elif x[-1] == 'N':
		if '?' in G:
			#Clears G of any '?' elements (which were initialised in line 8) and hence, checks if its the FIRST negative eg
			G = [g for g in G if g!= '?']
			for i in range(len(x)-1):
				if S[i] != x[i] and S[i] != '?':										#for eg: if 'Sunny' occurs in a negative example,
					for possibleVals in all_possible_values[i]:							# and all possible vals for that attribute are
						if possibleVals != x[i]:										# Sunny, Windy and Cloudy, append these elements to G
							new = '<' + ' ? '*i + possibleVals + ' ? '*(len(S)-i-1) + '>' # <??'Windy'??> and <??'Cloudy'??>
							if new not in G:											# This happens only for the FIRST negative example
								G.append(new)											# Coz ele in G decrease over time, not vice versa
		for i in range(len(x)-1):
			if S[i] != x[i] and S[i] != '?':
				search_str = '<' + ' ? '*i + x[i] + ' ? '*(len(S)-i-1) + '>'			# Any inconsistent ele in G are removed for eg.
				if search_str in G:														# if <??'Cloudy'??> is in G and Cloudy appears in a
					G.remove(search_str)												# negative eg, <??'Cloudy'??> is removed from G
	cnt+=1
	print('S',cnt,': ',S, '   ',)
	print('G',cnt,': ',G)




