'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: database
Experimental: True
'''

from dataclasses import dataclass, field
import typing


class DatabaseId(str):
    '''
    Unique identifier of Database object.
    '''
    @classmethod
    def from_response(cls, response):
        return cls(response)

    def __repr__(self):
        return 'DatabaseId({})'.format(str.__repr__(self))



@dataclass
class Database:
    '''
    Database object.
    '''
    #: Database ID.
    id: DatabaseId

    #: Database domain.
    domain: str

    #: Database name.
    name: str

    #: Database version.
    version: str

    @classmethod
    def from_response(cls, response):
        return cls(
            id=DatabaseId.from_response(response.get('id')),
            domain=str(response.get('domain')),
            name=str(response.get('name')),
            version=str(response.get('version')),
        )


@dataclass
class Error:
    '''
    Database error.
    '''
    #: Error message.
    message: str

    #: Error code.
    code: int

    @classmethod
    def from_response(cls, response):
        return cls(
            message=str(response.get('message')),
            code=int(response.get('code')),
        )
