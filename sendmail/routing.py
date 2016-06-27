from channels.routing import route

from .consumers import handle_send_mail
from .wrap import get_channel_name

channel_routing = [
    route(get_channel_name(), handle_send_mail),
]
