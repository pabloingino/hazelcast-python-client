import hazelcast

client = hazelcast.HazelcastClient(
    cluster_name="dev",
    cluster_members=[
        "hz-hazelcast.hazelcast-operator:5701",
    ],
    lifecycle_listeners=[
        lambda state: print("Lifecycle event >>>", state),
    ]
)

print("Connected to cluster")
client.shutdown()