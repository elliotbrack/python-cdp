'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: security
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *


@dataclass
class CertificateError:
    '''
    There is a certificate error. If overriding certificate errors is enabled, then it should be
    handled with the `handleCertificateError` command. Note: this event does not fire if the
    certificate error has been allowed internally. Only one client per target should override
    certificate errors at the same time.
    '''
    #: There is a certificate error. If overriding certificate errors is enabled, then it should be
    #: handled with the `handleCertificateError` command. Note: this event does not fire if the
    #: certificate error has been allowed internally. Only one client per target should override
    #: certificate errors at the same time.
    event_id: int

    #: There is a certificate error. If overriding certificate errors is enabled, then it should be
    #: handled with the `handleCertificateError` command. Note: this event does not fire if the
    #: certificate error has been allowed internally. Only one client per target should override
    #: certificate errors at the same time.
    error_type: str

    #: There is a certificate error. If overriding certificate errors is enabled, then it should be
    #: handled with the `handleCertificateError` command. Note: this event does not fire if the
    #: certificate error has been allowed internally. Only one client per target should override
    #: certificate errors at the same time.
    request_url: str


@dataclass
class SecurityStateChanged:
    '''
    The security state of the page changed.
    '''
    #: The security state of the page changed.
    security_state: SecurityState

    #: The security state of the page changed.
    scheme_is_cryptographic: bool

    #: The security state of the page changed.
    explanations: typing.List['SecurityStateExplanation']

    #: The security state of the page changed.
    insecure_content_status: InsecureContentStatus

    #: The security state of the page changed.
    summary: str
