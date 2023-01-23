# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "mobile-network sim policy update",
)
class Update(AAZCommand):
    """Update a SIM policy.

    :example: Update sim policy tags
        az mobile-network sim policy update -g rg-n sim-policy-name --mobile-network-name mobile-network-name --tags "{tag:test,tag2:test2}"
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.mobilenetwork/mobilenetworks/{}/simpolicies/{}", "2022-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.mobile_network_name = AAZStrArg(
            options=["--mobile-network-name"],
            help="The name of the mobile network.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_-]*$",
                max_length=64,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.sim_policy_name = AAZStrArg(
            options=["-n", "--name", "--sim-policy-name"],
            help="The name of the SIM policy.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_-]*$",
                max_length=64,
            ),
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.default_slice = AAZObjectArg(
            options=["--default-slice"],
            arg_group="Properties",
            help="The default slice to use if the UE does not explicitly specify it. This slice must exist in the `sliceConfigurations` map.",
        )
        cls._build_args_slice_resource_id_update(_args_schema.default_slice)
        _args_schema.registration_timer = AAZIntArg(
            options=["--registration-timer"],
            arg_group="Properties",
            help="Interval for the UE periodic registration update procedure, in seconds.",
            nullable=True,
            fmt=AAZIntArgFormat(
                minimum=30,
            ),
        )
        _args_schema.rfsp_index = AAZIntArg(
            options=["--rfsp-index"],
            arg_group="Properties",
            help="RAT/Frequency Selection Priority Index, defined in 3GPP TS 36.413. This is an optional setting and by default is unspecified.",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=256,
                minimum=1,
            ),
        )
        _args_schema.slice_config = AAZListArg(
            options=["--slice-config"],
            arg_group="Properties",
            help="The allowed slices and the settings to use for them. The list must not contain duplicate items and must contain at least one item.",
            fmt=AAZListArgFormat(
                unique=True,
            ),
        )
        _args_schema.ue_ambr = AAZObjectArg(
            options=["--ue-ambr"],
            arg_group="Properties",
            help="Aggregate maximum bit rate across all non-GBR QoS flows of all PDU sessions of a given UE. See 3GPP TS23.501 section 5.7.2.6 for a full description of the UE-AMBR.",
        )
        cls._build_args_ambr_update(_args_schema.ue_ambr)

        slice_config = cls._args_schema.slice_config
        slice_config.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.slice_config.Element
        _element.data_network_config = AAZListArg(
            options=["data-network-config"],
            help="The allowed data networks and the settings to use for them. The list must not contain duplicate items and must contain at least one item.",
            fmt=AAZListArgFormat(
                unique=True,
            ),
        )
        _element.default_data_network = AAZObjectArg(
            options=["default-data-network"],
            help="The default data network to use if the UE does not explicitly specify it. Configuration for this object must exist in the `dataNetworkConfigurations` map.",
        )
        cls._build_args_data_network_resource_id_update(_element.default_data_network)
        _element.slice = AAZObjectArg(
            options=["slice"],
            help="A reference to the slice that these settings apply to",
        )
        cls._build_args_slice_resource_id_update(_element.slice)

        data_network_config = cls._args_schema.slice_config.Element.data_network_config
        data_network_config.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.slice_config.Element.data_network_config.Element
        _element.five_qi = AAZIntArg(
            options=["five-qi"],
            help="Default QoS Flow 5G QoS Indicator value. The 5QI identifies a specific QoS forwarding treatment to be provided to a flow. This must not be a standardized 5QI value corresponding to a GBR (guaranteed bit rate) QoS Flow. The illegal GBR 5QI values are: 1, 2, 3, 4, 65, 66, 67, 71, 72, 73, 74, 75, 76, 82, 83, 84, and 85. See 3GPP TS23.501 section 5.7.2.1 for a full description of the 5QI parameter, and table 5.7.4-1 for the definition of which are the GBR 5QI values.",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=255,
                minimum=0,
            ),
        )
        _element.additional_session_type = AAZListArg(
            options=["additional-session-type"],
            help="Allowed session types in addition to the default session type. Must not duplicate the default session type.",
            nullable=True,
        )
        _element.arp_level = AAZIntArg(
            options=["arp-level"],
            help="Default QoS Flow allocation and retention priority (ARP) level. Flows with higher priority preempt flows with lower priority, if the settings of `preemptionCapability` and `preemptionVulnerability` allow it. 1 is the highest level of priority. If this field is not specified then `5qi` is used to derive the ARP value. See 3GPP TS23.501 section 5.7.2.2 for a full description of the ARP parameters.",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=15,
                minimum=1,
            ),
        )
        _element.allowed_services = AAZListArg(
            options=["allowed-services"],
            help="List of services that can be used as part of this SIM policy. The list must not contain duplicate items and must contain at least one item.",
            fmt=AAZListArgFormat(
                unique=True,
            ),
        )
        _element.data_network = AAZObjectArg(
            options=["data-network"],
            help="A reference to the data network that these settings apply to",
        )
        cls._build_args_data_network_resource_id_update(_element.data_network)
        _element.default_session_type = AAZStrArg(
            options=["default-session-type"],
            help="The default PDU session type, which is used if the UE does not request a specific session type.",
            nullable=True,
            enum={"IPv4": "IPv4", "IPv6": "IPv6"},
        )
        _element.maximum_number_of_buffered_packets = AAZIntArg(
            options=["maximum-number-of-buffered-packets"],
            help="The maximum number of downlink packets to buffer at the user plane for High Latency Communication - Extended Buffering. See 3GPP TS29.272 v15.10.0 section 7.3.188 for a full description. This maximum is not guaranteed because there is a internal limit on buffered packets across all PDU sessions.",
            nullable=True,
            fmt=AAZIntArgFormat(
                minimum=0,
            ),
        )
        _element.preemption_capability = AAZStrArg(
            options=["preemption-capability"],
            help="Default QoS Flow preemption capability. The preemption capability of a QoS Flow controls whether it can preempt another QoS Flow with a lower priority level. See 3GPP TS23.501 section 5.7.2.2 for a full description of the ARP parameters.",
            nullable=True,
            enum={"MayPreempt": "MayPreempt", "NotPreempt": "NotPreempt"},
        )
        _element.preemption_vulnerability = AAZStrArg(
            options=["preemption-vulnerability"],
            help="Default QoS Flow preemption vulnerability. The preemption vulnerability of a QoS Flow controls whether it can be preempted by a QoS Flow with a higher priority level. See 3GPP TS23.501 section 5.7.2.2 for a full description of the ARP parameters.",
            nullable=True,
            enum={"NotPreemptable": "NotPreemptable", "Preemptable": "Preemptable"},
        )
        _element.session_ambr = AAZObjectArg(
            options=["session-ambr"],
            help="Aggregate maximum bit rate across all non-GBR QoS flows of a given PDU session. See 3GPP TS23.501 section 5.7.2.6 for a full description of the Session-AMBR.",
        )
        cls._build_args_ambr_update(_element.session_ambr)

        additional_session_type = cls._args_schema.slice_config.Element.data_network_config.Element.additional_session_type
        additional_session_type.Element = AAZStrArg(
            nullable=True,
            enum={"IPv4": "IPv4", "IPv6": "IPv6"},
        )

        allowed_services = cls._args_schema.slice_config.Element.data_network_config.Element.allowed_services
        allowed_services.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.slice_config.Element.data_network_config.Element.allowed_services.Element
        _element.id = AAZStrArg(
            options=["id"],
            help="Service resource ID.",
            fmt=AAZStrArgFormat(
                pattern="^/[sS][uU][bB][sS][cC][rR][iI][pP][tT][iI][oO][nN][sS]/[^/?#]+/[rR][eE][sS][oO][uU][rR][cC][eE][gG][rR][oO][uU][pP][sS]/[^/?#]+/[pP][rR][oO][vV][iI][dD][eE][rR][sS]/[mM][iI][cC][rR][oO][sS][oO][fF][tT]\.[mM][oO][bB][iI][lL][eE][nN][eE][tT][wW][oO][rR][kK]/[mM][oO][bB][iI][lL][eE][nN][eE][tT][wW][oO][rR][kK][sS]/[^/?#]+/[sS][eE][rR][vV][iI][cC][eE][sS]/[^/?#]+$",
            ),
        )
        return cls._args_schema

    _args_ambr_update = None

    @classmethod
    def _build_args_ambr_update(cls, _schema):
        if cls._args_ambr_update is not None:
            _schema.downlink = cls._args_ambr_update.downlink
            _schema.uplink = cls._args_ambr_update.uplink
            return

        cls._args_ambr_update = AAZObjectArg()

        ambr_update = cls._args_ambr_update
        ambr_update.downlink = AAZStrArg(
            options=["downlink"],
            help="Downlink bit rate.",
            fmt=AAZStrArgFormat(
                pattern="^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$",
            ),
        )
        ambr_update.uplink = AAZStrArg(
            options=["uplink"],
            help="Uplink bit rate.",
            fmt=AAZStrArgFormat(
                pattern="^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$",
            ),
        )

        _schema.downlink = cls._args_ambr_update.downlink
        _schema.uplink = cls._args_ambr_update.uplink

    _args_data_network_resource_id_update = None

    @classmethod
    def _build_args_data_network_resource_id_update(cls, _schema):
        if cls._args_data_network_resource_id_update is not None:
            _schema.id = cls._args_data_network_resource_id_update.id
            return

        cls._args_data_network_resource_id_update = AAZObjectArg()

        data_network_resource_id_update = cls._args_data_network_resource_id_update
        data_network_resource_id_update.id = AAZStrArg(
            options=["id"],
            help="Data network resource ID.",
            fmt=AAZStrArgFormat(
                pattern="^/[sS][uU][bB][sS][cC][rR][iI][pP][tT][iI][oO][nN][sS]/[^/?#]+/[rR][eE][sS][oO][uU][rR][cC][eE][gG][rR][oO][uU][pP][sS]/[^/?#]+/[pP][rR][oO][vV][iI][dD][eE][rR][sS]/[mM][iI][cC][rR][oO][sS][oO][fF][tT]\.[mM][oO][bB][iI][lL][eE][nN][eE][tT][wW][oO][rR][kK]/[mM][oO][bB][iI][lL][eE][nN][eE][tT][wW][oO][rR][kK][sS]/[^/?#]+/[dD][aA][tT][aA][nN][eE][tT][wW][oO][rR][kK][sS]/[^/?#]+$",
            ),
        )

        _schema.id = cls._args_data_network_resource_id_update.id

    _args_slice_resource_id_update = None

    @classmethod
    def _build_args_slice_resource_id_update(cls, _schema):
        if cls._args_slice_resource_id_update is not None:
            _schema.id = cls._args_slice_resource_id_update.id
            return

        cls._args_slice_resource_id_update = AAZObjectArg()

        slice_resource_id_update = cls._args_slice_resource_id_update
        slice_resource_id_update.id = AAZStrArg(
            options=["id"],
            help="Slice resource ID.",
            fmt=AAZStrArgFormat(
                pattern="^/[sS][uU][bB][sS][cC][rR][iI][pP][tT][iI][oO][nN][sS]/[^/?#]+/[rR][eE][sS][oO][uU][rR][cC][eE][gG][rR][oO][uU][pP][sS]/[^/?#]+/[pP][rR][oO][vV][iI][dD][eE][rR][sS]/[mM][iI][cC][rR][oO][sS][oO][fF][tT]\.[mM][oO][bB][iI][lL][eE][nN][eE][tT][wW][oO][rR][kK]/[mM][oO][bB][iI][lL][eE][nN][eE][tT][wW][oO][rR][kK][sS]/[^/?#]+/[sS][lL][iI][cC][eE][sS]/[^/?#]+$",
            ),
        )

        _schema.id = cls._args_slice_resource_id_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.SimPoliciesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.SimPoliciesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SimPoliciesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/mobileNetworks/{mobileNetworkName}/simPolicies/{simPolicyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "mobileNetworkName", self.ctx.args.mobile_network_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "simPolicyName", self.ctx.args.sim_policy_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_sim_policy_read(cls._schema_on_200)

            return cls._schema_on_200

    class SimPoliciesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/mobileNetworks/{mobileNetworkName}/simPolicies/{simPolicyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "mobileNetworkName", self.ctx.args.mobile_network_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "simPolicyName", self.ctx.args.sim_policy_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_sim_policy_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                _UpdateHelper._build_schema_slice_resource_id_update(properties.set_prop("defaultSlice", AAZObjectType, ".default_slice", typ_kwargs={"flags": {"required": True}}))
                properties.set_prop("registrationTimer", AAZIntType, ".registration_timer")
                properties.set_prop("rfspIndex", AAZIntType, ".rfsp_index")
                properties.set_prop("sliceConfigurations", AAZListType, ".slice_config", typ_kwargs={"flags": {"required": True}})
                _UpdateHelper._build_schema_ambr_update(properties.set_prop("ueAmbr", AAZObjectType, ".ue_ambr", typ_kwargs={"flags": {"required": True}}))

            slice_configurations = _builder.get(".properties.sliceConfigurations")
            if slice_configurations is not None:
                slice_configurations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.sliceConfigurations[]")
            if _elements is not None:
                _elements.set_prop("dataNetworkConfigurations", AAZListType, ".data_network_config", typ_kwargs={"flags": {"required": True}})
                _UpdateHelper._build_schema_data_network_resource_id_update(_elements.set_prop("defaultDataNetwork", AAZObjectType, ".default_data_network", typ_kwargs={"flags": {"required": True}}))
                _UpdateHelper._build_schema_slice_resource_id_update(_elements.set_prop("slice", AAZObjectType, ".slice", typ_kwargs={"flags": {"required": True}}))

            data_network_configurations = _builder.get(".properties.sliceConfigurations[].dataNetworkConfigurations")
            if data_network_configurations is not None:
                data_network_configurations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.sliceConfigurations[].dataNetworkConfigurations[]")
            if _elements is not None:
                _elements.set_prop("5qi", AAZIntType, ".five_qi")
                _elements.set_prop("additionalAllowedSessionTypes", AAZListType, ".additional_session_type")
                _elements.set_prop("allocationAndRetentionPriorityLevel", AAZIntType, ".arp_level")
                _elements.set_prop("allowedServices", AAZListType, ".allowed_services", typ_kwargs={"flags": {"required": True}})
                _UpdateHelper._build_schema_data_network_resource_id_update(_elements.set_prop("dataNetwork", AAZObjectType, ".data_network", typ_kwargs={"flags": {"required": True}}))
                _elements.set_prop("defaultSessionType", AAZStrType, ".default_session_type")
                _elements.set_prop("maximumNumberOfBufferedPackets", AAZIntType, ".maximum_number_of_buffered_packets")
                _elements.set_prop("preemptionCapability", AAZStrType, ".preemption_capability")
                _elements.set_prop("preemptionVulnerability", AAZStrType, ".preemption_vulnerability")
                _UpdateHelper._build_schema_ambr_update(_elements.set_prop("sessionAmbr", AAZObjectType, ".session_ambr", typ_kwargs={"flags": {"required": True}}))

            additional_allowed_session_types = _builder.get(".properties.sliceConfigurations[].dataNetworkConfigurations[].additionalAllowedSessionTypes")
            if additional_allowed_session_types is not None:
                additional_allowed_session_types.set_elements(AAZStrType, ".")

            allowed_services = _builder.get(".properties.sliceConfigurations[].dataNetworkConfigurations[].allowedServices")
            if allowed_services is not None:
                allowed_services.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.sliceConfigurations[].dataNetworkConfigurations[].allowedServices[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_ambr_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("downlink", AAZStrType, ".downlink", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("uplink", AAZStrType, ".uplink", typ_kwargs={"flags": {"required": True}})

    @classmethod
    def _build_schema_data_network_resource_id_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id", typ_kwargs={"flags": {"required": True}})

    @classmethod
    def _build_schema_slice_resource_id_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id", typ_kwargs={"flags": {"required": True}})

    _schema_ambr_read = None

    @classmethod
    def _build_schema_ambr_read(cls, _schema):
        if cls._schema_ambr_read is not None:
            _schema.downlink = cls._schema_ambr_read.downlink
            _schema.uplink = cls._schema_ambr_read.uplink
            return

        cls._schema_ambr_read = _schema_ambr_read = AAZObjectType()

        ambr_read = _schema_ambr_read
        ambr_read.downlink = AAZStrType(
            flags={"required": True},
        )
        ambr_read.uplink = AAZStrType(
            flags={"required": True},
        )

        _schema.downlink = cls._schema_ambr_read.downlink
        _schema.uplink = cls._schema_ambr_read.uplink

    _schema_data_network_resource_id_read = None

    @classmethod
    def _build_schema_data_network_resource_id_read(cls, _schema):
        if cls._schema_data_network_resource_id_read is not None:
            _schema.id = cls._schema_data_network_resource_id_read.id
            return

        cls._schema_data_network_resource_id_read = _schema_data_network_resource_id_read = AAZObjectType()

        data_network_resource_id_read = _schema_data_network_resource_id_read
        data_network_resource_id_read.id = AAZStrType(
            flags={"required": True},
        )

        _schema.id = cls._schema_data_network_resource_id_read.id

    _schema_sim_policy_read = None

    @classmethod
    def _build_schema_sim_policy_read(cls, _schema):
        if cls._schema_sim_policy_read is not None:
            _schema.id = cls._schema_sim_policy_read.id
            _schema.location = cls._schema_sim_policy_read.location
            _schema.name = cls._schema_sim_policy_read.name
            _schema.properties = cls._schema_sim_policy_read.properties
            _schema.system_data = cls._schema_sim_policy_read.system_data
            _schema.tags = cls._schema_sim_policy_read.tags
            _schema.type = cls._schema_sim_policy_read.type
            return

        cls._schema_sim_policy_read = _schema_sim_policy_read = AAZObjectType()

        sim_policy_read = _schema_sim_policy_read
        sim_policy_read.id = AAZStrType(
            flags={"read_only": True},
        )
        sim_policy_read.location = AAZStrType(
            flags={"required": True},
        )
        sim_policy_read.name = AAZStrType(
            flags={"read_only": True},
        )
        sim_policy_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        sim_policy_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        sim_policy_read.tags = AAZDictType()
        sim_policy_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_sim_policy_read.properties
        properties.default_slice = AAZObjectType(
            serialized_name="defaultSlice",
            flags={"required": True},
        )
        cls._build_schema_slice_resource_id_read(properties.default_slice)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.registration_timer = AAZIntType(
            serialized_name="registrationTimer",
        )
        properties.rfsp_index = AAZIntType(
            serialized_name="rfspIndex",
        )
        properties.site_provisioning_state = AAZDictType(
            serialized_name="siteProvisioningState",
            flags={"read_only": True},
        )
        properties.slice_configurations = AAZListType(
            serialized_name="sliceConfigurations",
            flags={"required": True},
        )
        properties.ue_ambr = AAZObjectType(
            serialized_name="ueAmbr",
            flags={"required": True},
        )
        cls._build_schema_ambr_read(properties.ue_ambr)

        site_provisioning_state = _schema_sim_policy_read.properties.site_provisioning_state
        site_provisioning_state.Element = AAZStrType(
            flags={"read_only": True},
        )

        slice_configurations = _schema_sim_policy_read.properties.slice_configurations
        slice_configurations.Element = AAZObjectType()

        _element = _schema_sim_policy_read.properties.slice_configurations.Element
        _element.data_network_configurations = AAZListType(
            serialized_name="dataNetworkConfigurations",
            flags={"required": True},
        )
        _element.default_data_network = AAZObjectType(
            serialized_name="defaultDataNetwork",
            flags={"required": True},
        )
        cls._build_schema_data_network_resource_id_read(_element.default_data_network)
        _element.slice = AAZObjectType(
            flags={"required": True},
        )
        cls._build_schema_slice_resource_id_read(_element.slice)

        data_network_configurations = _schema_sim_policy_read.properties.slice_configurations.Element.data_network_configurations
        data_network_configurations.Element = AAZObjectType()

        _element = _schema_sim_policy_read.properties.slice_configurations.Element.data_network_configurations.Element
        _element["5qi"] = AAZIntType()
        _element.additional_allowed_session_types = AAZListType(
            serialized_name="additionalAllowedSessionTypes",
        )
        _element.allocation_and_retention_priority_level = AAZIntType(
            serialized_name="allocationAndRetentionPriorityLevel",
        )
        _element.allowed_services = AAZListType(
            serialized_name="allowedServices",
            flags={"required": True},
        )
        _element.data_network = AAZObjectType(
            serialized_name="dataNetwork",
            flags={"required": True},
        )
        cls._build_schema_data_network_resource_id_read(_element.data_network)
        _element.default_session_type = AAZStrType(
            serialized_name="defaultSessionType",
        )
        _element.maximum_number_of_buffered_packets = AAZIntType(
            serialized_name="maximumNumberOfBufferedPackets",
        )
        _element.preemption_capability = AAZStrType(
            serialized_name="preemptionCapability",
        )
        _element.preemption_vulnerability = AAZStrType(
            serialized_name="preemptionVulnerability",
        )
        _element.session_ambr = AAZObjectType(
            serialized_name="sessionAmbr",
            flags={"required": True},
        )
        cls._build_schema_ambr_read(_element.session_ambr)

        additional_allowed_session_types = _schema_sim_policy_read.properties.slice_configurations.Element.data_network_configurations.Element.additional_allowed_session_types
        additional_allowed_session_types.Element = AAZStrType()

        allowed_services = _schema_sim_policy_read.properties.slice_configurations.Element.data_network_configurations.Element.allowed_services
        allowed_services.Element = AAZObjectType()

        _element = _schema_sim_policy_read.properties.slice_configurations.Element.data_network_configurations.Element.allowed_services.Element
        _element.id = AAZStrType(
            flags={"required": True},
        )

        system_data = _schema_sim_policy_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_sim_policy_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_sim_policy_read.id
        _schema.location = cls._schema_sim_policy_read.location
        _schema.name = cls._schema_sim_policy_read.name
        _schema.properties = cls._schema_sim_policy_read.properties
        _schema.system_data = cls._schema_sim_policy_read.system_data
        _schema.tags = cls._schema_sim_policy_read.tags
        _schema.type = cls._schema_sim_policy_read.type

    _schema_slice_resource_id_read = None

    @classmethod
    def _build_schema_slice_resource_id_read(cls, _schema):
        if cls._schema_slice_resource_id_read is not None:
            _schema.id = cls._schema_slice_resource_id_read.id
            return

        cls._schema_slice_resource_id_read = _schema_slice_resource_id_read = AAZObjectType()

        slice_resource_id_read = _schema_slice_resource_id_read
        slice_resource_id_read.id = AAZStrType(
            flags={"required": True},
        )

        _schema.id = cls._schema_slice_resource_id_read.id


__all__ = ["Update"]