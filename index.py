import hazelcast

client = hazelcast.HazelcastClient(
    cluster_name="dev",
    cluster_members=[
        "endpoint-hazelcast-operator.apps.qa.interbanking.com.ar",
    ],
    lifecycle_listeners=[
        lambda state: print("Lifecycle event >>>", state),
    ]
)

print("Connected to cluster")
client.shutdown()