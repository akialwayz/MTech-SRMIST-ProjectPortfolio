import math
class Van_Emde_Boas:
    def __init__(self, size):
        self.universe_size = size
        self.minimum = -1
        self.maximum = -1
        # Base case
        if size <= 2:
            self.summary = None
            self.clusters = []
        else:
            no_clusters = math.ceil(math.sqrt(size))
            self.summary = Van_Emde_Boas(no_clusters)
            self.clusters = [Van_Emde_Boas(math.ceil(math.sqrt(size))) for i in range(no_clusters)]
            
    def high(self, x):
        div = math.ceil(math.sqrt(self.universe_size))
        return x // div
    
    def low(self, x):
        mod = math.ceil(math.sqrt(self.universe_size))
        return x % mod

    def generate_index(self, x, y):
        ru = math.ceil(math.sqrt(self.universe_size))
        return x * ru + y

def VEB_minimum(helper):
    return helper.minimum if helper.minimum != -1 else -1

def VEB_maximum(helper):
    return helper.maximum if helper.maximum != -1 else -1

def insert(helper, key):
    if helper.minimum == -1:
        helper.minimum = key
        helper.maximum = key
    else:
        if key < helper.minimum:
            helper.minimum, key = key, helper.minimum
        if helper.universe_size > 2:
            if VEB_minimum(helper.clusters[helper.high(key)]) == -1:
                insert(helper.summary, helper.high(key))
                helper.clusters[helper.high(key)].minimum = helper.low(key)
                helper.clusters[helper.high(key)].maximum = helper.low(key)
            else:
                insert(helper.clusters[helper.high(key)], helper.low(key))
                if helper.clusters[helper.high(key)].maximum == helper.clusters[helper.high(key)].minimum:
                    insert(helper.summary, helper.high(key))
                    helper.clusters[helper.high(key)].minimum = -1
                    helper.clusters[helper.high(key)].maximum = -1
                elif helper.clusters[helper.high(key)].maximum > helper.maximum:
                    helper.maximum = helper.clusters[helper.high(key)].maximum


def print_veb(veb, depth=0):
    if veb is None:
        return
    if veb.universe_size <= 2:
        print("  " * depth + f"VEB(2) [min: {veb.minimum}, max: {veb.maximum}]")
        return
    print_veb(veb.summary, depth + 1)
    for i, cluster in enumerate(veb.clusters):
        print("  " * depth + f"Cluster {i} [min: {cluster.minimum}, max: {cluster.maximum}]")
        print_veb(cluster, depth + 1)

# create VEB tree
universe_size = 16
veb = Van_Emde_Boas(universe_size)

# insert values
for value in [0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0]:
    insert(veb, value)

# print the tree
print_veb(veb)
