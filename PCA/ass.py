import numpy as np
import time
from itertools import combinations

def read_data(file_name):
    file = open(file_name, 'r')
    data = []
    disease = []
    for line in file:
        genes = line.replace("\n","").split("\t")
        disease.append(genes.pop())
        for i in range(0,len(genes)):
            genes[i] = "G"+str(i+1)+"_"+genes[i]
        data.append(genes)

    return data


def support_count(data,map):
    for disease in data:
        for key in map.keys():
            klist = key.split()
            if set(klist).issubset(set(disease)):
                map[key] += 1
    return map


def remove_infrequent(data,freq_map,min_sup):
    temp = freq_map.copy()
    rm_list = []
    for key in freq_map.keys():
        if freq_map[key]/100 < min_sup:
            temp.pop(key)
            rm_list.append(key)
    freq_map = temp
    return freq_map


def k_level(data,freq_map,level,min_sup):
    if level == 1:
        for disease in data:
            for gene in disease:
                if gene not in freq_map.keys():
                    freq_map[gene] = 0
        freq_map = support_count(data,freq_map)
        freq_map = remove_infrequent(data,freq_map,min_sup)
        return freq_map
    else:
        map = {}
        klist = []
        for key in freq_map.keys():
            klist.append(key)
        comb = combinations(klist,level)
        for c in comb:
            count = 0
            gene = ""
            clist = list(c)
            while count < level:
                gene += str(clist[count]) + " "
                count += 1
            map[gene] = 0
        map = support_count(data,map)
        map = remove_infrequent(data,map,min_sup)
        return map


if __name__ == "__main__":
    data = read_data("association-rule-test-data.txt")

    min_sup = 0.40
    start = time.time()
    map = {}
    freq_map = k_level(data,map,1,min_sup)
    print("Number of length - 1 Frequent Itemset: " + str(len(freq_map)))

    for i in range(2,10):
        freq_map = k_level(data,freq_map,i,min_sup)
        print("Number of length - " + str(i)+ " Frequent Itemset: " + str(len(freq_map)))

    print(time.time()-start)