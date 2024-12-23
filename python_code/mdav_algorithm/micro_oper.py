# todo: implement the Maximum distance vector algorithm
#
# @Time: 2024/12/23 13:02:38
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import pathlib
import pickle
import numpy as np
import pandas as pd
import numpy.typing as npt

from sklearn.metrics.pairwise import euclidean_distances

from micro_info import MicroInfo

"""
@todo:  返回与给定记录距离最远的记录的索引，使用欧氏距离 
@param: 
@return: 与记录距离最大的记录的索引（标签）
"""
def _farthest_record_index(df: pd.DataFrame, record: pd.Series) -> int:
    distances = euclidean_distances(df, [record])
    far_index = distances.argmax()
    return df.index[far_index]

"""
@todo: 返回与给定记录最近的 k 个记录的索引，构成一个簇。
@param: 
@return: 
"""
def _closest_k_record_index(df: pd.DataFrame, record: pd.Series, 
                            k: int) -> npt.ArrayLike: # type: ignore
    diatances = euclidean_distances(df, [record]).flatten()
    indices = diatances.argpartition(k)[:k]
    return df.index[indices].values

"""
@todo: 创建一个微簇，并用簇的均值更新保护数据集 prot 中的记录，同时删除原始数据集 orig 中的相应记录。 
@param: 
@return: 
"""
def _make_cluster(orig: pd.DataFrame, prot: pd.DataFrame, 
                 record: pd.Series, k: int) -> list[int]:
    
    indices = _closest_k_record_index(orig, record, k)
    centroid = orig.loc[indices].mean()
    prot.iloc[indices, ] = centroid.values
    orig.drop(indices, inplace=True)
    return indices

"""
@todo: 对剩余的记录进行聚类，计算均值并更新保护数据集 prot
@param: 
@return: 
"""
def _cluster_remaining(orig: pd.DataFrame, prot: pd.DataFrame) -> list[int]:
    centroide = orig.mean()
    indices = orig.index
    prot.iloc[orig.index, ] = centroide.values
    orig.drop(indices, inplace=True)
    return indices

"""
@todo: 执行MDAV算法，返回保护数据集和微簇信息
@param: 
@return: 
"""
def mdav_algorithm(df: pd.DataFrame, k: int, columns: list[int] = None) -> tuple[pd.DataFrame, MicroInfo]:
    if columns:
        orig = df[columns].copy(deep=True)
    else:
        orig = df.copy(deep=True)

    prot = pd.DataFrame(columns=orig.columns, 
                        index=orig.index,
                        dtype=np.float64)
    
    stats = MicroInfo(k, orig.copy(deep=True))

    while orig.shape[0] >= 3 * k:
        # data mean
        center = orig.mean()
        # most distant record to center
        x_r_index = _farthest_record_index(orig, center)
        x_r_value = orig.loc[x_r_index]
        # make k cluster on x_r
        idx = _make_cluster(orig, prot, x_r_value, k)
        stats.add_cluster(idx)
        # most distance record to x_r
        x_s_index = _farthest_record_index(orig, x_r_value)
        # make k cluster on x_s
        idx = _make_cluster(orig, prot, orig.loc[x_s_index], k)
        stats.add_cluster(idx)
    
    if orig.shape[0] >= 2 * k:
        center = orig.mean()
        x_r_index = _farthest_record_index(orig, center)
        idx = _make_cluster(orig, prot, orig.loc[x_r_index], k)
        stats.add_cluster(idx)
    
    idx = _cluster_remaining(orig, prot)
    stats.add_cluster(idx)
    stats.protected_data = prot.copy(deep=True)
    return prot, stats


def run_madv(file_path, filename, output, k: int):
    csv_filename = filename + f'_k{k}' + '.csv'
    pickle_filename = filename + f'_k{k}' + '.pickle'

    print(f"MDAV for k={k}:...", end=" " + '\n')
    df = pd.read_csv(file_path)
    protected, stats = mdav_algorithm(df, k)
    print('done.')

    protected.to_csv(output + csv_filename, index=False)
    with open(output + pickle_filename, "wb") as f:
        pickle.dump(stats, f)
    print(f"Protected data saved to: {csv_filename}")
    print(f"Microaggregation info saved to: {pickle_filename}")



if __name__ == "__main__":
    k = 5
    file_path = r'python_code\mdav_algorithm\data\banes-2019-11-13.csv'
    filename = 'banes-2019-11-13'
    output = r'python_code\mdav_algorithm\output\\'
    run_madv(file_path, filename, output, k)

