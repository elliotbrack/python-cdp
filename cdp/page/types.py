'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: page
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from ..network import types as network


class FrameId(str):
    '''
    Unique frame identifier.
    '''
    @classmethod
    def from_response(cls, response):
        return cls(response)

    def __repr__(self):
        return 'FrameId({})'.format(str.__repr__(self))


class ScriptIdentifier(str):
    '''
    Unique script identifier.
    '''
    @classmethod
    def from_response(cls, response):
        return cls(response)

    def __repr__(self):
        return 'ScriptIdentifier({})'.format(str.__repr__(self))



class TransitionType:
    '''
    Transition type.
    '''
    LINK = "link"
    TYPED = "typed"
    ADDRESS_BAR = "address_bar"
    AUTO_BOOKMARK = "auto_bookmark"
    AUTO_SUBFRAME = "auto_subframe"
    MANUAL_SUBFRAME = "manual_subframe"
    GENERATED = "generated"
    AUTO_TOPLEVEL = "auto_toplevel"
    FORM_SUBMIT = "form_submit"
    RELOAD = "reload"
    KEYWORD = "keyword"
    KEYWORD_GENERATED = "keyword_generated"
    OTHER = "other"


class DialogType:
    '''
    Javascript dialog type.
    '''
    ALERT = "alert"
    CONFIRM = "confirm"
    PROMPT = "prompt"
    BEFOREUNLOAD = "beforeunload"


class ClientNavigationReason:
    FORM_SUBMISSION_GET = "formSubmissionGet"
    FORM_SUBMISSION_POST = "formSubmissionPost"
    HTTP_HEADER_REFRESH = "httpHeaderRefresh"
    SCRIPT_INITIATED = "scriptInitiated"
    META_TAG_REFRESH = "metaTagRefresh"
    PAGE_BLOCK_INTERSTITIAL = "pageBlockInterstitial"
    RELOAD = "reload"


@dataclass
class Frame:
    '''
    Information about the Frame on the page.
    '''
    #: Frame unique identifier.
    id: str

    #: Parent frame identifier.
    parent_id: str

    #: Identifier of the loader associated with this frame.
    loader_id: network.LoaderId

    #: Frame's name as specified in the tag.
    name: str

    #: Frame document's URL.
    url: str

    #: Frame document's security origin.
    security_origin: str

    #: Frame document's mimeType as determined by the browser.
    mime_type: str

    #: If the frame failed to load, this contains the URL that could not be loaded.
    unreachable_url: str

    @classmethod
    def from_response(cls, response):
        return cls(
            id=str(response.get('id')),
            parent_id=str(response.get('parentId')),
            loader_id=network.LoaderId.from_response(response.get('loaderId')),
            name=str(response.get('name')),
            url=str(response.get('url')),
            security_origin=str(response.get('securityOrigin')),
            mime_type=str(response.get('mimeType')),
            unreachable_url=str(response.get('unreachableUrl')),
        )


@dataclass
class FrameResource:
    '''
    Information about the Resource on the page.
    '''
    #: Resource URL.
    url: str

    #: Type of this resource.
    type_: network.ResourceType

    #: Resource mimeType as determined by the browser.
    mime_type: str

    #: last-modified timestamp as reported by server.
    last_modified: network.TimeSinceEpoch

    #: Resource content size.
    content_size: float

    #: True if the resource failed to load.
    failed: bool

    #: True if the resource was canceled during loading.
    canceled: bool

    @classmethod
    def from_response(cls, response):
        return cls(
            url=str(response.get('url')),
            type_=network.ResourceType.from_response(response.get('type')),
            mime_type=str(response.get('mimeType')),
            last_modified=network.TimeSinceEpoch.from_response(response.get('lastModified')),
            content_size=float(response.get('contentSize')),
            failed=bool(response.get('failed')),
            canceled=bool(response.get('canceled')),
        )


@dataclass
class FrameResourceTree:
    '''
    Information about the Frame hierarchy along with their cached resources.
    '''
    #: Frame information for this tree item.
    frame: Frame

    #: Child frames.
    child_frames: typing.List['FrameResourceTree']

    #: Information about frame resources.
    resources: typing.List['FrameResource']

    @classmethod
    def from_response(cls, response):
        return cls(
            frame=Frame.from_response(response.get('frame')),
            child_frames=[FrameResourceTree.from_response(i) for i in response.get('childFrames')],
            resources=[FrameResource.from_response(i) for i in response.get('resources')],
        )


@dataclass
class FrameTree:
    '''
    Information about the Frame hierarchy.
    '''
    #: Frame information for this tree item.
    frame: Frame

    #: Child frames.
    child_frames: typing.List['FrameTree']

    @classmethod
    def from_response(cls, response):
        return cls(
            frame=Frame.from_response(response.get('frame')),
            child_frames=[FrameTree.from_response(i) for i in response.get('childFrames')],
        )


@dataclass
class NavigationEntry:
    '''
    Navigation history entry.
    '''
    #: Unique id of the navigation history entry.
    id: int

    #: URL of the navigation history entry.
    url: str

    #: URL that the user typed in the url bar.
    user_typed_url: str

    #: Title of the navigation history entry.
    title: str

    #: Transition type.
    transition_type: TransitionType

    @classmethod
    def from_response(cls, response):
        return cls(
            id=int(response.get('id')),
            url=str(response.get('url')),
            user_typed_url=str(response.get('userTypedURL')),
            title=str(response.get('title')),
            transition_type=TransitionType.from_response(response.get('transitionType')),
        )


@dataclass
class ScreencastFrameMetadata:
    '''
    Screencast frame metadata.
    '''
    #: Top offset in DIP.
    offset_top: float

    #: Page scale factor.
    page_scale_factor: float

    #: Device screen width in DIP.
    device_width: float

    #: Device screen height in DIP.
    device_height: float

    #: Position of horizontal scroll in CSS pixels.
    scroll_offset_x: float

    #: Position of vertical scroll in CSS pixels.
    scroll_offset_y: float

    #: Frame swap timestamp.
    timestamp: network.TimeSinceEpoch

    @classmethod
    def from_response(cls, response):
        return cls(
            offset_top=float(response.get('offsetTop')),
            page_scale_factor=float(response.get('pageScaleFactor')),
            device_width=float(response.get('deviceWidth')),
            device_height=float(response.get('deviceHeight')),
            scroll_offset_x=float(response.get('scrollOffsetX')),
            scroll_offset_y=float(response.get('scrollOffsetY')),
            timestamp=network.TimeSinceEpoch.from_response(response.get('timestamp')),
        )


@dataclass
class AppManifestError:
    '''
    Error while paring app manifest.
    '''
    #: Error message.
    message: str

    #: If criticial, this is a non-recoverable parse error.
    critical: int

    #: Error line.
    line: int

    #: Error column.
    column: int

    @classmethod
    def from_response(cls, response):
        return cls(
            message=str(response.get('message')),
            critical=int(response.get('critical')),
            line=int(response.get('line')),
            column=int(response.get('column')),
        )


@dataclass
class LayoutViewport:
    '''
    Layout viewport position and dimensions.
    '''
    #: Horizontal offset relative to the document (CSS pixels).
    page_x: int

    #: Vertical offset relative to the document (CSS pixels).
    page_y: int

    #: Width (CSS pixels), excludes scrollbar if present.
    client_width: int

    #: Height (CSS pixels), excludes scrollbar if present.
    client_height: int

    @classmethod
    def from_response(cls, response):
        return cls(
            page_x=int(response.get('pageX')),
            page_y=int(response.get('pageY')),
            client_width=int(response.get('clientWidth')),
            client_height=int(response.get('clientHeight')),
        )


@dataclass
class VisualViewport:
    '''
    Visual viewport position, dimensions, and scale.
    '''
    #: Horizontal offset relative to the layout viewport (CSS pixels).
    offset_x: float

    #: Vertical offset relative to the layout viewport (CSS pixels).
    offset_y: float

    #: Horizontal offset relative to the document (CSS pixels).
    page_x: float

    #: Vertical offset relative to the document (CSS pixels).
    page_y: float

    #: Width (CSS pixels), excludes scrollbar if present.
    client_width: float

    #: Height (CSS pixels), excludes scrollbar if present.
    client_height: float

    #: Scale relative to the ideal viewport (size at width=device-width).
    scale: float

    #: Page zoom factor (CSS to device independent pixels ratio).
    zoom: float

    @classmethod
    def from_response(cls, response):
        return cls(
            offset_x=float(response.get('offsetX')),
            offset_y=float(response.get('offsetY')),
            page_x=float(response.get('pageX')),
            page_y=float(response.get('pageY')),
            client_width=float(response.get('clientWidth')),
            client_height=float(response.get('clientHeight')),
            scale=float(response.get('scale')),
            zoom=float(response.get('zoom')),
        )


@dataclass
class Viewport:
    '''
    Viewport for capturing screenshot.
    '''
    #: X offset in device independent pixels (dip).
    x: float

    #: Y offset in device independent pixels (dip).
    y: float

    #: Rectangle width in device independent pixels (dip).
    width: float

    #: Rectangle height in device independent pixels (dip).
    height: float

    #: Page scale factor.
    scale: float

    @classmethod
    def from_response(cls, response):
        return cls(
            x=float(response.get('x')),
            y=float(response.get('y')),
            width=float(response.get('width')),
            height=float(response.get('height')),
            scale=float(response.get('scale')),
        )


@dataclass
class FontFamilies:
    '''
    Generic font families collection.
    '''
    #: The standard font-family.
    standard: str

    #: The fixed font-family.
    fixed: str

    #: The serif font-family.
    serif: str

    #: The sansSerif font-family.
    sans_serif: str

    #: The cursive font-family.
    cursive: str

    #: The fantasy font-family.
    fantasy: str

    #: The pictograph font-family.
    pictograph: str

    @classmethod
    def from_response(cls, response):
        return cls(
            standard=str(response.get('standard')),
            fixed=str(response.get('fixed')),
            serif=str(response.get('serif')),
            sans_serif=str(response.get('sansSerif')),
            cursive=str(response.get('cursive')),
            fantasy=str(response.get('fantasy')),
            pictograph=str(response.get('pictograph')),
        )


@dataclass
class FontSizes:
    '''
    Default font sizes.
    '''
    #: Default standard font size.
    standard: int

    #: Default fixed font size.
    fixed: int

    @classmethod
    def from_response(cls, response):
        return cls(
            standard=int(response.get('standard')),
            fixed=int(response.get('fixed')),
        )
