# CodingChallenge01
Return active business

Problem statement:
==================

Given list of user interaction events on "Site", return a
list of active business ids.

A business is considered active if in at least two event types, it has a
greater that (or equal to) number of events than the average for that event
type across all businesses.

The average for a given event types is found by averaging any occurrences of
the event type across all businesses, excluding the businesses where data is
not provided. For example, if  there's no page_views data for business 7, the 0
shouldn't be counted towards the page_views average.

Note 1:
-------

event type will never be repeated for the same biz_id.

Note 2:
-------

For computation average, we would  not consider missing event types. For example,
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
