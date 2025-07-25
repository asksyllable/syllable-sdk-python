"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from typing import TYPE_CHECKING
from importlib import import_module

if TYPE_CHECKING:
    from .apierror import APIError
    from .httpvalidationerror import HTTPValidationError, HTTPValidationErrorData
    from .no_response_error import NoResponseError
    from .responsevalidationerror import ResponseValidationError
    from .syllablesdkerror import SyllableSDKError

__all__ = [
    "APIError",
    "HTTPValidationError",
    "HTTPValidationErrorData",
    "NoResponseError",
    "ResponseValidationError",
    "SyllableSDKError",
]

_dynamic_imports: dict[str, str] = {
    "APIError": ".apierror",
    "HTTPValidationError": ".httpvalidationerror",
    "HTTPValidationErrorData": ".httpvalidationerror",
    "NoResponseError": ".no_response_error",
    "ResponseValidationError": ".responsevalidationerror",
    "SyllableSDKError": ".syllablesdkerror",
}


def __getattr__(attr_name: str) -> object:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(
            f"No {attr_name} found in _dynamic_imports for module name -> {__name__} "
        )

    try:
        module = import_module(module_name, __package__)
        result = getattr(module, attr_name)
        return result
    except ImportError as e:
        raise ImportError(
            f"Failed to import {attr_name} from {module_name}: {e}"
        ) from e
    except AttributeError as e:
        raise AttributeError(
            f"Failed to get {attr_name} from {module_name}: {e}"
        ) from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)
