from graphdatascience import GraphDataScience

gds = GraphDataScience(
    "neo4j+s://23a7cf73.databases.neo4j.io",
    auth=("neo4j", "XsU2xCiyksCXgPmNTmncPvrsQib4YGb2Nhl-5-_j3s0"),
    database="neo4j",
)
gds.set_compute_cluster_ip("34.142.81.53") # field-testing GCP machine. Fixed.

try:
    G = gds.graph.get("cora")
except:
    G = gds.graph.load_cora("cora")

#sub2vec example

# output = gds.sub2vec.train_and_stream(
#     G,
#     model_name="cora_sub2vec_3",
#     subgraphs=[[31336, 31349, 686532, 1129442], [24043, 928873, 15076, 1111265]],
#     embedding_dimension=128,
#     window=3,
#     min_count=1,
#     workers=1,
#     num_epochs=10,
#     walk_length=5,
#     mlflow_experiment_name="test",
# )
#
# print(output)

predictions = gds.sub2vec.predict_and_stream(
    G,
    model_name="cora_sub2vec_3",
    subgraphs=[[31336, 31349, 686532, 1129442], [24043, 928873, 15076, 1111265]],
    mlflow_experiment_name="test",
)

print(predictions)