from inspect import trace
from ansible.module_utils.basic import env_fallback
import traceback
from ansible.module_utils.basic import missing_required_lib


class AnsibleIPFModule(object):
    """An ansible module class for IP Fabric modules
    AnsibleIPFModule provides a class for building modules which
    connect to IP Fabric.
    """

    def __init__(self, module):
        self.module = module
        self.provider = module.params.get('provider')

        IPFABRIC_IMP_ERR = None
        try:
            from ipfabric import IPFClient
            from ipfabric import models
            HAS_IPFABRIC = True
        except ImportError:
            IPFABRIC_IMP_ERR = traceback.format_exc()
            HAS_IPFABRIC = False

        HTTPX_IMP_ERR = None

        try:
            import httpx
            HAS_HTTPX = True
        except ImportError:
            HTTPX_IMP_ERR = traceback.format_exc()
            HAS_HTTPX = False

        if not HAS_IPFABRIC:
            self.module.fail_json(msg=f'The IP Fabric collection requires ipfabric. Error: {missing_required_lib("ipfabric")}')

        if not HAS_HTTPX:
            self.module.fail_json(msg=f'The IP Fabric collection requires httpx. Error: {missing_required_lib("httpx")}')

        try:
            self.ipf = IPFClient(**self.module.params.get('provider'))
            self.models = models
        except httpx.HTTPStatusError as exc:
            self.module.fail_json(msg=f"Failed to connect: {exc.response.json()['message']} ({exc.response.json()['code']})")
        except httpx.ConnectTimeout as exc:
            self.module.fail_json(msg=f"Failed to connect: {exc}")

    def get_snapshot(self, snapshot_id):
        resp = self.ipf.get(f"snapshots/{snapshot_id}")
        resp.raise_for_status()
        snap = self.models.Snapshot(**resp.json())
        return snap

    def get_snapshots_list(self):
        resp = self.ipf.get_snapshots()
        return_list = []
        for k, v in resp.items():
            if k not in ['$last', '$prev']:
                return_list.append(v.dict())

        return return_list

    @staticmethod
    def provider_argument_spec():
        return dict(
            provider=dict(
                type="dict",
                options=dict(
                    base_url=dict(
                        type='str',
                        required=True,
                        fallback=(env_fallback, ['IPF_URL'])
                    ),
                    token=dict(type="str", required=True, fallback=(env_fallback, ['IPF_TOKEN']), no_log=True),
                    api_version=dict(type="str", required=False),
                    verify=dict(type="bool", required=False, default=True)
                ),
                required=True
            )
        )
