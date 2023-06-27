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
    "networkcloud virtualmachine console update",
    is_experimental=True,
)
class Update(AAZCommand):
    """Update the properties of the provided virtual machine console, or update the tags associated with the virtual machine console. Properties and tag updates can be done independently.

    :example: Patch virtual machine console
        az networkcloud virtualmachine console update --enabled "True" --expiration "2022-06-01T01:27:03.008Z" --ssh-public-key key-data="ssh-rsa AAtsE3njSONzDYRIZv/WLjVuMfrUSByHp+jfaaOLHTIIB4fJvo6dQUZxE20w2iDHV3tEkmnTo84eba97VMueQD6OzJPEyWZMRpz8UYWOd0IXeRqiFu1lawNblZhwNT/ojNZfpB3af/YDzwQCZgTcTRyNNhL4o/blKUmug0daSsSXISTRnIDpcf5qytjs1Xo+yYyJMvzLL59mhAyb3p/cD+Y3/s3WhAx+l0XOKpzXnblrv9d3q4c2tWmm/SyFqthaqd0= admin@vm" --tags key1="myvalue1" key2="myvalue2" --resource-group "resourceGroupName" --virtual-machine-name "virtualMachineName"

    :example: Patch virtual machine console with SSH key file
        az networkcloud virtualmachine console update --enabled "True" --expiration "2022-06-01T01:27:03.008Z" --ssh-public-key key-data=~/.ssh/id_rsa.pub --tags key1="myvalue1" key2="myvalue2" --resource-group "resourceGroupName" --virtual-machine-name "virtualMachineName"
    """

    _aaz_info = {
        "version": "2023-05-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/virtualmachines/{}/consoles/{}", "2023-05-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

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
        _args_schema.console_name = AAZStrArg(
            options=["-n", "--name", "--console-name"],
            help="The name of the virtual machine console.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^default$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.virtual_machine_name = AAZStrArg(
            options=["--virtual-machine-name"],
            help="The name of the virtual machine.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9]{0,62}[a-zA-Z0-9])$",
            ),
        )

        # define Arg Group "ConsoleUpdateParameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="ConsoleUpdateParameters",
            help="The Azure resource tags that will replace the existing ones.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.enabled = AAZStrArg(
            options=["--enabled"],
            arg_group="Properties",
            help="The credentials used to login to the image repository that has access to the specified image.",
            enum={"False": "False", "True": "True"},
        )
        _args_schema.expiration = AAZDateTimeArg(
            options=["--expiration"],
            arg_group="Properties",
            help="The date and time after which the key will be disallowed access.",
        )
        _args_schema.ssh_public_key = AAZObjectArg(
            options=["--ssh-public-key"],
            arg_group="Properties",
            help="The SSH public key that will be provisioned for user access. The user is expected to have the corresponding SSH private key for logging in.",
        )

        ssh_public_key = cls._args_schema.ssh_public_key
        ssh_public_key.key_data = AAZStrArg(
            options=["key-data"],
            help="The public ssh key of the user.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ConsolesUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ConsolesUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/virtualMachines/{virtualMachineName}/consoles/{consoleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "consoleName", self.ctx.args.console_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualMachineName", self.ctx.args.virtual_machine_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-05-01-preview",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("enabled", AAZStrType, ".enabled")
                properties.set_prop("expiration", AAZStrType, ".expiration")
                properties.set_prop("sshPublicKey", AAZObjectType, ".ssh_public_key")

            ssh_public_key = _builder.get(".properties.sshPublicKey")
            if ssh_public_key is not None:
                ssh_public_key.set_prop("keyData", AAZStrType, ".key_data", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
            _UpdateHelper._build_schema_console_read(cls._schema_on_200)

            return cls._schema_on_200


class _UpdateHelper:
    """Helper class for Update"""

    _schema_console_read = None

    @classmethod
    def _build_schema_console_read(cls, _schema):
        if cls._schema_console_read is not None:
            _schema.extended_location = cls._schema_console_read.extended_location
            _schema.id = cls._schema_console_read.id
            _schema.location = cls._schema_console_read.location
            _schema.name = cls._schema_console_read.name
            _schema.properties = cls._schema_console_read.properties
            _schema.system_data = cls._schema_console_read.system_data
            _schema.tags = cls._schema_console_read.tags
            _schema.type = cls._schema_console_read.type
            return

        cls._schema_console_read = _schema_console_read = AAZObjectType()

        console_read = _schema_console_read
        console_read.extended_location = AAZObjectType(
            serialized_name="extendedLocation",
            flags={"required": True},
        )
        console_read.id = AAZStrType(
            flags={"read_only": True},
        )
        console_read.location = AAZStrType(
            flags={"required": True},
        )
        console_read.name = AAZStrType(
            flags={"read_only": True},
        )
        console_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        console_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        console_read.tags = AAZDictType()
        console_read.type = AAZStrType(
            flags={"read_only": True},
        )

        extended_location = _schema_console_read.extended_location
        extended_location.name = AAZStrType(
            flags={"required": True},
        )
        extended_location.type = AAZStrType(
            flags={"required": True},
        )

        properties = _schema_console_read.properties
        properties.detailed_status = AAZStrType(
            serialized_name="detailedStatus",
            flags={"read_only": True},
        )
        properties.detailed_status_message = AAZStrType(
            serialized_name="detailedStatusMessage",
            flags={"read_only": True},
        )
        properties.enabled = AAZStrType(
            flags={"required": True},
        )
        properties.expiration = AAZStrType()
        properties.private_link_service_id = AAZStrType(
            serialized_name="privateLinkServiceId",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.ssh_public_key = AAZObjectType(
            serialized_name="sshPublicKey",
            flags={"required": True},
        )
        properties.virtual_machine_access_id = AAZStrType(
            serialized_name="virtualMachineAccessId",
            flags={"read_only": True},
        )

        ssh_public_key = _schema_console_read.properties.ssh_public_key
        ssh_public_key.key_data = AAZStrType(
            serialized_name="keyData",
            flags={"required": True},
        )

        system_data = _schema_console_read.system_data
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

        tags = _schema_console_read.tags
        tags.Element = AAZStrType()

        _schema.extended_location = cls._schema_console_read.extended_location
        _schema.id = cls._schema_console_read.id
        _schema.location = cls._schema_console_read.location
        _schema.name = cls._schema_console_read.name
        _schema.properties = cls._schema_console_read.properties
        _schema.system_data = cls._schema_console_read.system_data
        _schema.tags = cls._schema_console_read.tags
        _schema.type = cls._schema_console_read.type


__all__ = ["Update"]
