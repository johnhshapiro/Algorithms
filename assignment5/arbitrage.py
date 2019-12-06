trade_list = []

def build_edge_list():
    data = open("exchange.txt", "r")
    rates = data.read().splitlines()
    edges = []
    currency_count = rates[0]
    for line in rates[1:]:
        line = line.split()
        origin_currency = line[0]
        destination_currency = line[1]
        rate = float(line[2])
        edges.append((origin_currency,destination_currency,rate))
    data.close()
    return edges, currency_count

if __name__ == "__main__":
    graph, currency_count = build_edge_list()
    current_currency = graph[0][0]
    print(current_currency, currency_count)
        