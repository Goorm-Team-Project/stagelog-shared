from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

DEFAULT_NOTIFICATION_DETAIL_TYPE = "notification.system.broadcast"

NOTIFICATION_DETAIL_TYPE_MAP = {
    "comment": "notification.comment.created",
    "post_like": "notification.post.liked",
    "post_dislike": "notification.post.disliked",
    "event": "notification.event.updated",
    "notice": DEFAULT_NOTIFICATION_DETAIL_TYPE,
}


def to_detail_type(notification_type: str) -> str:
    return NOTIFICATION_DETAIL_TYPE_MAP.get(notification_type, DEFAULT_NOTIFICATION_DETAIL_TYPE)


@dataclass(slots=True)
class NotificationEventPayload:
    event_id: str
    schema_version: str
    source: str
    detail_type: str
    occurred_at: str
    recipient_user_id: int
    type: str
    message: str
    relate_url: Optional[str] = None
    post_id: Optional[int] = None
    related_event_id: Optional[int] = None
