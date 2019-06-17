'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: browser
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *
from ..target import types as target



class Browser:
    @staticmethod
    def grant_permissions(origin: str, permissions: typing.List['PermissionType'], browser_context_id: target.BrowserContextID) -> None:
        '''
        Grant specific permissions to the given origin and reject all others.
        
        :param origin: 
        :param permissions: 
        :param browser_context_id: BrowserContext to override permissions. When omitted, default browser context is used.
        '''

        cmd_dict = {
            'method': 'Browser.grantPermissions',
            'params': {
                'origin': origin,
                'permissions': permissions,
                'browserContextId': browser_context_id,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def reset_permissions(browser_context_id: target.BrowserContextID) -> None:
        '''
        Reset all permission management for all origins.
        
        :param browser_context_id: BrowserContext to reset permissions. When omitted, default browser context is used.
        '''

        cmd_dict = {
            'method': 'Browser.resetPermissions',
            'params': {
                'browserContextId': browser_context_id,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def close() -> None:
        '''
        Close browser gracefully.
        '''

        cmd_dict = {
            'method': 'Browser.close',
        }
        response = yield cmd_dict

    @staticmethod
    def crash() -> None:
        '''
        Crashes browser on the main thread.
        '''

        cmd_dict = {
            'method': 'Browser.crash',
        }
        response = yield cmd_dict

    @staticmethod
    def crash_gpu_process() -> None:
        '''
        Crashes GPU process.
        '''

        cmd_dict = {
            'method': 'Browser.crashGpuProcess',
        }
        response = yield cmd_dict

    @staticmethod
    def get_version() -> dict:
        '''
        Returns version information.
        :returns: a dict with the following keys:
            * protocolVersion: Protocol version.
            * product: Product name.
            * revision: Product revision.
            * userAgent: User-Agent.
            * jsVersion: V8 version.
        '''

        cmd_dict = {
            'method': 'Browser.getVersion',
        }
        response = yield cmd_dict
        return {
                'protocolVersion': str.from_response(response['protocolVersion']),
                'product': str.from_response(response['product']),
                'revision': str.from_response(response['revision']),
                'userAgent': str.from_response(response['userAgent']),
                'jsVersion': str.from_response(response['jsVersion']),
            }

    @staticmethod
    def get_browser_command_line() -> typing.List:
        '''
        Returns the command line switches for the browser process if, and only if
        --enable-automation is on the commandline.
        :returns: Commandline parameters
        '''

        cmd_dict = {
            'method': 'Browser.getBrowserCommandLine',
        }
        response = yield cmd_dict
        return [str(i) for i in response['arguments']]

    @staticmethod
    def get_histograms(query: str, delta: bool) -> typing.List['Histogram']:
        '''
        Get Chrome histograms.
        
        :param query: Requested substring in name. Only histograms which have query as a
        substring in their name are extracted. An empty or absent query returns
        all histograms.
        :param delta: If true, retrieve delta since last call.
        :returns: Histograms.
        '''

        cmd_dict = {
            'method': 'Browser.getHistograms',
            'params': {
                'query': query,
                'delta': delta,
            }
        }
        response = yield cmd_dict
        return [Histogram.from_response(i) for i in response['histograms']]

    @staticmethod
    def get_histogram(name: str, delta: bool) -> Histogram:
        '''
        Get a Chrome histogram by name.
        
        :param name: Requested histogram name.
        :param delta: If true, retrieve delta since last call.
        :returns: Histogram.
        '''

        cmd_dict = {
            'method': 'Browser.getHistogram',
            'params': {
                'name': name,
                'delta': delta,
            }
        }
        response = yield cmd_dict
        return Histogram.from_response(response['histogram'])

    @staticmethod
    def get_window_bounds(window_id: WindowID) -> Bounds:
        '''
        Get position and size of the browser window.
        
        :param window_id: Browser window id.
        :returns: Bounds information of the window. When window state is 'minimized', the restored window
        position and size are returned.
        '''

        cmd_dict = {
            'method': 'Browser.getWindowBounds',
            'params': {
                'windowId': window_id,
            }
        }
        response = yield cmd_dict
        return Bounds.from_response(response['bounds'])

    @staticmethod
    def get_window_for_target(target_id: target.TargetID) -> dict:
        '''
        Get the browser window that contains the devtools target.
        
        :param target_id: Devtools agent host id. If called as a part of the session, associated targetId is used.
        :returns: a dict with the following keys:
            * windowId: Browser window id.
            * bounds: Bounds information of the window. When window state is 'minimized', the restored window
        position and size are returned.
        '''

        cmd_dict = {
            'method': 'Browser.getWindowForTarget',
            'params': {
                'targetId': target_id,
            }
        }
        response = yield cmd_dict
        return {
                'windowId': WindowID.from_response(response['windowId']),
                'bounds': Bounds.from_response(response['bounds']),
            }

    @staticmethod
    def set_window_bounds(window_id: WindowID, bounds: Bounds) -> None:
        '''
        Set position and/or size of the browser window.
        
        :param window_id: Browser window id.
        :param bounds: New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined
        with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
        '''

        cmd_dict = {
            'method': 'Browser.setWindowBounds',
            'params': {
                'windowId': window_id,
                'bounds': bounds,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_dock_tile(badge_label: str, image: str) -> None:
        '''
        Set dock tile details, platform-specific.
        
        :param badge_label: 
        :param image: Png encoded image.
        '''

        cmd_dict = {
            'method': 'Browser.setDockTile',
            'params': {
                'badgeLabel': badge_label,
                'image': image,
            }
        }
        response = yield cmd_dict
