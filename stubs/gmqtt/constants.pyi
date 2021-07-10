import enum

# MQTT protocol versions
MQTTv311 = 4
MQTTv50 = 5


class PubRecReasonCode(enum.IntEnum):
    SUCCESS = 0
    NO_MATCHING_SUBSCRIBERS = 16
    UNSPECIFIED_ERROR = 128
    IMPLEMENTATION_SPECIFIC_ERROR = 131
    NOT_AUTHORIZED = 135
    TOPIC_NAME_INVALID = 144
    PACKET_IDENTIFIER_IN_USE = 145
    QUOTA_EXCEEDED = 151
    PAYLOAD_FORMAT_INVALID = 153
