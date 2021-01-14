from src.GraphInterface import GraphInterface


class NodeData:

    def __init__(self, key: int = None, tag: int = 0, pos: tuple = None):
        self.key = key
        self.tag = tag
        self.pos = pos

    def __repr__(self):
        return f'NodeData: {self.key}, tag={self.tag}, pos= {self.pos}'


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodesMap = {}
        self.outMap = {}
        self.inMap = {}
        self.mc = 0
        self.edgesSize = 0

    def v_size(self) -> int:
        return len(self.nodesMap)

    def e_size(self) -> int:
        return self.edgesSize

    def get_all_v(self) -> dict:
        return self.nodesMap

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.inMap.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.outMap.get(id1)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (self.nodesMap.get(id1) is not None) and (self.nodesMap.get(id2) is not None) and (id1 is not id2) and (
                weight >= 0):
            if id2 not in self.outMap.get(id1) and id1 not in self.inMap.get(id2):
                self.outMap[id1][id2] = weight
                self.inMap[id2][id1] = weight
                self.edgesSize = self.edgesSize + 1
                self.mc = self.mc + 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodesMap.get(node_id) is not None:
            return False
        else:
            node = NodeData(key=node_id, pos=pos)
            self.nodesMap[node_id] = node
            self.inMap[node_id] = {}
            self.outMap[node_id] = {}
            self.mc = self.mc + 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if self.nodesMap.get(node_id) is not None:
            for i in self.inMap.keys():
                if node_id in self.inMap.get(i).keys():
                    self.remove_edge(i, node_id)
                    self.mc = self.mc - 1
            for j in self.outMap.keys():
                if node_id in self.inMap.get(j).keys():
                    self.remove_edge(node_id, j)
                    self.mc = self.mc - 1
            del self.nodesMap[node_id]
            self.mc = self.mc + 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (self.nodesMap.get(node_id1) is not None) and (self.nodesMap.get(node_id2) is not None) and (
                node_id1 is not node_id2):
            if node_id2 in self.outMap.get(node_id1) and node_id1 in self.inMap.get(node_id2):
                del self.outMap[node_id1][node_id2]
                del self.inMap[node_id2][node_id1]
                self.edgesSize = self.edgesSize - 1
                self.mc = self.mc + 1
                return True
        else:
            return False
