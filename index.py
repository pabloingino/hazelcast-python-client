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
# Get the Distributed Map from Cluster.
my_map = client.get_map("map-testing").blocking()
# Standard Put and Get
my_map.put("key2", "value2")
my_map.put("key3", "value3")
my_map.put("client_id", "88223")
my_map.get("key")
# Concurrent Map methods, optimistic updating
#my_map.put_if_absent("somekey", "somevalue")
#my_map.replace_if_same("key", "value", "newvalue")


client.shutdown()