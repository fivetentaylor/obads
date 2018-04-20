
# node or leaf | data | offset to next
#    [0,1]     | .... |  [-1, offset]

#Function: search (k)
#  return tree_search (k, root);
# 
#Function: tree_search (k, node)
#  if node is a leaf then
#    return node;
#  switch k do
#  case k < k_0
#    return tree_search(k, p_0);
#  case k_i ≤ k < k_{i+1}
#    return tree_search(k, p_{i+1});
#  case k_d ≤ k
#    return tree_search(k, p_{d+1});

def search(k, node):
    if node[0]: return node
    
    if 
