# Returns index, specifying only address and appropriate lookup table
def get_address_index(address, lookup_table):
    return lookup_table.index(address)

# Returns distance between two addresses
def get_distance(address1, address2, address_lookup, distance_lookup):
    index1 = get_address_index(address1, address_lookup)
    index2 = get_address_index(address2, address_lookup)

    if distance_lookup[index1][index2] == '':
        return float(distance_lookup[index2][index1])

    return float(distance_lookup[index1][index2])

# helper function to identify shortest distance node
def get_shortest_distance_node(current, unvisited, address_lookup, distance_lookup):
    # set shortest distance to infinity - all nodes currently shorter
    shortest_distance = float('inf')

    # initialize shortest distance node
    shortest_distance_node = None

    # iterate over each unvisited node to determine shortest, using existing helper functions
    # when distance is equal, use first appearance of shortest distance
    for node in unvisited:
        distance = get_distance(current, node, address_lookup, distance_lookup)

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_distance_node = node

    # return node to visit next
    return shortest_distance_node




# implement nearest-neighbor to route a list of addresses
def get_route(hub, addresses, address_lookup, distance_lookup):
    current_node = hub
    # all packages at same address will be delivered at same time - set removes duplicates
    unvisited = set(addresses)
    visited = []

    while len(unvisited) > 0:
        visited.append(current_node)
        next_to_visit = get_shortest_distance_node(current_node, unvisited, address_lookup, distance_lookup)
        unvisited.remove(next_to_visit)
        current_node = next_to_visit

    # appending last node will not be caught in while loop
    visited.append(current_node)

    # append hub to account for return trip to hub following final delivery
    visited.append(hub)

    return visited

# given a full route, calculate the total distance
def get_route_distance(route, address_lookup, distance_matrix):
    route_distance = 0
    for i in range(len(route) - 1):
        route_distance += get_distance(route[i], route[i+1], address_lookup, distance_matrix)

    return route_distance
