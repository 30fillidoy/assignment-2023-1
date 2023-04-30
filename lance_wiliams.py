import sys

# Define a function to compute the distance between two clusters
def distance(cluster1, cluster2, method):
    if method == 'single':
        # Single link method: distance between the two closest points in the clusters
        return min([abs(i-j) for i in cluster1 for j in cluster2])
    elif method == 'complete':
        # Complete link method: distance between the two farthest points in the clusters
        return max([abs(i-j) for i in cluster1 for j in cluster2])
    elif method == 'average':
        # Complete link method: distance between the two farthest points in the clusters
        return (max([abs(i-j) for i in cluster1 for j in cluster2])+ min([abs(i-j) for i in cluster1 for j in cluster2]))/2
    else:
        raise ValueError('Invalid method')



# Get the method from the user input
if len(sys.argv) < 2:
    print('Usage: python lance_williams.py [single|complete|average]')
    sys.exit()
method = sys.argv[1]
if method != 'single' and method != 'complete'  and method != 'average':
    print('Invalid method. Methods should be one of: single|complete|average')
    sys.exit()


file = open(sys.argv[2], "r")

# Initialize the data and the clusters
data = file.read()
line = [int(i) for i in data.split(" ")]

clusters = [[i] for i in line]


# Perform the clustering
while len(clusters) > 1:
    # Find the two closest/farthest clusters
    distances = [[distance(clusters[i], clusters[j], method), i, j] for i in range(len(clusters)) for j in range(i+1, len(clusters))]
    closest = min(distances)
    # Merge the two clusters
    new_cluster = clusters[closest[1]] + clusters[closest[2]]
    # Remove the old clusters and adjust the remaining clusters' index values
    clusters = [clusters[i] for i in range(len(clusters)) if i != closest[1] and i != closest[2]]
    # Add the new cluster
    clusters.append(new_cluster)
    # Print the current step
    if len(clusters) >= 2:
        print('({}) ({}) {:.2f} {}'.format(' '.join(map(str, clusters[-2])), ' '.join(map(str, clusters[-1])), closest[0], len(new_cluster)))


