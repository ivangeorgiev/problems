from pathlib import Path

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.analytics import Databricks
from diagrams.azure.database import SQLDatabases
from diagrams.azure.security import KeyVaults
from diagrams.azure.compute import KubernetesServices
from diagrams.onprem.queue import Kafka
from diagrams.programming.framework import FastAPI
from diagrams.generic.compute import Rack
from diagrams.k8s.compute import Job as KubeJob


# Store diagram using the same filename as the python file.
diagram_filename = Path(__file__).with_suffix("")

with Diagram(
    "DAL - Unity Catalog as Consumption Pattern Architecture",
    filename=diagram_filename,
    show=True,
    direction="LR",
):

    # External systems
    kafka = Kafka("dcam-events")

    # Shared services
    datamodel = SQLDatabases("datamodel")
    keyvault = KeyVaults("Key Vault")

    workspace = Databricks("management-workspace")

    with Cluster("AKS Cluster"):

        keda = KubeJob("KEDA")
        orchestrator = KubeJob("orchestrator\n(Scaled Job)")

        unity = FastAPI("unity API")
        avm = FastAPI("avm API")

        # KEDA triggers orchestrator
        kafka >> Edge(label="monitor lag") >> keda
        keda >> Edge(label="scale jobs") >> orchestrator

        # Message consumption
        kafka >> Edge(label="consume events") >> orchestrator

        # API calls
        orchestrator >> Edge(label="provision UC objects") >> unity
        orchestrator >> Edge(label="manage schemas/views") >> avm

        # Secrets
        keyvault >> Edge(label="SPN credentials") >> orchestrator
        keyvault >> Edge(label="SPN credentials") >> unity
        keyvault >> Edge(label="SPN credentials") >> avm

    # Databricks usage
    unity >> Edge(label="catalog APIs") >> workspace
    avm >> Edge(label="jobs / SQL APIs") >> workspace

    # Database persistence
    orchestrator >> Edge(label="consumer metadata") >> datamodel
    # unity >> Edge(style="dashed", label="optional consumer metadata") >> datamodel
