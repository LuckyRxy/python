# todo: 存储和管理MDAV算法执行过程中的信息
#
# @Time: 2024/12/23 12:36:30
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import numpy as np
import pandas as pd
import numpy.typing as npt


class MicroInfo:

    protected_data: pd.DataFrame
    original_data: pd.DataFrame

    """
    @todo: 
    @param: k值为聚类的大小，即每个微簇包含的记录数
    @return: 
    """
    def __init__(self, k: int, original_data: pd.DataFrame) -> None:
        self.k = k
        self.original_data = original_data
        self.clusters: list[list[int]] = []

    """
    @todo: 迭代每个微簇的记录 
    @param: 
    @return: 
    """
    def cluster_values_iter(self) -> npt.ArrayLike: # type: ignore
        for c in self.clusters:
            yield self.original_data.iloc[c]

    def num_columns(self) -> int:
        return self.original_data.shape[1]
    
    def num_records(self) -> int:
        return self.original_data.shape[0]
    
    def num_clusters(self) -> int:
        return len(self.clusters)
    
    def num_cells(self) -> int:
        return self.num_clusters() * self.num_columns()
    
    def add_cluster(self, cluster: list[int]) -> None:
        self.clusters.append(cluster)

    def __str__(self):
        return (f"<MicroInfo> k:{self.k}, "
                f"  data size:{self.original.shape[0]}x{self.original.shape[1]} "
                f"  n_clusters:{self.num_clusters()}")