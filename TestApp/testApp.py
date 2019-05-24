from TSP.TSP import TSP
if __name__ == '__main__':
    map = {"prima": {"seconda": 2, "quarta": 10}, "seconda": {"terza": 1, "prima": 2}, "terza": {}, "quarta": {"prima": 5}}
    TSP(map)
