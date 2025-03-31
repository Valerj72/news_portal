from django.utils import timezone

import pytz

def get_timezones(request):
    return {
        'current_time': timezone.localtime(timezone.now()),
        'timezones': pytz.common_timezones
    }