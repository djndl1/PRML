#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import operator


def kNN_classify0(in_X, data_set, labels, k):
    """
        in_X: m-dim test sample 
        data_set: N-by-m training sets
        labels: corresponding labels
        k: top k nearest neighbors

        return: the lable of in_X
    """
    diff_mat = in_X - data_set
    distances = np.sum((diff_mat ** 2), 1)
    sorted_indices = distances.argsort(axis=0)
    class_count = {}      # a dict for label counts

    for i in range(k):
        vote_Ilabel = labels[sorted_indices[i]]
        class_count[vote_Ilabel] = class_count.get(vote_Ilabel, 0) + 1

    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_class_count[0][0]