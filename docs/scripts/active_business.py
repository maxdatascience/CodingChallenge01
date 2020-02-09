"""
Determine if business considered active based on occurrences in the events.

__author__ = 'Max Luckystar'
__email__ = 'data.maxluckystar@gmail.com'
__website__ = ''
__ copyright__ = 'Copyright 2020, Max Luckystar' __version__ = '1.0'

Problem statement: Given list of user interaction events on "Site", return a
list of active business ids.

A business is considered active if in at least two event types, it has a
greater that (or equal to) number of events than the average for that event
type across all businesses.

The average for a given event types is found by averaging any occurrences of
the event type across all businesses, excluding the businesses where data is
not provided. For example, if  there's no page_views data for business 7, the 0
shouldn't be counted towards the page_views average.

Note 1: event type will never be repeated for the same biz_id. Note 2: For
computation average, we would  not consider missing event types. For example,
if business 2 has 11 page_views, business 3 has 12 page_views and business 1
doesn't have an event for page_views, we treat the average number of page_views
as (11+12)/2.

Valid event types: photo_views, ads, page_views, reviews

Return: List of all active biz_ids sorted in ascending order of biz_id

Example: Input:  Event('ads', 7, 3) # event_type, occurrences, biz_id
                 Event('ads', 8, 2)
                 Event('ads', 5, 1)
                 Event('page_views', 11, 2)
                 Event('page_views', 12, 3)
                 Event('photo_views', 10, 3)
                 Event('reviews',7, 2)

Output: [2, 3]

Explanation: The average number of ads occurrences is (7+8+5)/3 = 6.67. The
average number of page_views occurrences is (11+12)/2 = 11.5. The average
number of photo_views occurrences is 10. The average number of reviews
occurrences is 7. Business 1 is below average in all event types. Business 2 is
at least average in both ads and reviews. Business 3 is at least average in
ads, page_views, and photo_views. Therefore, only business 2 and 3 are active.
"""


class Event:
    """Event class.

    Event streaming class
    """

    def __init__(self, event_type, occurrences, biz_id):
        """Create instance of the Event class.

        Arguments:
            event_type {string} -- type of event
            occurrences {number} -- number of occurrences in the events
            biz_id {number} -- business id
        """
        self.event_type = event_type
        self.occurrences = occurrences
        self.biz_id = biz_id


def find_active_businesses(events):
    """Find active business.

    Bissiness is active if occurrence of events >= average for this event type

    Arguments:
        events {list} -- contain the list of Event objects

    Returns:
        list -- List of active businesses
    """
    event_types = ['photo_views', 'ads', 'page_views', 'reviews']
    event_sum = [0]*4
    event_col = [0]*4
    # biz -  hash table. key - biz_id from events, value - list of events at 0
    # position, list of occurrences for events in 1 position ex. 3: [['ads',
    # 'page view', 'photo_views'], [7, 12, 10]]
    biz = {}
    biz_list = []

    for event in events:
        event_type = event.event_type
        if event_type in event_types:
            pos = event_types.index(event_type)
            event_sum[pos] += event.occurrences
            event_col[pos] += 1
            if biz.get(event.biz_id):
                if event_type in biz[event.biz_id][0]:
                    pos = biz[event.biz_id][0].index(event_type)
                    biz[event.biz_id][1][pos] += event.occurrences
                else:
                    biz[event.biz_id][0].append(event_type)
                    biz[event.biz_id][1].append(event.occurrences)
            else:
                biz[event.biz_id] = [
                    [event_type], [event.occurrences]]

    for biz_id, biz_event_col in biz.items():
        if len(biz_event_col[0]) >= 2:
            count_event = 0
            for event, numb in zip(biz_event_col[0], biz_event_col[1]):
                pos = event_types.index(event)
                avr = round(event_sum[pos] / event_col[pos], 0)
                if numb >= avr:
                    count_event += 1
                if count_event == 2:
                    biz_list.append(biz_id)
                    break
    biz_list.sort()
    return biz_list


if __name__ == "__main__":
    lines = [['ads', '7', '3'],
             ['ads', '8', '2'],
             ['ads', '5', '1'],
             ['page_views', '11', '2'],
             ['page_views', '12', '3'],
             ['photo_views', '10', '3'],
             ['reviews', '7', '2']]

    events = [Event(line[0], int(line[1]), int(line[2])) for line in lines]
    print(find_active_businesses(events))
