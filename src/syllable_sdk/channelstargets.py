"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from syllable_sdk import models, utils
from syllable_sdk._hooks import HookContext
from syllable_sdk.types import OptionalNullable, UNSET
from syllable_sdk.utils import get_security_from_env
from typing import Any, List, Mapping, Optional


class ChannelsTargets(BaseSDK):
    def list_available(
        self,
        *,
        page: OptionalNullable[int] = UNSET,
        limit: Optional[int] = 25,
        search_fields: Optional[List[models.AvailableTargetProperties]] = None,
        search_field_values: Optional[List[str]] = None,
        order_by: OptionalNullable[models.AvailableTargetProperties] = UNSET,
        order_by_direction: OptionalNullable[models.OrderByDirection] = UNSET,
        fields: OptionalNullable[List[models.AvailableTargetProperties]] = UNSET,
        start_datetime: OptionalNullable[str] = UNSET,
        end_datetime: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListResponseAvailableTarget:
        r"""Available Targets List

        List the available phone numbers

        :param page:
        :param limit:
        :param search_fields:
        :param search_field_values:
        :param order_by:
        :param order_by_direction:
        :param fields:
        :param start_datetime:
        :param end_datetime:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.AvailableTargetsRequest(
            page=page,
            limit=limit,
            search_fields=search_fields,
            search_field_values=search_field_values,
            order_by=order_by,
            order_by_direction=order_by_direction,
            fields=fields,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        )

        req = self._build_request(
            method="GET",
            path="/api/v1/channels/available-targets",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="available_targets",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.ListResponseAvailableTarget
            )
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_available_async(
        self,
        *,
        page: OptionalNullable[int] = UNSET,
        limit: Optional[int] = 25,
        search_fields: Optional[List[models.AvailableTargetProperties]] = None,
        search_field_values: Optional[List[str]] = None,
        order_by: OptionalNullable[models.AvailableTargetProperties] = UNSET,
        order_by_direction: OptionalNullable[models.OrderByDirection] = UNSET,
        fields: OptionalNullable[List[models.AvailableTargetProperties]] = UNSET,
        start_datetime: OptionalNullable[str] = UNSET,
        end_datetime: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListResponseAvailableTarget:
        r"""Available Targets List

        List the available phone numbers

        :param page:
        :param limit:
        :param search_fields:
        :param search_field_values:
        :param order_by:
        :param order_by_direction:
        :param fields:
        :param start_datetime:
        :param end_datetime:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.AvailableTargetsRequest(
            page=page,
            limit=limit,
            search_fields=search_fields,
            search_field_values=search_field_values,
            order_by=order_by,
            order_by_direction=order_by_direction,
            fields=fields,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/v1/channels/available-targets",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="available_targets",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.ListResponseAvailableTarget
            )
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
