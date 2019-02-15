# -*- coding: utf-8 -*-
import numpy as np

def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a
    :param vector_b: 向量 b
    :return: sim
    """

    vector_a = np.mat(np.array(vector_a,dtype=float))
    vector_b = np.mat(np.array(vector_b,dtype=float))
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

def add_str(str):
    return "'"+str+"'"