"""

1. Install graphviz
2. Test graphviz installation `dot -V`
3. Install diagrams: `uv tool install diagrams`

"""

from pathlib import Path

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB, Route53

# Store diagram using the same filename as the python file.
diagram_filename = Path(__file__).with_suffix("")

with Diagram("Clustered Web Service", filename=diagram_filename, show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"), ECS("web2"), ECS("web3")]

    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    memcached = ElastiCache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
