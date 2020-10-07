from rest_framework.throttling import UserRateThrottle

# Custom Throttle Classes
class LimitedRateThrottle(UserRateThrottle):
    scope = 'limited'

class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'