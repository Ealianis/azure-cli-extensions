# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps['fleet'] = """
    type: group
    short-summary: Commands to manage fleet.
"""

helps['fleet create'] = """
    type: command
    short-summary: Creates or updates a Fleet.
    parameters:
        - name: --dns-name-prefix -p
          type: string
          short-summary: Prefix for hostnames that are created. If not specified, generate a hostname using the
                         managed cluster and resource group names.
    examples:
        - name: Create a hubless fleet.
          text: az fleet create -g MyFleetResourceGroup -l MyLocation -n MyFleetName --tags "TagKey=TagValue"
        - name: Create a hubful fleet.
          text: az fleet create -g MyFleetResourceGroup -l MyLocation -n MyFleetName --enable-hub --tags "TagKey=TagValue"
        - name: Create a fleet with a system assigned Managed Service Identity.
          text: az fleet create -g MyFleetResourceGroup -l MyLocation -n MyFleetName --enable-managed-identity
        - name: Create a fleet with a user provided Managed Service Identity.
          text: az fleet create -g MyFleetResourceGroup -l MyLocation -n MyFleetName --enable-managed-identity --assign-identity "/subscription/00000000-0000-0000-0000-000000000000/resourcegroup/MyFleetResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MyIdentity"
"""

helps['fleet update'] = """
    type: command
    short-summary: Patches a fleet resource.
    examples:
        - name: Update a Fleet's tags.
          text: az fleet update -g MyFleetResourceGroup -n MyFleetName --tags Key=Value
        - name: Update a Fleet to use a system assigned managed service identity.
          text: az fleet update -g MyFleetResourceGroup -n MyFleetName --enable-managed-identity --tags Key=Value
        - name: Update a Fleet to use a user assigned managed service identity.
          text: az fleet update -g MyFleetResourceGroup -n MyFleetName --enable-managed-identity --assign-identity "/subscription/00000000-0000-0000-0000-000000000000/resourcegroup/MyFleetResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MyIdentity" --tags Key=Value
"""

helps['fleet show'] = """
    type: command
    short-summary: Gets a Fleet.
    examples:
        - name: Show the details of a fleet.
          text: az fleet show -g MyFleetResourceGroup -f MyFleetName
"""

helps['fleet list'] = """
    type: command
    short-summary: Lists all fleets within a resource group.
    examples:
        - name: List all fleets that exist within a specific subscription and resource group.
          text: az fleet list -g MyResourceGroup
"""

helps['fleet delete'] = """
    type: command
    short-summary: Deletes a Fleet.
    examples:
        - name: Delete a specific fleet.
          text: az fleet delete -g MyFleetResourceGroup -f MyFleetName
"""

helps['fleet get-credentials'] = """
    type: command
    short-summary: For hubful fleets, gets the kubeconfig for the fleet's hub cluster.
    parameters:
    - name: --overwrite-existing
      type: bool
      short-summary: Overwrite any existing cluster entry with the same name.
    - name: --file -f
      type: string
      short-summary: Kubernetes configuration file to update. Use "-" to print YAML to stdout instead.
    examples:
        - name: Get a Fleet's hub cluster kubeconfig. 
          text: az fleet get-credentials -g MyFleetResourceGroup -n MyFleetName
        - name: Get a Fleet's hub cluster kubeconfig, and save it to a specific file.
          text: az fleet get-credentials -g MyFleetResourceGroup -n MyFleetName -f ~/mykubeconfigfile.txt
"""

helps['fleet wait'] = """
type: command
short-summary: Wait for a fleet resource to reach a desired state.
long-summary: If an operation on fleet was interrupted or was started with `--no-wait`, use this command to wait for it to complete.
"""

helps['fleet member'] = """
    type: group
    short-summary: Commands to manage a fleet member.
"""

helps['fleet member create'] = """
    type: command
    short-summary: Creates or updates a fleet member.
    parameters:
        - name: --member-cluster-id
          type: string
          short-summary: ID of the managed cluster.
        - name: --update-group
          type: string
          short-summary: Group of the fleet member.
    examples:
        - name: Create a fleet member and assign it to a specific update group.
          text: az fleet member create -g MyFleetResourceGroup -f MyFleetName -n NameOfMember --update-group UpdateGroup1 --member-cluster-id "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyFleetResourceGroup/providers/Microsoft.ContainerService/managedClusters/MyManagedCluster"
"""

helps['fleet member update'] = """
    type: command
    short-summary: Update a fleet member.
    parameters:
        - name: --update-group
          type: string
          short-summary: Group of the fleet member.
    examples:
        - name: Update an existing member's update group.
          text: az fleet member update -g MyFleetResourceGroup -f MyFleetName -n NameOfMember --update-group UpdateGroup2"
"""

helps['fleet member list'] = """
    type: command
    short-summary: Lists the members of a fleet.
    examples:
        - name: List all members for a given fleet.
          text: az fleet member list -g MyFleetResourceGroup -n MyFleetName
"""

helps['fleet member show'] = """
    type: command
    short-summary: Gets a fleet member.
    examples:
        - name: Show the details of a specific fleet member.
          text: az fleet member show -g MyFleetResourceGroup -f MyFleetName -n NameOfMember
"""

helps['fleet member delete'] = """
    type: command
    short-summary: Deletes a fleet member.
    examples:
        - name: Delete a specific fleet member
          text: az fleet member delete -g MyFleetResourceGroup -f MyFleetName -n NameOfMember
"""

helps['fleet member wait'] = """
    type: command
    short-summary: Wait for a fleet member resource to reach a desired state.
    long-summary: If an operation on fleet member was interrupted or was started with `--no-wait`, use this command to wait for it to complete.
"""

helps['fleet updaterun'] = """
    type: group
    short-summary: Commands to manage a fleet update run.
"""

helps['fleet updaterun create'] = """
    type: command
    short-summary: Creates or updates a fleet update run.
    parameters:
        - name: --upgrade-type
          type: string
          short-summary: Specify the upgrade type of fleet members. Acceptable values are 'Full' and 'NodeImageOnly'.
        - name: --kubernetes-version
          type: string
          short-summary: Specify the kubernetes version to upgrade fleet member(s) to, when --upgrade-type is set to 'Full'. Acceptable format is x.x.x (eg. 1.2.3).
        - name: --stages
          type: string
          short-summary: Path to a json file that defines stages to upgrade a fleet. See examples for further reference.
    examples:
        - name: Create updaterun for a fleet with 'Full' upgrade type.
          text: az fleet updaterun create -g MyResourceGroup -f MyFleet -n MyUpdateRun --upgrade-type Full --kubernetes-version 1.25.0 --node-image-selection Latest
        - name: Create updaterun for a fleet with 'NodeImageOnly' upgrade type.
          text: az fleet updaterun create -g MyResourceGroup -f MyFleet -n MyUpdateRun --upgrade-type NodeImageOnly --node-image-selection Latest
        - name: Create updaterun for a fleet with 'Full' upgrade type & stages.
          text: |
            az fleet updaterun create -g MyResourceGroup -f MyFleet -n MyUpdateRun --upgrade-type Full --kubernetes-version 1.25.0 --node-image-selection Latest --stages ./test/stages.json

                A sample json to demonstrate the expected format. It takes a stages array. Each stage consists of the stage name, groups array and an optional afterStageWaitInSeconds integer.
                Within groups, each group consists of group name, given to a fleet's member(s).
                {
                    "stages": [
                        {
                            "name": "stage1",
                            "groups": [
                                {
                                    "name": "group-a1"
                                },
                                {
                                    "name": "group-a2"
                                },
                                {
                                    "name": "group-a3"
                                }
                            ],
                            "afterStageWaitInSeconds": 3600
                        },
                        {
                            "name": "stage2",
                            "groups": [
                                {
                                    "name": "group-b1"
                                },
                                {
                                    "name": "group-b2"
                                },
                                {
                                    "name": "group-b3"
                                }
                            ]
                        },
                    ]
                }
"""

helps['fleet updaterun show'] = """
    type: command
    short-summary: Shows a fleet update run.
    examples:
        - name: Show the details of a specific updaterun
          text: az fleet updaterun show -g MyFleetResourceGroup -f MyFleetName -n NameofUpdateRun
"""

helps['fleet updaterun list'] = """
    type: command
    short-summary: Lists the update runs of a fleet.
    examples:
        - name: Show the details of a specific updaterun
          text: az fleet updaterun show -g MyFleetResourceGroup -f MyFleetName -n NameofUpdateRun
"""

helps['fleet updaterun delete'] = """
    type: command
    short-summary: Deletes a fleet update run.
    examples:
        - name: Delete a specific updaterun.
          text: az fleet updaterun delete -g MyFleetResourceGroup -f MyFleetName -n NameofUpdateRun
"""

helps['fleet updaterun start'] = """
    type: command
    short-summary: Starts a fleet update run.
    examples:
        - name: Starts an updaterun
          text: az fleet updaterun start -g MyFleetResourceGroup -f MyFleetName -n NameofUpdateRun
"""

helps['fleet updaterun stop'] = """
    type: command
    short-summary: Stops a fleet update run.
    examples:
        - name: Stops an updaterun
          text: az fleet updaterun stop -g MyFleetResourceGroup -f MyFleetName -n NameofUpdateRun
    
"""

helps['fleet updaterun wait'] = """
    type: command
    short-summary: Wait for a fleet updateraun resource to reach a desired state.
    long-summary: If an operation on fleet updateraun was interrupted or was started with `--no-wait`, use this command to wait for it to complete.
"""

helps['fleet updatestrategy'] = """
    type: group
    short-summary: Commands to manage a fleet update strategy.
"""

helps['fleet updatestrategy create'] = """
    type: command
    short-summary: Creates or updates a update strategy
    parameters:
        - name: --stages
          type: string
          short-summary: Path to a json file that defines the update strategy.
    examples:
        - name: Create an updatestrategy from a JSON file.
          text: az fleet updatestrategy create -g MyFleetResourceGroup -f MyFleetName -n MyUpdateStrategy --stages MyUpdateStrategyFile.json
"""

helps['fleet updatestrategy show'] = """
    type: command
    short-summary: Shows a update strategy.
    examples:
        - name: Show the details of a specific updatestrategy.
          text: az fleet updatestrategy show -g MyFleetResourceGroup -f MyFleetName -n MyUpdateStrategy
"""

helps['fleet updatestrategy list'] = """
    type: command
    short-summary: Lists the fleet's update strategies.
    examples:
        - name: List all updatestratgies for a given fleet.
          text: az fleet updatestrategy list -g MyFleetResourceGroup -f MyFleetName
"""

helps['fleet updatestrategy delete'] = """
    type: command
    short-summary: Deletes a update strategy.
    examples:
        - name: Delete a specific updatestrategy.
          text: az fleet updatestrategy delete -g MyFleetResourceGroup -f MyFleetName -n MyUpdateStrategy
"""

helps['fleet updatestrategy wait'] = """
    type: command
    short-summary: Wait for a fleet updatestrategy resource to reach a desired state.
    long-summary: If an operation on fleet updatestrategy was interrupted or was started with `--no-wait`, use this command to wait for it to complete.
"""
